from Classes import User
from Classes import Posts
from Classes import SocialGraph

Users=[]
def main():
    network=SocialGraph(0)
    readUsersFile("users.txt",network)
    print("***Welcome to SocialWave: Post, Like and Connect***")
    # is_registred=True if input("Do you have an exsiting account?(Y/N)")=="Y" else False
    # if is_registred:
    #     user_email=input("Enter your email:")
    #     user_pass=input("Enter your password:")
    #     is_verified=login(user_email,user_pass)


    # else:
    #     print("Create a new Acount:")
    #     user_name = input("Enter your name:")
    #     user_email= input("Enter your email:")
    #     user_pass=input("Enter your password:")
    #     user_city=input("Enter the city that you live in:")
    #     user_career=input("Enter your career:")
    #     newUser=User(user_name,user_email,user_pass,user_city,user_career,network)
    #     Users.append(newUser)
    #     is_verified=True
    print("Search for a user:")
    print(network.bfs(" arsal", "city"))
    for user in network.mergeSortBy(network.getAll(),"name"):
        print(user.name)


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

def readUsersFile(file_path,network):
    with open(file_path, 'r') as file:
        for line in file:
            user_info = line.split(',')
            for word in user_info:
                word=word.strip()
            if len(user_info) == 5:
                name, email, password, city, career = user_info
                new_user = User(name, email, password, city, career, network)
main()