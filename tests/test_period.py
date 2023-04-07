import pytest
from dateutil.relativedelta import relativedelta

from utils import period

month = {'group_type': 'month'}
day = {'group_type': 'day'}
hour = {'group_type': 'hour'}


@pytest.mark.parametrize('p, expected_result',
                         [(month, relativedelta(months=1)),
                          (day, relativedelta(days=1)),
                          (hour, relativedelta(hours=1))])
def test_period(p, expected_result):
    assert period(p) == expected_result
