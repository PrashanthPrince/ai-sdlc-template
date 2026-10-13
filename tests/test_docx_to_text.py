import subprocess
import sys
import tempfile
import unittest
import zipfile
from pathlib import Path

from scripts.docx_to_text import extract_document_text

REPOSITORY_ROOT = Path(__file__).resolve().parents[1]
INPUT_DIRECTORY = REPOSITORY_ROOT / "docs" / "inputs"
DOCUMENT_XML = """\
<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<w:document xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main">
  <w:body>
    <w:p><w:pPr><w:pStyle w:val="Heading1"/></w:pPr><w:r><w:t>Goals</w:t></w:r></w:p>
    <w:p><w:r><w:t>Reduce customer effort</w:t></w:r></w:p>
    <w:tbl>
      <w:tr>
        <w:tc><w:p><w:r><w:t>Must have</w:t></w:r></w:p></w:tc>
        <w:tc><w:p><w:r><w:t>SSO login</w:t></w:r></w:p></w:tc>
      </w:tr>
    </w:tbl>
  </w:body>
</w:document>
"""


class DocxToTextTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temp_dir = tempfile.TemporaryDirectory(dir=INPUT_DIRECTORY)
        self.docx_path = Path(self.temp_dir.name) / "meeting.docx"
        with zipfile.ZipFile(self.docx_path, "w") as document:
            document.writestr("word/document.xml", DOCUMENT_XML)

    def tearDown(self) -> None:
        self.temp_dir.cleanup()

    def test_extracts_paragraphs_and_tables_in_document_order(self) -> None:
        text = extract_document_text(self.docx_path)

        self.assertIn("# [P0001] Goals", text)
        self.assertIn("[P0002] Reduce customer effort", text)
        self.assertIn(
            "T0001 R0001 C0001: [P0003] Must have | "
            "T0001 R0001 C0002: [P0004] SSO login",
            text,
        )
        self.assertLess(text.index("[P0002]"), text.index("T0001"))

    def test_rejects_non_docx_input(self) -> None:
        path = self.docx_path.with_suffix(".txt")
        path.write_text("not a docx", encoding="utf-8")

        with self.assertRaisesRegex(ValueError, "Expected a .docx file"):
            extract_document_text(path)

    def test_reports_invalid_docx_archive(self) -> None:
        self.docx_path.write_text("not a zip archive", encoding="utf-8")

        with self.assertRaises(zipfile.BadZipFile):
            extract_document_text(self.docx_path)

    def test_rejects_paths_outside_docs_inputs(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "meeting.docx"
            path.write_bytes(b"")

            with self.assertRaisesRegex(ValueError, "must be inside docs/inputs"):
                extract_document_text(path)

    def test_cli_prints_extracted_text(self) -> None:
        result = subprocess.run(
            [
                sys.executable,
                str(REPOSITORY_ROOT / "scripts" / "docx_to_text.py"),
                str(self.docx_path),
            ],
            check=True,
            capture_output=True,
            text=True,
        )

        self.assertIn("[P0002] Reduce customer effort", result.stdout)


if __name__ == "__main__":
    unittest.main()
