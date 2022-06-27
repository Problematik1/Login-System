import os, time, string, random
with open('users/passwords.txt', 'r') as f:
    passwords = f.read().splitlines()

with open('users/usernames.txt', 'r') as f:
    usernames = f.read().splitlines()

def error():
    print('Invalid username or password!')
    time.sleep(1)
    os.system('exit')

def captcha():
    captc = ''.join(random.choices(string.ascii_lowercase + string.digits, k=3 ))
    captchatext = input(f'Captcha: {captc}\nEnter Captcha: ')
    if captchatext != captc:
        print('Invalid Captcha')
        time.sleep(1)
        os.system('exit')
    else: login()

def login():
    os.system('cls')
    username = input('Username: ')
    password = input('Password: ') 
    if password in passwords and username in usernames:
        prog()
    else: 
       return error()

def prog():
   print('Hello World!')

if __name__=='__main__':
    captcha()