# ResizeEC2
Resize EC2 instances using Lambda and CloudWatch Events

Invoke Lambda to resize instances:
aws lambda invoke --function-name ec2-lambda-resize --payload '{"site": "site", "type": "type", "size": "t3.large"}' output
