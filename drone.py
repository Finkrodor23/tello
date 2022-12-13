import calendar
from datetime import datetime
import json
import random
import time
import boto3
from tello import tello

drone = tello()
drone.recv()

# Open kinesis stream
my_stream_name = 'Drone-Logs'
kinesis_client = boto3.client('kinesis', region_name='eu-central-1')

#New comment

def put_to_stream(thing_id, property_value, property_timestamp):
    payload = {
        'prop': str(property_value),
        'timestamp': str(property_timestamp),
        'thing_id': thing_id
    }
    print(payload)

    put_response = kinesis_client.put_record(
        StreamName=my_stream_name,
        Data=json.dumps(payload),
        PartitionKey=thing_id)
    print(put_response)


try:
    while True:
        property_value = random.randint(40, 120)
        property_timestamp = calendar.timegm(datetime.utcnow().timetuple())
        thing_id = 'aa-bb'

        put_to_stream(thing_id, property_value, property_timestamp)

        time.sleep(5)
except KeyboardInterrupt:
    print('interrupted!')

# Stream data to kinesis stream
# def stream_data_to_kinesis(drone, stream_name, kinesis_client):
#    while True:
#        data = drone.recv()
#        if data:
#            print(data)
#            kinesis_client.put_record(StreamName=stream_name, Data=data, PartitionKey="partitionkey")
