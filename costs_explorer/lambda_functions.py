from app.costs_explorer import CostsExplorer
from app.email_sender import EmailSender

def lambda_handler(event, context):
    
    ce = CostsExplorer()
    daily_report = ce.generate_report(ce.daily_report_kwargs)
    monthly_report = ce.generate_report(ce.monthly_report_kwargs)

    email_sender = EmailSender()
    email_sender.send(
        daily_billing_report=daily_report,
        monthly_billing_report=monthly_report
    )