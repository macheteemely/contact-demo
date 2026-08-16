from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, EmailStr
from email.message import EmailMessage
from dotenv import load_dotenv
import smtplib
import os

load_dotenv()

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)


class Contact(BaseModel):
    name: str
    email: EmailStr
    message: str


@app.post("/contact")
def contact(data: Contact):
    

    email = EmailMessage()

    email["Subject"] = "New Portfolio Contact"
    email["From"] = os.getenv("EMAIL_ADDRESS")
    email["To"] = os.getenv("EMAIL_ADDRESS")

    email.set_content(
        f"""
Name: {data.name}

Email: {data.email}

Message:

{data.message}
"""
    )

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
        smtp.login(
            os.getenv("EMAIL_ADDRESS"),
            os.getenv("EMAIL_PASSWORD")
        )

        smtp.send_message(email)

    return {
        "message": "Your message has been sent successfully."
    }