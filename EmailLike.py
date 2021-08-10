from email import message
from email.message import EmailMessage
from email.mime import text
from re import X
import selenium
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

from etext import send_sms_via_email


phone_number = "954-648-4490"
message = "big chungo"
provider = "Verizon"

sender_credentials = ("scammerscansuckitlol@gmail.com", "TreeMan1!")

send_sms_via_email(
    phone_number, message, provider, sender_credentials, subject="pog"
)

print("Start")
a =0
iNext =0
i = 0

time.sleep(3)

driver = webdriver.Chrome(ChromeDriverManager().install())

driver1 = webdriver.Chrome(ChromeDriverManager().install())


driver.get('https://www.tiktok.com/@gordonramsayofficial/video/6916583398500748550?lang=en&is_copy_url=1&is_from_webapp=v1')

time.sleep(10)


TEXT = driver.find_element_by_xpath('//*[@id="main"]/div[2]/div[2]/div/div/main/div/div[1]/span[1]/div/div[1]/div[5]/div[2]/div[1]').text

print(TEXT)

print("working")


def convert_str_to_number(TEXT):
    total_stars = 0
    global i
    global a
    global iNext
    i1 =0
    if(a==0):
        i = 259990
        i1 = 259990
    if(a>0):
        i1 = iNext

    num_map = {'K':1000, 'M':1000000, 'B':1000000000}
    if TEXT.isdigit():
        total_stars = int(TEXT)
    else:
        if len(TEXT) > 1:
            total_stars = float(TEXT[:-1]) * num_map.get(TEXT[-1].upper(), 1)
    print(total_stars)
    print(i1)

    while i1 < total_stars:
        if i1 % 2 == 0:
            email = 'geeimatree101@gmail.com'
            password = 'TreeMan1!'
            send_to_email = 'raymondemaldonado1@gmail.com'
            subject = 'This is working'
            message = 'https://www.youtube.com/watch?v=dQw4w9WgXcQ'
            msg = MIMEMultipart()
            msg['From'] = email
            msg['To'] = send_to_email
            msg['Subject'] = subject
            msg.attach(MIMEText(message, 'plain'))
            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.starttls()
            server.login(email, password)
            text = msg.as_string()
            server.sendmail(email, send_to_email, text)
            server.quit()
            i1 += 1
        if i1 % 2 != 0:
            email1 = 'scammerscansuckitlol@gmail.com'
            password1 = 'TreeMan1!'
            send_to_email1 = 'raymondemaldonado1@gmail.com'
            subject1 = 'This is still working'
            message = 'https://www.youtube.com/watch?v=dQw4w9WgXcQ'
            msg = MIMEMultipart()
            msg['From'] = email1
            msg['To'] = send_to_email1
            msg['Subject'] = subject1
            msg.attach(MIMEText(message, 'plain'))
            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.starttls()
            server.login(email1, password1)
            text = msg.as_string()
            server.sendmail(email1, send_to_email1, text)
            server.quit()
            i1 += 1  
    a+= 1
    print(i1)
    iNext = i1
    print(iNext)

    if(a==1):
        print("Round 2")
        time.sleep(10)

        driver1.get('https://www.tiktok.com/@gordonramsayofficial/video/6916583398500748550?lang=en&is_copy_url=1&is_from_webapp=v1')

        TEXT1 = driver1.find_element_by_xpath('//*[@id="main"]/div[2]/div[2]/div/div/main/div/div[1]/span[1]/div/div[1]/div[5]/div[2]/div[1]').text

        convert_str_to_number(TEXT1)

    return int(total_stars)
    
convert_str_to_number(TEXT)
print("complete")


