import sqlite_utils


def test_jq():
    db = sqlite_utils.Database(memory=True)
    result = list(db.query("select jq(?, ?) as result", ('{"foo": "bar"}', ".foo")))
    assert result == [{"result": '"bar"'}]
