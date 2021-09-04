import json

from eventstream import Vehicle,DrivingLog


def job():
    log = DrivingLog.DriverLog()
    print(json.dumps(log.__dict__,sort_keys=True, default=str))
