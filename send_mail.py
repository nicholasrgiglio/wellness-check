import smtplib
from email.mime.text import MIMEText

def send_mail(time,name,sleep,meals,work,exercise,meditation,happiness):
    port = 2525 #depends on the email service
    smtp_server = 'smtp.mailtrap.io'
    login = 'e5af5969a9fc5e'
    password = '02daba2be45da5'
    message = f"<h3> New Feedback Submission</h3><ul><li>Name: {name}</li>" \
              f"<li>Hours of Sleep: {sleep}</li>" \
              f"<li>Number of Meals: {meals}</li>" \
              f"<li>Hours of Work: {work}</li>" \
              f"<li>Exercise?: {exercise}</li>" \
              f"<li>Meditation: {meditation}</li>" \
              f"<li>Happiness: {happiness}</li></ul><br>" \
              f"Submitted at {time}."
    sender_email = 'email1@example.com'
    receiver_email = 'email2@example.com'
    msg = MIMEText(message,'html')
    msg['Subject'] = 'Wellness Submission'
    msg['From'] = sender_email
    msg['To'] = receiver_email

    # Send email
    with smtplib.SMTP(smtp_server,port) as server:
        server.login(login,password)
        server.sendmail(sender_email,receiver_email,msg.as_string())
