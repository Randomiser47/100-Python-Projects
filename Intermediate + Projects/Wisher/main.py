##################### Extra Hard Starting Project ######################
import smtplib
import pandas
import datetime as dt
import random
#Constants
MY_EMAIL = 'ENTER YOUR OWN '
MY_PASSWORD = 'ENTER YOUR OWN app password'

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv
data = pandas.read_csv('birthdays.csv')
now = dt.datetime.now()
month = now.month
year = now.year
day = now.day
matching_rows = data[(data['month'] == month) & (data['day'] == day)]
emails = matching_rows['email'].to_string(index=False)
names = matching_rows['name'].to_string(index=False)

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
list_letters = ['letter_1.txt','letter_2.txt','letter_3.txt']
with open(f"letter_templates/{random.choice(list_letters)}") as file:
    read_File = file.read()
    letter =  read_File.replace("[NAME]",names)
    
# 4. Send the letter generated in step 3 to that person's email address.
with smtplib.SMTP('smtp.gmail.com') as connection:
    connection.starttls()
    connection.login(user=MY_EMAIL,password=MY_PASSWORD)
    connection.sendmail(from_addr=MY_EMAIL,
                        to_addrs=emails,
                        msg=f"Subject:Test\n\n{letter}")