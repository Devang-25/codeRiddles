from datetime import datetime

epoch = datetime(1970,1,1)

# form datetime object from custom date
x = datetime(2015,1,25,23,59,59)
# OR
x = datetime(year=2015, day=25, month=1, hour=23, minute=59, second=59)
# datetime.datetime(2015, 1, 25, 23, 59, 59)

# datetime to string
tmp  = str(x)
# "2015-01-25 23:59:59"

# string to datetime
dt = datetime.strptime(tmp, "%Y-%m-%d %H:%M:%S")
# datetime.datetime(2015, 1, 25, 23, 59, 59)

# datetime to UNIX timestamp
def _normalize_tstamp(dt):
    td = dt - epoch
    return (td.microseconds + (td.seconds + td.days * 24 * 3600) * 10**6) / 1e6

_normalize_tstamp(dt)
# 1422230399.0

# UNIX to timestamp
datetime.utcfromtimestamp(1422230399.0)
# datetime.datetime(2015, 1, 25, 23, 59, 59)

# better version of to:UNIX  conversion @:
# http://www.markhneedham.com/blog/2014/10/20/python-converting-a-date-string-to-timestamp/

datetime.now().strftime("%Y-%m-%d_%H:%M:%S")
# '2017-12-21_20:18:09'
