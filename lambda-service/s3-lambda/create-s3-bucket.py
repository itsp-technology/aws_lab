import boto3
import json

s3 = boto3.client('s3')

def lambda_handler(event, context):
    s3.create_bucket(Bucket='my-bucket01001')
    return {
        'statusCode': 200,
        'body': json.dumps('create s3 bucket')
    }
