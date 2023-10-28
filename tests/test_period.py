import os
import sys

import pytest
from dateutil.relativedelta import relativedelta

parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(parent_dir)

from utils import period

month = {'group_type': 'month'}
week = {'group_type': 'week'}
day = {'group_type': 'day'}
hour = {'group_type': 'hour'}


@pytest.mark.parametrize('p, expected_result',
                         [(month, relativedelta(months=1)),
                          (week, relativedelta(weeks=1)),
                          (day, relativedelta(days=1)),
                          (hour, relativedelta(hours=1))])
def test_period(p, expected_result):
    assert period(p) == expected_result
