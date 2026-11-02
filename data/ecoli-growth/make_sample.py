# /// script
# requires-python = ">=3.12"
# dependencies = ["pandas", "openpyxl"]
# ///
"""Derive the smoke-test CSV sample from the published E. coli growth workbook.

The source workbook is downloaded from Zenodo and checked against the MD5
checksum that Zenodo publishes. It is never modified. One sheet is exported
to CSV unchanged: same columns, same header names, same values.

Run from the repository root:

    uv run data/ecoli-growth/make_sample.py
"""

import hashlib
import io
import urllib.request
from pathlib import Path

import pandas as pd

SOURCE_DOI = "10.5281/zenodo.19416053"
SOURCE_URL = "https://zenodo.org/api/records/19416053/files/Repo1pct.xlsx/content"
SOURCE_MD5 = "b52a4e3556b1d401799a4b43094bf2a5"
SHEET = "37_1%n2"  # 37 °C, 1 % glucose
OUTPUT = Path(__file__).parent / "ecoli-growth-37c-1pct.csv"


def main() -> None:
    with urllib.request.urlopen(SOURCE_URL) as response:
        workbook = response.read()
    md5 = hashlib.md5(workbook).hexdigest()
    if md5 != SOURCE_MD5:
        raise SystemExit(f"Checksum mismatch: expected {SOURCE_MD5}, got {md5}")

    sheet = pd.read_excel(io.BytesIO(workbook), sheet_name=SHEET)
    sheet.to_csv(OUTPUT, index=False)

    print(f"source  {SOURCE_DOI} Repo1pct.xlsx sheet {SHEET!r} md5 {md5}")
    print(f"output  {OUTPUT.name} {len(sheet)} rows, {len(sheet.columns)} columns")
    print(f"sha256  {hashlib.sha256(OUTPUT.read_bytes()).hexdigest()}")


if __name__ == "__main__":
    main()
