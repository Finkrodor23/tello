from tello import tello
import boto3

client = boto3.client('s3')

drone = tello()

drone.recv()

#Stream data to kinesis stream
#def stream_data_to_kinesis(drone, stream_name, kinesis_client):
#    while True:
#        data = drone.recv()
#        if data:
#            print(data)
#            kinesis_client.put_record(StreamName=stream_name, Data=data, PartitionKey="partitionkey")

