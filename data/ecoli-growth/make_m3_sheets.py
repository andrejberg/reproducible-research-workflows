# /// script
# requires-python = ">=3.12"
# dependencies = ["pandas", "openpyxl"]
# ///
"""Export the three temperature sheets of module m3 from the published workbook.

The source workbook is downloaded from Zenodo and checked against the MD5
checksum that Zenodo publishes. It is never modified. Each sheet is exported
to CSV unchanged: same columns, same header names, same values, as in
make_sample.py.

Run from the repository root:

    uv run data/ecoli-growth/make_m3_sheets.py
"""

import hashlib
import io
import urllib.request
from pathlib import Path

import pandas as pd

SOURCE_DOI = "10.5281/zenodo.19416053"
SOURCE_URL = "https://zenodo.org/api/records/19416053/files/Repo1pct.xlsx/content"
SOURCE_MD5 = "b52a4e3556b1d401799a4b43094bf2a5"
SHEETS = {  # sheet name in Repo1pct.xlsx -> CSV file name
    "29_1%b": "ecoli-growth-29c-1pct.csv",
    "37_1%n2": "ecoli-growth-37c-1pct.csv",
    "45_1%b": "ecoli-growth-45c-1pct.csv",
}
OUTPUT = (Path(__file__).parents[2] / "modules" / "m3" / "starting-state"
          / "2026-11-05_ecoli-growth-temperatures" / "data" / "raw")


def main() -> None:
    with urllib.request.urlopen(SOURCE_URL) as response:
        workbook = response.read()
    md5 = hashlib.md5(workbook).hexdigest()
    if md5 != SOURCE_MD5:
        raise SystemExit(f"Checksum mismatch: expected {SOURCE_MD5}, got {md5}")

    print(f"source  {SOURCE_DOI} Repo1pct.xlsx md5 {md5}")
    OUTPUT.mkdir(parents=True, exist_ok=True)
    for sheet_name, file_name in SHEETS.items():
        sheet = pd.read_excel(io.BytesIO(workbook), sheet_name=sheet_name)
        target = OUTPUT / file_name
        sheet.to_csv(target, index=False)
        digest = hashlib.sha256(target.read_bytes()).hexdigest()
        print(f"{sheet_name!r:10} -> {file_name}  {len(sheet)} rows  sha256 {digest}")


if __name__ == "__main__":
    main()
