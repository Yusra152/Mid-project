import re
email=input("enter your email:")
location=input("enter your location:")
if "@" in email:
    print("valid")
    username,domain=email.split("@")
    print("username:",username)
    print("domain:",domain)
else:
    print("invalid")
    print("location:",location)