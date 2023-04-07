import pytest

from utils import check_query

good_query_1 = '''{
   "dt_from": "2022-02-01T00:00:00",
   "dt_upto": "2022-02-02T00:00:00",
   "group_type": "hour"
}'''


good_query_2 = '''{
   "dt_from": "2021-02-01T00:00:00",
   "dt_upto": "2022-02-01T00:00:00",
   "group_type": "month"
}'''


bad_query_1 = '''{
   "dt_from": "2022-02-05T00:00:00",
   "dt_upto": "2022-02-02T00:00:00",
   "group_type": "hour"
}'''


bad_query_2 = '''{
   "dt_from": "2022-02-05T00:00:00",
   "dt_upto": "2022-02-02T00:00:00",
   "group_type": "year"
}'''


bad_query_3 = '''{ }'''


@pytest.mark.parametrize('query, expected_result', [(good_query_1, True),
                                                    (good_query_2, True)])
def test_check_query_good(query, expected_result):
    assert check_query(query) == expected_result


@pytest.mark.parametrize('query, expected_result', [(bad_query_1, False),
                                                    (bad_query_2, False),
                                                    (bad_query_3, False)])
def test_check_query_bad(query, expected_result):
    assert check_query(query) == expected_result
