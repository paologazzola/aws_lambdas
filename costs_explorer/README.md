# Costs Explorer
This AWS Lambda function is used to monitor the total daily and monthly costs incurred by a particular account. In the case of an Organization management account, the summary shows the total costs incurred by all accounts under a given Organization.

The report is sent via email using the AWS Simple Email Service (SES). In the SES console, create an identity of type _Email address_, then insert the email of the sender. Repeat this procedure for recipient addresses too.
The html of the email is easily enrichable and the request sento to the AWS Costs Explorer is easily configurable to receive more detailed reports, if needed.

Two Lambda environment variables called `FROM_EMAIL_ADDRESS` and `TO_EMAIL_ADDRESSES` must be configured in the Configuration tab of the Lambda. The value of the first one must be the _FROM_ address, the value of the second one must be a string containining a list of recipient (_TO_ addresses). Every address previously mentioned must be added in the AWS Simple Email Service.
Example of variables:
- `FROM_EMAIL_ADDRESS`: `from@email.com`
- `TO_EMAIL_ADDRESSES`: `["first_recipient@email.com", "second_recipient@email.com"]`

The trigger of this Lambda is created using AWS EventBridge in order to send email everyday at a specific interval of time. For do this, create a Rule in the AWS EventBridge console of type schedule, and put a cron string. Then select the already created Lambda function.

Usefull docs:
- https://docs.aws.amazon.com/ses/latest/dg/send-an-email-using-sdk-programmatically.html
- https://docs.aws.amazon.com/ses/latest/dg/request-production-access.html (if you want to move out of the SES sandbox)
