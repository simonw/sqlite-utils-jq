import jq
import json
import sqlite_utils


def sqlite_jq(value, expression):
    try:
        return json.dumps(jq.first(expression, json.loads(value)))
    except Exception as ex:
        return json.dumps({"error": str(ex)})


@sqlite_utils.hookimpl
def prepare_connection(conn):
    conn.create_function("jq", 2, sqlite_jq)
