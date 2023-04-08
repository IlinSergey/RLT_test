from utils import check_hour

import pytest


@pytest.mark.parametrize('date1, date2, expected_result', [
    ('2022-02-02T00:00:00', '2022-02-01T23:00:00', False),
    ('2022-02-01T22:00:00', '2022-02-01T21:00:00', True)
    ])
def test_check_hour(date1, date2, expected_result):
    assert check_hour(date1, date2) == expected_result
