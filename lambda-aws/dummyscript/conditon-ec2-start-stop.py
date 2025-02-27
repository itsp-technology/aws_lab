import boto3
import os

region = 'us-east-1'
ami_id = 'ami-02a53b0d62d37a757'  
instance_type = 't2.micro'  
instances = ['i-0cfac58b7e4077372', 'i-0ca0a20ae7b2715b9']
ec2 = boto3.client('ec2', region_name=region)

def launch_instance():
    print("Launching New EC2 Instance")
    new_instance = ec2.run_instances(
        ImageId=ami_id,
        InstanceType=instance_type,
        MinCount=1,
        MaxCount=1,
        KeyName='personLap', 
    )
    new_instance_id = new_instance['Instances'][0]['InstanceId']
    print('New Instance Launched: {new_instance_id}')
    return new_instance_id

def check_instance(instance_id):
    try:
        response = ec2.describe_instances(InstanceIds=[instance_id])
        state = response['Reservations'][0]['Instances'][0]['State']['Name']
        return state
    except Exception as e:
        print(' Instance {instance_id} Not Found')
        return 'not_found'

def lambda_handler(event, context):
    schedule_name = event.get('resources', [])
    
    if schedule_name:
        rule_name = schedule_name[0]
        
        if 'start_ec2_instances' in rule_name:
            for instance in instances:
                state = check_instance(instance)
                if state == 'stopped':
                    ec2.start_instances(InstanceIds=[instance])
                    print(' Started Instance: {instance}')
                elif state == 'not_found':
                    new_instance = launch_instance()
                    instances.append(new_instance)

        elif 'stop_ec2_instances' in rule_name:
            ec2.stop_instances(InstanceIds=instances)
            print(' Stopped Instances:', instances)

        else:
            print(' No matching action found')

    else:
        print('No EventBridge rule trigger detected')
