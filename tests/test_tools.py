from xlsxp import tools


def test_create_table_name():
    cases = [
        ("tests/data/ABC.xlsx", "sheet1", "sheet"),
        ("tests/data/abc.xlsx", "电子簿", "abc"),
        ("tests/data/中文.xlsx", "电子簿", "table"),
    ]
    for case in cases:
        xlsx_path, sheet_name, expected = case
        result = tools.create_table_name(xlsx_path, sheet_name)
        assert result.startswith(expected)
