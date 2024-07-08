from Classes import User
from Classes import Posts

Users=[]
def main():
    print("***Welcome to SocialWave: Post, Like and Connect***")
    is_registred=True if input("Do you have an exsiting account?(Y/N)")=="Y" else False
    if is_registred:
        user_email=input("Enter your email:")
        user_pass=input("Enter your password:")
        is_verified=login(user_email,user_pass)

    else:
        print("Create a new Acount:")
        user_name = input("Enter your name:")
        user_email= input("Enter your email:")
        user_pass=input("Enter your password:")
        user_city=input("Enter the city that you live in:")
        newUser=User(user_name,user_email,user_pass,user_city)
        Users.append(newUser)
        is_verified=True

def login(email,password):
    is_loggedin=False
    is_existed=False
    for user in Users:
        if user.email==email:
            is_existed=True
            if user.password==password:
                is_loggedin=True
                break
            else:
                c=0
                while user.password!=password and c<3:
                    password=input("invalid password! try again:")
                    c+=1
                if c>=3 or user.password!=password:
                    print("invalid credentials! Exiting...")
                    break
                else:
                    is_loggedin=True
                    break
    if not is_existed:
        print("Account not found!")
    return is_loggedin

main()