# -Code-an-AWS-Lambda-function-to-store-a-document-or-PDF-file-in-an-S3-bucket.-
2. Code an AWS Lambda function to store a document or PDF file in an S3 bucket.

Let's move on to the second Lambda function for uploading files to S3. I'll guide you step by step:

Create a new Lambda function:

Go back to Lambda console
Click "Create function"
Select "Author from scratch"
Function name: upload_to_s3
Runtime: Python 3.9
Architecture: x86_64

Type the code in the editor:

Add S3 permissions:

Click on "Configuration"
Click on "Permissions"
Click on the role name (it starts with your function name)
Click "Add permissions" → "Create inline policy"
Click "JSON" tab
Type policy

Replace "your-bucket-name" with your actual S3 bucket name
Click "Review policy"
Name it "S3UploadPolicy"
Click "Create policy"

After creating the policy 
Get back to the lambda function code editor
Deploy the code:
Type this into the Lambda code editor
Click "Deploy"

Test the function:
Click "Test"
Create a new test event with this JSON:
json
And in your test event:

Save this and click on test 
 
 

