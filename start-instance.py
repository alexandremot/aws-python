
import boto3
import json


def start_instance():
	ids_list = []

	ec2_cli = boto3.client('ec2', region_name='us-east-2')

	instance_id = ec2_cli.describe_instances()['Reservations'][1]['Instances'][0]['InstanceId']

	ids_list.append(instance_id)

	print(ids_list)

	a = ec2_cli.start_instances(InstanceIds=ids_list)

	print(a)

if __name__ == "__main__":
    start_instance()
