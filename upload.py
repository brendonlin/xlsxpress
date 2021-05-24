from xlsxp import config
from xlsxp import xlsxp
import argparse


CONN_MAP = config.read_conn_map()


parser = argparse.ArgumentParser(description="xlsx upload command paraser")
parser.add_argument("-p", "--xlsx_path")
parser.add_argument("-s", "--sheet_name", required=False)
parser.add_argument("-c", "--conn_name")
parser.add_argument("-t", "--table_name", default=None)


def main():

    args = parser.parse_args()
    conn_uri = CONN_MAP.get(args.conn_name)
    if conn_uri is None:
        raise Exception(
            f"connection name {args.conn_name} not found. Please check your config"
        )

    response = xlsxp.upload_xlsx(
        args.xlsx_path,
        conn_uri,
        sheet_name=args.sheet_name,
        table_name=args.table_name,
    )
    if response.get("is_success") == 0:
        raise Exception(f"Task faild:(")
    else:
        print("Task succeed:)")


if __name__ == "__main__":
    main()
