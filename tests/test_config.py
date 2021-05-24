from xlsxp import config


def test_read_conn_map():
    conn_map = config.read_conn_map()
    print(conn_map)
