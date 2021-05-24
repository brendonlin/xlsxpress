import pandas as pd
import sqlalchemy
from . import tools


def upload_xlsx(xlsx_path, conn_uri, sheet_name=None, table_name=None):

    if sheet_name is None:
        df_map = pd.read_excel(xlsx_path, sheet_name=sheet_name)
    else:
        df_map = pd.read_excel(xlsx_path, sheet_name=[sheet_name])
    for sheet_name in df_map.keys():
        df = df_map.get(sheet_name)
        conn = sqlalchemy.create_engine(conn_uri)
        if table_name is not None:
            table_name_ = table_name
        else:
            table_name_ = tools.create_table_name(
                xlsx_path=xlsx_path, sheet_name=sheet_name
            )
        df.to_sql(name=table_name_, con=conn, if_exists="replace", index=False)

    return {"is_success": 1}
