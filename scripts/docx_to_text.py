#!/usr/bin/env python3
"""Extract ordered text from a DOCX file with stable paragraph references."""

from __future__ import annotations

import argparse
import sys
import zipfile
from pathlib import Path
from xml.etree import ElementTree

WORD_NAMESPACE = "http://schemas.openxmlformats.org/wordprocessingml/2006/main"
DOCUMENT_XML = "word/document.xml"
NS = {"w": WORD_NAMESPACE}


def paragraph_text(paragraph: ElementTree.Element) -> str:
    parts: list[str] = []
    for element in paragraph.iter():
        if element.tag == f"{{{WORD_NAMESPACE}}}t":
            parts.append(element.text or "")
        elif element.tag == f"{{{WORD_NAMESPACE}}}tab":
            parts.append("\t")
        elif element.tag in {
            f"{{{WORD_NAMESPACE}}}br",
            f"{{{WORD_NAMESPACE}}}cr",
        }:
            parts.append("\n")
    return "".join(parts).strip()


def paragraph_style(paragraph: ElementTree.Element) -> str | None:
    style = paragraph.find("./w:pPr/w:pStyle", NS)
    if style is None:
        return None
    return style.get(f"{{{WORD_NAMESPACE}}}val")


def extract_document_text(path: Path) -> str:
    if path.suffix.lower() != ".docx":
        raise ValueError(f"Expected a .docx file: {path}")
    if not path.is_file():
        raise FileNotFoundError(f"Input file does not exist: {path}")

    with zipfile.ZipFile(path) as document:
        xml_content = document.read(DOCUMENT_XML)
    root = ElementTree.fromstring(xml_content)
    body = root.find("./w:body", NS)
    if body is None:
        raise ValueError(f"DOCX document has no body: {path}")

    lines: list[str] = []
    paragraph_number = 0
    table_number = 0

    def render_paragraph(paragraph: ElementTree.Element) -> str | None:
        nonlocal paragraph_number
        paragraph_number += 1
        text = paragraph_text(paragraph)
        if not text:
            return None

        reference = f"P{paragraph_number:04d}"
        style = paragraph_style(paragraph) or ""
        if style.startswith("Heading"):
            depth = style.removeprefix("Heading")
            level = int(depth) if depth.isdigit() else 2
            return f"{'#' * min(max(level, 1), 6)} [{reference}] {text}"
        return f"[{reference}] {text}"

    for child in body:
        if child.tag == f"{{{WORD_NAMESPACE}}}p":
            rendered = render_paragraph(child)
            if rendered:
                lines.append(rendered)
        elif child.tag == f"{{{WORD_NAMESPACE}}}tbl":
            table_number += 1
            for row_number, row in enumerate(child.findall("./w:tr", NS), start=1):
                cells: list[str] = []
                for cell_number, cell in enumerate(row.findall("./w:tc", NS), start=1):
                    cell_paragraphs = [
                        rendered
                        for paragraph in cell.findall("./w:p", NS)
                        if (rendered := render_paragraph(paragraph))
                    ]
                    if cell_paragraphs:
                        cells.append(
                            f"T{table_number:04d} R{row_number:04d} "
                            f"C{cell_number:04d}: {'; '.join(cell_paragraphs)}"
                        )
                if cells:
                    lines.append(" | ".join(cells))

    return "\n".join(lines)


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Extract DOCX paragraphs and tables with stable source references."
    )
    parser.add_argument("docx", type=Path, help="Path to a .docx file")
    args = parser.parse_args()

    try:
        print(extract_document_text(args.docx))
    except (FileNotFoundError, ValueError, zipfile.BadZipFile, KeyError, ElementTree.ParseError) as error:
        parser.error(str(error))
    return 0


if __name__ == "__main__":
    sys.exit(main())
