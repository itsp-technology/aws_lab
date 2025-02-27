import boto3  
region = 'us-east-1'
instances = ['i-0f6be46fbe136f281', 'i-0648877a98fb941e9']
ec2 = boto3.client('ec2', region_name=region)

def lambda_handler(event, context):
    ec2.start_instances(InstanceIds=instances)
    print('started your instances: ' + str(instances))