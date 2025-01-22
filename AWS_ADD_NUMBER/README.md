# Write an AWS Lambda function that adds two numbers and returns the result
AWS: 1. Write an AWS Lambda function that adds two numbers and returns the result.

Here's the step-by-step process to implement these Lambda functions:
Function 1: Add Numbers

Create a new Lambda function:

Go to AWS Lambda Console
Click "Create function"
Choose "Author from scratch"
Name: add_numbers
Runtime: Python 3.9 (or later)
Architecture: x86_64
Click "Create function"
Type py code:

Deploy the code:
Type this into the Lambda code editor
Click "Deploy"

Test the function:
Click "Test"
Create a new test event with this JSON:
json
{
  "num1": 10,
  "num2": 20
}
Type this in json new test event
And click on save and run the test

Now u can see the output 
 


