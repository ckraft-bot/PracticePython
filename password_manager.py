# encrypt paswwords
from cryptography.fernet import Fernet # pip install cryptography

"""
key + master password + text to encrypt = random text
random text + key + master password = text to encrypyt

def function_name(parameter, parameter)
"""

def write_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file: # wr = write bytes
        key_file.write(key)

def load_key():
    file = open("key.key", "rb") # rb = read bytes
    key = file.read()
    file.close()
    return key

master_pwd = input("The master pasword is: ")
key = load_key() + master_pwd.encode()
fer = Fernet(key)

def view():
    # open and read the file
    with open('passwords.txt', 'r') as f:
        for line in f.readlines():
            data = line.rstrip() # rstrip strips the carriage return (extra spaces and new lines)
            user, pwd = data.split("|") # "|" is called "pipe operator"
            print("User:", user, "| Password:",
                # open decrypted
                fer.decrypt(pwd.encode()).decode())

def add():
    # get user's account name and password
    name = input("Account Name: ")
    pwd = input("Password: ")
    
    # create file if it does not exit  or open a text file and append the name and password into that text file
    with open('passwords.txt', 'a') as f:
        # seperate the name and password inputs, read encrypted
        f.write(name + "|" + fer.encrypt(pwd.encode()).decode() + "\n")

while True:
    mode = input("Do you want to add a new password or view existing ones(view/add), press q to quit ?")
    if mode == "q":
        break 
    
    if mode == "view":
        view()
    elif mode == "add":
        add()
    else:
        print("Invalid mode.")
        continue
