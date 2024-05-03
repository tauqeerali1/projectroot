from datetime import datetime

def datetime_to_str(dt):
    return dt.strftime('%Y-%m-%d %H:%M')

def str_to_datetime(s):
    return datetime.strptime(s, '%Y-%m-%d %H:%M')
