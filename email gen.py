import random
import string
import os
import smtplib
def email_gen(length):
        email = string.ascii_letters + string.digits #using the string module to create our email
        mail_gen = ''.join(random.choice(email) for _ in range(length)) #using .join we are putting items into this string 
        return mail_gen

def password_gen(length):
    password = string.ascii_letters + string.digits + string.hexdigits + '-'
    password_generator = ''.join(random.choice(password) for _ in range (length)) #same as before
    return password_generator 
while True:
    email_length = 10
    random_email = email_gen(email_length)
    format = '@fbi.ac'



    password_length = 15
    random_password = password_gen(password_length)
    print(random_email + format + ' ' +  random_password +'\n')


    with open('test.txt', 'a') as file:
        file.write(random_password + format + " " + random_password  )
    
        if os.path.exists('test.txt'):
            try:
                with open('test.txt', 'wb') as file:
                    file.write(random_password + format + " " + random_password  )
            except:
                pass  

    #def send_email():
       # my_email = random_email
       # password = random_password
        #connection = smtplib.SMTP("smtp.gmail.com")
        #connection.login(user=my_email, password=password)

       # connection.sendmail(from_addr= my_email,
                    #        to_addrs='lostatsea@fbi.ac')
#send_email()        



             
