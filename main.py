# To run and test the code you need to update 4 places:
# 1. Change MY_EMAIL/MY_PASSWORD to your own details.
# 2. Go to your email provider and make it allow less secure apps.
# 3. Update the SMTP ADDRESS to match your email provider.
# 4. Update birthdays.csv to contain today's month and day.
# See the solution video in the 100 Days of Python Course for explainations.

import os
import datetime as dt
import random
import pandas
import smtplib

now = dt.datetime.now()
today = (now.month,now.day,)
birthday = pandas.read_csv("birthdays.csv")
day_extract=(birthday["day"])
month_extract= (birthday["month"])
bd_dictionary= {(row.month,row.day):(row.name,row.email,row.year,row.month,row.day) for
                index,row in birthday.iterrows()}
print(bd_dictionary)


if today in bd_dictionary :
 print(bd_dictionary[today])
else:
 print("dictionary")

user= (bd_dictionary[today])
name=(user[0])
email=(user[1])


letters=["letter_1.txt","letter_2.txt","letter_3.txt"]
random_letter=random.choice(letters)

with open (random_letter,"r") as file:
    txt = file.read()
    x=txt.replace("[NAME]",f"{name}")
    print(x)

my_email=""
password=""

with smtplib.SMTP("smtp.gmail.com") as connection:

    connection.starttls()
    connection.login(user=my_email,password=password)
    connection.sendmail(from_addr="dnew94125@gmail.com",to_addrs="dnew94125@gmail.com",msg=f"Subject:Happy birthday \n\n {x}")
    connection.close()
