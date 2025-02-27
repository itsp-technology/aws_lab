import boto3

region = 'us-east-1'  
ami_id = 'ami-02a53b0d62d37a757' 
instance_type = 't2.micro' 
key_name = 'personLap' 
security_group = ['sg-01250b867adf26816'] 

# Initialize EC2 client
ec2 = boto3.client('ec2', region_name=region)

def lambda_handler(event, context):
    try:
        response = ec2.run_instances(
            ImageId=ami_id,
            InstanceType=instance_type,
            KeyName=key_name,
            SecurityGroupIds=security_group,
            MinCount=1,
            MaxCount=1
        )
        instance_id = response['Instances'][0]['InstanceId']
        print(f'Launched EC2 instance: {instance_id}')
        return {
            'statusCode': 200,
            'body': f'Successfully launched EC2 instance: {instance_id}'
        }
    except Exception as e:
        print(f'Error launching instance: {str(e)}')
        return {
            'statusCode': 500,
            'body': f'Error launching EC2 instance: {str(e)}'
        }
