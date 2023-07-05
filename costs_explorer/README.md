# Costs Explorer
This AWS Lambda function is used to monitor the total daily and monthly costs incurred by a particular account. In the case of an Organization management account, the summary shows the total costs incurred by all accounts under a given Organization.

The report is sent via email using the AWS Simple Email Service (SES). In the SES ui manager, create a identity of type _Email address_, then insert the email of the sender.
The html of the email is easily enrichable and the request sento to the AWS Costs Explorer is easily configurable to receive more detailed reports.

A Lambda environment variable called `FROM_EMAIL_ADDRESS` must be configured in the Configuration tab of the Lambda. The value must be the email address previously added in the AWS Simple Email Service.

The trigger of this Lambda is created using AWS EventBridge in order to send email everyday at a specific interval of time. For do this, create a Rule in the AWS EventBridge console of type schedule, and put a cron string. Then select the already created Lambda function. 
