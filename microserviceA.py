import json
from flask import Flask, request, jsonify
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# references: https://dev.to/khaledhosseini/play-microservices-email-service-1kmc
# references: https://www.ory.sh/docs/kratos/self-hosted/email-http
# references: https://medium.com/the-andela-way/create-a-simple-microservice-with-celery-python-flask-redis-to-send-emails-with-gmail-api-224cc74ac7b3

# documentation: https://www.w3schools.com/python/ref_requests_post.asp
# documentation: https://pypi.org/project/requests/
# documentation: https://sentry.io/answers/flask-configure-dev-server-visibility/
# documentation: https://docs.python.org/3/library/email.mime.html
# documentation: https://docs.python.org/3/library/smtplib.html
# documentation: https://www.mailgun.com/blog/email/which-smtp-port-understanding-ports-25-465-587/

app = Flask(__name__)

# smtp server configuration 
SMTP_PORT = 587
SMTP_SERVER = 'smtp.gmail.com'
SENDER_EMAIL = 'your_email@gmail.com'
SENDER_PASSWORD = 'your_email_password' 

# endpoint to request data from and to receieve data also
@app.route('/send-email', methods=['POST'])
def sendEmail():
  try:
    content = request.get_json()

    # according to partner, JSON contains 'email' and 'message' parameters
    recipient_email = content.get('email')
    message = content.get('message')

    if not recipient_email or not message:
      return jsonify({"error": "Missing input"}), 400 # user/input error

    # Create the email message
    msg = MIMEMultipart()
    msg['To'] = recipient_email
    msg['From'] = SENDER_EMAIL
    msg['Subject'] = 'New message'
    msg.attach(MIMEText(message, 'plain'))

    # smtp server initiation
    with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
      server.starttls()
      server.login(SENDER_EMAIL, SENDER_PASSWORD) 
      text = msg.as_string()
      server.sendmail(SENDER_EMAIL, recipient_email, text)

    return jsonify({"status": "success", "message": "Email sent"}), 200 # success

  except Exception:
    return jsonify({"error": str(Exception)}), 500 # server error

if __name__ == '__main__':
  app.run(debug=True, port=5000, host='0.0.0.0')
