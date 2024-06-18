import smtplib
import ssl
from dotenv import load_dotenv
import os

load_dotenv()


def send_email(message):
    host = "smtp.gmail.com"
    port = 465
    username = "sanjaydangwal1999@gmail.com"
    password = os.getenv("PASSWORD")

    context = ssl.create_default_context()
    print("sending email")
    with smtplib.SMTP_SSL(host=host, port=port, context=context) as server:
        server.login(user=username, password=password)
        temp = server.sendmail(from_addr=username, to_addrs="sanjay.dangwal199@gmail.com", msg=message)
        print(temp)


if __name__ == "__main__":
    pass
