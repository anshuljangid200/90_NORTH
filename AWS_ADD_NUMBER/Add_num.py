import json
def lambda_handler(event, context):
 try:

 num1 = event['num1']
 num2 = event['num2']


 if not (isinstance(num1, (int, float)) and isinstance(num2, (int, float))):
 raise ValueError("Input values must be numbers")


 result = num1 + num2


 response = {
 'statusCode': 200,
 'body': json.dumps({
 'result': result,
 'message': 'Success'
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
 except ValueError as e:
 response = {
 'statusCode': 400,
 'body': json.dumps({
 'error': 'Invalid input',
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
