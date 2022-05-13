import boto3

def handler(event, context):

    client = boto3.client('ec2')

    # Get Instance ID 
    filters = [ {'Name': 'tag-value', 'Values': [event['site']]}, {'Name': 'tag-value', 'Values': [event['type']]} ]

    response = client.describe_instances(Filters=filters)["Reservations"]
    instance_id = response[0]['Instances'][0]['InstanceId']

    # Stop the instance
    client.stop_instances(InstanceIds=[instance_id])
    waiter=client.get_waiter('instance_stopped')
    waiter.wait(InstanceIds=[instance_id])

    # Change the instance type
    client.modify_instance_attribute(InstanceId=instance_id, Attribute='instanceType', Value=event['size'])

    # Start the instance
    client.start_instances(InstanceIds=[instance_id])


