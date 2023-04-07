from pymongo import MongoClient

from datetime import datetime, timedelta
import calendar

import config

client = MongoClient(config.MONGO_LINK)
db = client[config.MONGO_DB]
collection = db['sample_collection']


def find_value_by_month(date: str):
    date_start = datetime.strptime(date, '%Y-%m-%dT00:00:00')
    days_in_month = calendar.monthrange(date_start.year, date_start.month)[1]
    date_end = date_start + timedelta(days=days_in_month)
    value = 0
    res = collection.find({'dt': {'$gte': date_start, '$lt': date_end}})
    for item in res:
        value += item['value']
    return value


def find_value_by_day(date: str):
    date_start = datetime.strptime(date, '%Y-%m-%dT00:00:00')
    date_end = date_start + timedelta(days=1)
    value = 0
    res = collection.find({'dt': {'$gte': date_start, '$lt': date_end}})
    for item in res:
        value += item['value']
    return value


def find_value_by_hour(date: str):
    date_start = datetime.strptime(date, '%Y-%m-%dT%H:%M:%S')
    date_end = date_start + timedelta(hours=1)
    value = 0
    res = collection.find({'dt': {'$gte': date_start, '$lte': date_end}})
    for item in res:
        value += item['value']
    return value
