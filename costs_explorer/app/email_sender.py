import boto3
import os


class EmailSender:    

    # recipient email address taken fromma AWS Lambda environment variables configuration
    RECIPIENT = os.environ['FROM_EMAIL_ADDRESS']
    
    SENDER = "AWS Cost Alert <{}>".format(os.environ['FROM_EMAIL_ADDRESS'])
    
    SUBJECT = "Daily AWS Billing Report"
    
    # The email body for recipients with non-HTML email clients.
    BODY_PLAIN_TEXT = """AWS Billing Costs \r\n
    Daily costs report\r\n
    {daily_billing_report}\r\n
    Monthly costs report\r\n
    {monthly_billing_report}\r\n
    """

    # The character encoding for the email.
    CHARSET = "UTF-8"

    # The HTML body of the email.
    BODY_HTML = """<html>
    <head></head>
    <body>
        <h1>AWS Costs Report</h1>
        <p>Some text here</p>
        <hr />
        <h3>Daily Costs</h3>
        <p>{daily_billing_report}</p>
        <hr />
        <h3>Monthly Costs</h3>
        <p>{monthly_billing_report}</p>
    </body>

    </html>
    """
    
    def __init__(self):
        self.client = boto3.client("ses")

    def send(self, daily_billing_report, monthly_billing_report):
        """Send an email which contains AWS billing data"""
        email_text = self.BODY_PLAIN_TEXT.format(
            daily_billing_report=daily_billing_report,
            monthly_billing_report=monthly_billing_report
        )

        email_html = self.BODY_HTML.format(
            daily_billing_report=daily_billing_report.replace("\n", "<br>"),
            monthly_billing_report=monthly_billing_report.replace("\n", "<br>")
        )
        response = self.client.send_email(
            Destination={
                "ToAddresses": [
                    self.RECIPIENT,
                ],
            },
            Message={
                "Body": {
                    "Html": {
                        "Charset": self.CHARSET,
                        "Data": email_html
                    },
                    "Text": {
                        "Charset": self.CHARSET,
                        "Data": email_text,
                    },
                },
                "Subject": {
                    "Charset": self.CHARSET,
                    "Data": self.SUBJECT,
                },
            },
            Source=self.SENDER,
        )
