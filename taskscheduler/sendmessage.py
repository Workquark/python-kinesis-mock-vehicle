import json
import boto3
from eventstream import Vehicle, DrivingLog


def job():
    log = DrivingLog.DriverLog()
    jsonStr = json.dumps(log.__dict__, sort_keys=True, default=str)
    client = boto3.client('kinesis')
    print(log.vehicleId)
    response = client.put_record(
        StreamName='Driverlog-DS',
        Data=bytes(jsonStr, 'utf-8'),
        PartitionKey= str(log.vehicleId),
        # ExplicitHashKey='string',
        # SequenceNumberForOrdering='string'
    )
    print(response)