import re
import os
import time


def create_table_name(xlsx_path: str, sheet_name: str) -> str:
    path_name_ = os.path.basename(xlsx_path).split(".")[0].lower()
    sheet_name_ = sheet_name.lower()
    pattern = re.compile(r"[a-z0-9_]+")
    if re.match(pattern, sheet_name_):
        name = sheet_name_
    elif re.match(pattern, path_name_):
        name = path_name_
    else:
        name = "table"
    timestamp = time.strftime("%Y%m%d_%H%m%S", time.localtime())
    return f"{name}_{timestamp}"
