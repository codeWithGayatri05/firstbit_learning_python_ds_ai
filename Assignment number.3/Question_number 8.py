import random
name='gayatrijadhav'
passwrd='05042005'
userid=input("Enter userid :")
password=input("Enter password :")
if(name==userid and passwrd==password):
    captcha=random.randint(2343,6666)
    print("Captcha :",captcha)
    captcha_user=int(input("Enter captcha :"))
    if(captcha_user==captcha):
        print("Login successfully !!")
    else:
        print("Invalid Captcha .")
else:
    print("Invalid userid and password .")