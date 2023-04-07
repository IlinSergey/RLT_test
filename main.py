from datetimerange import DateTimeRange
from dateutil.relativedelta import relativedelta
from time import strptime

from db import find_value_by_month, find_value_by_day, find_value_by_hour


import json


def check_query(query: str):
    try:
        query = json.loads(query)
        dt_upto = strptime(query['dt_upto'], '%Y-%m-%dT%H:%M:%S')
        dt_from = strptime(query['dt_from'], '%Y-%m-%dT%H:%M:%S')
        return dt_upto > dt_from and query['group_type'] in ('hour', 'day', 'month')
    except Exception:
        return False


def period(query):
    period = None
    if query['group_type'] == 'month':
        period = relativedelta(months=1)
    elif query['group_type'] == 'day':
        period = relativedelta(days=1)
    else:
        period = relativedelta(hours=1)
    return period


def answer(query):
    check = check_query(query)
    if check:
        query = json.loads(query)

        time_list = []
        salary_list = []

        time_range = DateTimeRange(query['dt_from'], query['dt_upto'])
        for value in time_range.range(period(query)):
            time_list.append(value.strftime('%Y-%m-%dT%H:%M:%S'))

        for i in time_list:
            if query['group_type'] == 'month':
                x = find_value_by_month(i)
            elif query['group_type'] == 'day':
                x = find_value_by_day(i)
            else:
                x = find_value_by_hour(i)
            salary_list.append(x)

        response = {}
        response['dataset'] = salary_list
        response['labels'] = time_list
        return response
    correct_answer = '{"dt_from": "2022-09-01T00:00:00", \
"dt_upto": "2022-12-31T23:59:00", \
"group_type": "month"}'
    return f'Невалидный запрос. Пример запроса: {correct_answer}'
