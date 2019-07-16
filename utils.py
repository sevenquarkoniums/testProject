# some useful functions.
import pytz,datetime
import pandas as pd

def unix2string(unixTime):
    pacific = pytz.timezone('US/Pacific')
    thisTime = datetime.datetime.utcfromtimestamp(unixTime).replace(tzinfo=datetime.timezone.utc).astimezone(tz=pacific)
    timestr = thisTime.strftime('%Y-%m-%d %H:%M:%S')
    return timestr

def unix2pdTime(unixTime):
    return pd.Timestamp(unixTime, unit='s', tz='US/Pacific')

def string2unix(timeString):
    return datetime.datetime.strptime(timeString, '%m/%d/%Y, %H:%M:%S%z').timestamp()
