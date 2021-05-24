import configparser
import ipdb


def read_conn_map():
    config = configparser.ConfigParser()
    config.read("config.ini")
    conn_section = config["conn"]
    conn_map = {x: conn_section.get(x) for x in conn_section.keys()}
    return conn_map
