import smtplib, ssl
password = ""

def send_email(receiver_email, message):
    port = 465 
    smtp_server = "smtp.gmail.com"
    sender_email = "robertminzat@gmail.com" 


    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message)