import json
from time import strptime
from datetime import datetime as dt

from datetimerange import DateTimeRange
from dateutil.relativedelta import relativedelta

from db import find_value_by_day, find_value_by_hour, find_value_by_month


def check_query(query: str):
    try:
        query = json.loads(query)
        dt_upto = strptime(query['dt_upto'], '%Y-%m-%dT%H:%M:%S')
        dt_from = strptime(query['dt_from'], '%Y-%m-%dT%H:%M:%S')
        return dt_upto > dt_from and query['group_type'] in ('hour', 'day', 'month')
    except Exception:
        return False


def period(query: dict):
    period = None
    if query['group_type'] == 'month':
        period = relativedelta(months=1)
    elif query['group_type'] == 'day':
        period = relativedelta(days=1)
    else:
        period = relativedelta(hours=1)
    return period


def check_hour(date_1: str, date_2: str):
    dt_last = dt.strptime(date_1, '%Y-%m-%dT%H:%M:%S')
    dt_prelast = dt.strptime(date_2, '%Y-%m-%dT%H:%M:%S')
    if dt_last.date() > dt_prelast.date():
        return False
    else:
        return True


def answer(query: str):
    check = check_query(query)
    if check:
        query = json.loads(query)

        time_list = []
        salary_list = []

        time_range = DateTimeRange(query['dt_from'], query['dt_upto'])
        for value in time_range.range(period(query)):
            time_list.append(value.strftime('%Y-%m-%dT%H:%M:%S'))

        period_len = len(time_list) - 1

        for count, item in enumerate(time_list):
            if query['group_type'] == 'month':
                x = find_value_by_month(item)
            elif query['group_type'] == 'day':
                x = find_value_by_day(item)
            else:
                if count == period_len:
                    if check_hour(time_list[count], time_list[count - 1]):
                        x = find_value_by_hour(item)
                    else:
                        x = 0
                elif count < period_len:
                    x = find_value_by_hour(item)
            salary_list.append(x)

        response = {}
        response['dataset'] = salary_list
        response['labels'] = time_list
        return response
    correct_answer = '{"dt_from": "2022-09-01T00:00:00", \
"dt_upto": "2022-12-31T23:59:00", \
"group_type": "month"}'
    return f'Невалидный запрос. Пример запроса: {correct_answer}'
