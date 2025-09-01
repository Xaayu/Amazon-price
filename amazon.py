import requests
from bs4 import BeautifulSoup
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
                  "(KHTML, like Gecko) Chrome/127.0.0.1 Safari/537.36",
    "Accept-Language": "en-IN,en;q=0.9"
}

url = "https://www.amazon.in/Campus-Burgundy-Running-Shoes-9-5G-634/dp/B07KPWH6MW"
response = requests.get(url, headers=headers)

soup = BeautifulSoup(response.text, "html.parser")
s = soup.find("span", class_="a-price-whole").text
s = s.replace(",", "")   # remove commas from price if present
print(f"The current price is: ₹{s}")

set_price = 1000
current_price = float(s)

if current_price <= set_price:
    my_email = "yonohacks18@gmail.com"
    app_pass = "pvpyldwgqlwthlwy"
    to_email = "nexxgenn18@gmail.com"   # change to your receiver email

    subject = "Amazon Price Alert!"
    body = f"The price dropped! Current price is ₹{current_price}.\nCheck the link: {url}"

    # Create proper email with UTF-8 encoding
    msg = MIMEMultipart()
    msg["From"] = my_email
    msg["To"] = to_email
    msg["Subject"] = subject

    msg.attach(MIMEText(body, "plain", "utf-8"))

    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(my_email, app_pass)
        connection.sendmail(my_email, to_email, msg.as_string())

    print("Email sent successfully 🚀")
else:
    print("No alert. Price is still high.")