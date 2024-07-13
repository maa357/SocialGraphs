from Classes import User
from Classes import Posts
from Classes import SocialGraph

Users=[]
def main():
    network=readGraphFromFile("Graph.txt")
    readUsersFile("users.txt",network)
    print("***Welcome to SocialWave: Post, Like and Connect***")
    logged_in=False
    while True:
        check,this_key=login()
        if check==True:
            logged_in=True
        else:
            try_again=input("Do you want to try again?(Y/N)")
            if try_again=="N":
                print("Exiting...")
                logged_in=False
                break
    if logged_in==True:
        this_user=User.user_dict[this_key]
        chioce=0
        while chioce!=8:
            getMneu()
            chioce=input("choose what do you want to do:")
            if chioce==1:
                while True:
                    c=0
                    this_user.getProfile()
                    c=input("1.return to menu\n2.edite profile")
                    if c==1:
                        break
                    else:
                        print("choose a number to edit:")
                        c=input("1.name\n2.email\n3.password\n4.city\5.career")
                        change=input("enter the new value:")
                        if c==1:
                            this_user.uppdateProfile("name",change)
                        elif c==2:
                            this_user.uppdateProfile("email",change)
                        elif c==3:
                            this_user.uppdateProfile("password",change)
                        elif c==4:
                            this_user.uppdateProfile("city",change)
                        elif c==5:
                            this_user.uppdateProfile("city",change)

            elif chioce==2:
                post=Posts(input("write your post here:"))
                this_user.addPost(post)
            elif chioce==3:
                pass
            elif chioce==4:
                pass
            elif chioce==5:
                pass
            elif chioce==6:
                pass
            elif chioce==7:
                pass
    print("Search for a user:")
    print(network.bfs(" arsal", "city"))
    for user in network.mergeSortBy(network.getAll(),"name"):
        print(user.name)
    print(network.adj_matrix)
    #writeGraphOnFile(network,"Graph.txt")


def checkPass(email,password):
    is_loggedin=False
    is_existed=False
    for user in Users:
        if user.email==email:
            is_existed=True
            if user.password==password:
                is_loggedin=True
                key=user.mykey
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
                    key=user.mykey
                    break
    if not is_existed:
        print("Account not found!")
    return is_loggedin,key

def readUsersFile(file_path,network):
    with open(file_path, 'r') as file:
        for line in file:
            user_info = line.split(',')
            for word in user_info:
                word=word.strip()
            if len(user_info) == 5:
                name, email, password, city, career = user_info
                new_user = User(name, email, password, city, career, network)

def writeGraphOnFile(network, file_path):
    with open(file_path, 'w') as file:
        for row in network.adj_matrix:
            row_str = ','.join(map(str, row))
            file.write(row_str + '\n')
def clearFileContent(file_path):
    with open(file_path, 'w') as file:
        pass
def readGraphFromFile(file_path):
    matrix = []
    with open(file_path, 'r') as file:
        for line in file:
            row = list(line.strip().split(','))
            matrix.append(row)
    return SocialGraph.convertMatrixToGraph(matrix)

def getMneu():
    print("Welcome again,")
    print("\t1.View profile\n\t2.post something\n\t3.Suggest a new friend\n\t4.View all users\t\n5.View Statistics about network\t\n6.Search for a user\t\n7.Delete my account\t\n8.Exit")

def login():
    is_registred=True if input("Do you have an exsiting account?(Y/N)")=="Y" else False
    if is_registred:
        user_email=input("Enter your email:")
        user_pass=input("Enter your password:")
        is_verified=checkPass(user_email,user_pass)


    else:
        print("Create a new Acount:")
        user_name = input("Enter your name:")
        user_email= input("Enter your email:")
        user_pass=input("Enter your password:")
        user_city=input("Enter the city that you live in:")
        user_career=input("Enter your career:")
        newUser=User(user_name,user_email,user_pass,user_city,user_career,network)
        newUser.addToGraph()
        is_verified=True
    return is_verified
main()