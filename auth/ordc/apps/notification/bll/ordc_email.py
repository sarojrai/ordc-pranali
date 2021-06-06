import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from . import email_config

class EmailManager:
    
  def notify(self, requested_data):
      is_success = True
      subject = requested_data.get("subject")
      email_ids = requested_data.get("email_ids")
      message_body  = requested_data.get("message_body")
      content_type = requested_data.get("content_type")
      resp = self.send_email(subject, email_ids, message_body, content_type=content_type) 
      return is_success, "message", resp

  def send_email(self, subject, email_ids, message_body, content_type='html'):
        emails_resp = []
        for email_id in email_ids:
              message = MIMEMultipart("alternative")
              message["Subject"] = subject
              message["From"] = email_config.DEFAULT_FROM_EMAIL
              message["To"] = email_id
              # Turn these into plain/html MIMEText objects
              if content_type == 'html':
                  part = MIMEText(message_body, "html")
                  message.attach(part)
              # Create secure connection with server and send email
              context = ssl.create_default_context()
              with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
                  server.login(email_config.DEFAULT_FROM_EMAIL, email_config.EMAIL_HOST_PASSWORD)
                  server.sendmail(
                      email_config.DEFAULT_FROM_EMAIL, email_id, message.as_string()
                  )
                  emails_resp.append({email_id:"Send"})
        return emails_resp



# ###Usage
# subject = "Order Confirmation(fulfillzy.com)"
# email_ids = ['guptaka691@gmail.com', 'ordcinfo@gmail.com']
# message_body = """\
# <html>
#   <body>
#     <p>Dear Customer,<br>
#        Your Order Number(ORDER_NUMBER)<br>
#        <a href="https://fulfillzy.com/">fulfillzy.com/</a> 
#        <br><br><br>Thank You!
#     </p>
#   </body>
# </html>
# """
# emails_resp = send_email(subject, email_ids, message_body, content_type='html')
# print(emails_resp)