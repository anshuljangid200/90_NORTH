import json
import boto3
import base64
def lambda_handler(event, context):
 try:
 # Initialize S3 client
 s3_client = boto3.client('s3')

 # Extract file data and name from event
 file_content = event['file_content']
 file_name = event['file_name']
 bucket_name = event['bucket_name']

 # Decode base64 file content
 file_data = base64.b64decode(file_content)

 # Upload to S3
 s3_client.put_object(
 Bucket=bucket_name,
 Key=file_name,
 Body=file_data
 )

 # Prepare success response
 response = {
 'statusCode': 200,
 'body': json.dumps({
 'message': 'File uploaded successfully',
 'file_name': file_name,
 'bucket': bucket_name
 })
 }

 except KeyError as e:
 response = {
 'statusCode': 400,
 'body': json.dumps({
 'error': 'Missing required parameters',
 'message': str(e)
 })
 }
 except Exception as e:
 response = {
 'statusCode': 500,
 'body': json.dumps({
 'error': 'Internal server error',
 'message': str(e)
 })
 }

 return response
