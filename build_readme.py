#!/usr/bin/env python
from pathlib import Path

import pandoc

PATH_MAIN = Path(__file__).resolve().parent
FILE_README_MD = PATH_MAIN / "README.md"
FILE_README_RST = PATH_MAIN / "README.rst"

doc = pandoc.Document()
doc.markdown = FILE_README_MD.read_text(encoding="utf-8").encode("utf-8")
long_description = doc.rst.decode("utf-8")

FILE_README_RST.write_text(long_description, encoding="utf-8")
