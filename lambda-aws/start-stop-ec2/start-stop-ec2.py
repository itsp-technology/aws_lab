import boto3
import os

region = 'us-east-1'
instances = ['i-0cfac58b7e4077372', 'i-0ca0a20ae7b2715b9']
ec2 = boto3.client('ec2', region_name=region)

def lambda_handler(event, context):
    # Check if 'resources' key is available in the event payload
    schedule_name = event.get('resources', [])

    if schedule_name:
        rule_name = schedule_name[0]  # Get the first resource ARN
        
        if 'start_ec2_instances' in rule_name:
            ec2.start_instances(InstanceIds=instances)
            print('Started Instances:', instances)
        
        elif 'stop_ec2_instances' in rule_name:
            ec2.stop_instances(InstanceIds=instances)
            print('Stopped Instances:', instances)
            
        else:
            print('No matching action found')

    else:
        print('🚫 No EventBridge rule trigger detected')
