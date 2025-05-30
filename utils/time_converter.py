# utils/time_converter.py

from datetime import datetime
import pytz

def convert_to_utc(local_datetime_str, timezone_str):
    """문자열 로컬 시간과 타임존을 받아 UTC datetime으로 변환."""
    local = pytz.timezone(timezone_str)
    local_dt = local.localize(datetime.strptime(local_datetime_str, "%Y-%m-%d %H:%M"))
    utc_dt = local_dt.astimezone(pytz.utc)
    return utc_dt
