import boto3  
region = 'us-east-1'
instances = ['i-0648877a98fb941e9', 'i-0f6be46fbe136f281']
ec2 = boto3.client('ec2', region_name=region)
       
def lambda_handler(event, context):
    ec2.stop_instances(InstanceIds=instances)
    print('stopped your instances: ' + str(instances))