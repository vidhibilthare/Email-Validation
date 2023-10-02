# a-z wscubetech
# 0-9
# @( one time)
# . _ (one time)
# . (before 2-3 charactor)
import re
email_condition="^[a-z]+[\._]?[a-z 0-9]+[@]\w+[.]\w{2,3}$"
user_email=input("enter your email:-")

if re.search(email_condition,user_email):
    print("Right Email...")
else:
    print("there is mistake...")