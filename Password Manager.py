from cryptography.fernet import Fernet
import os

print("----------Welcome to the Password Manager----------")
print()


# fucntion to generate a unique common key for encryption process
def write_key():
    key = Fernet.generate_key()
    # wb - write byte mode
    with open ("key.key" , "wb") as key_file:
        key_file.write(key)

#function to get the generated key
def load_key():
    # rb - read byte mode
    file = open("key.key","rb")
    key = file.read()
    file.close()
    return key

if not os.path.exists("key.key"):
    write_key()

key = load_key()
# complete key
fer = Fernet(key)


def add():
    username = input("Account name / Username : ")
    pwd = input("Password : ")

    with open ("Passwords.txt","a") as file_pwd:
        # encrypt the password and make it a byte string when saving into the file
        file_pwd.write(username + " ----> " + fer.encrypt(pwd.encode()).decode() +  "\n")
        print()

def view():
     with open ("Passwords.txt","r") as file_pwd:
        for line in file_pwd.readlines():
            data = line.rstrip()
            user , passw = data.split(" ----> ")
            # decrypt the password and make byte stream to a string when loading from the file
            print("Username : ", user , " -----> Password : " , fer.decrypt(passw.encode()).decode())
            print()

while True:
    option = input("Would you like to add a new password or view existing ones ? (add,view) press 'q' to quit : ").lower()
    print()
    if option == "q":
        break

    elif option == "add":
        add()
    elif option == "view":
        if os.path.exists("Passwords.txt"):
            view()
        else:
            print("You have not added any passwords")
    else:
        print("Invalid Option")
        continue