import smtplib

def send_email(receiver_email, subject, content, sender_email, sender_password):
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(sender_email, sender_password)
        email_msg = f"Subject: {subject}\n\n{content}"
        server.sendmail(sender_email, receiver_email, email_msg)
        server.quit()
        return True
    except Exception as e:
        print(f"Email error: {e}")
        return False
