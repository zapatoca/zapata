import mock
from zapata.reminders import reminders


@mock.patch("sqlalchemy.engine.Engine.connect")
@mock.patch("sqlalchemy.engine.Engine.begin")
@mock.patch("pandas.read_sql_table")
def test_main(mocked_conntection, mocked_engine_begin, mocked_pandas_table):
    reminders.main()
    assert mocked_conntection
    assert mocked_engine_begin
    assert mocked_pandas_table
