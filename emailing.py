import smtplib
from email.message import EmailMessage
import imghdr

PASSWORD = "dpwhnkitvxrjdopg"
SENDER = "jgtefera@gmail.com"
RECIEVER = "jgtefera@gmail.com"


def send_email(img_path):
    email_message = EmailMessage()
    email_message["Subject"] = "Intruder in your room !"
    email_message.set_content("Hey Joey Stark, we detected an intruder !")

    with open(img_path, "rb") as file:
        content = file.read()
    email_message.add_attachment(content, maintype="image", subtype=imghdr.what(None, content))

    gmail = smtplib.SMTP("smtp.gmail.com", 587)
    gmail.ehlo()
    gmail.starttls()
    gmail.login(SENDER, PASSWORD)
    gmail.sendmail(SENDER, RECIEVER, email_message.as_string())
    gmail.quit()

if __name__ == "__main__":
    send_email()
