import smtplib
import datetime as dt
import random


# CONSTANTS

my_email = 'ENTER YOUR OWN '
password = 'ENTER YOUR OWN app password'
#----------------------------Quotes file--------------------------------------#
with open('quotes.txt', mode= 'r') as file:
    quotes = file.read()
    quote = random.choice(quotes.splitlines())

    
#----------------------------Datetime---------------------------#
now = dt.datetime.now()
today = (now.weekday())


#------------------------------Email-------------------------------#
if today ==3:
   
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email,password=password)
        connection.sendmail(from_addr=my_email,to_addrs='ENTER EMAIL....',
                            msg= f"Subject: Tuesday Motivation Email \n\n {quote}")
else:
    print("nah, today not the day")




