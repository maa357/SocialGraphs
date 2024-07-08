class User:
    key = -1
    def __init__(self, name, email, password, friends, posts, city):
        self.name=name
        self.email=email
        self.friends= []
        self.posts=[]
        self.city=city
        self.password=password
        User.key+=1
        self.mykey= User.key
    def getFriends(self):
        print("***"+self.name+"'s friends\n"+"***")
        i=1
        for user in self.friends:
            print(i+". "+user.name+"\n")
            i+=1
    def getPosts(self):
        print("***"+self.name+"'s posts\n"+"***")
        for post in self.posts:
            print("______________")
            print(post.date+":\n",post.content,"\n",post.likes)

    def addFriend(self,new_friend):
        if new_friend not in self.friends:
            self.friends.append(new_friend)
            new_friend.friends.append(self)
    def removeFriend(self,afriend):
        if afriend in self.friends:
            self.friends.reomve(afriend)
            afriend.friends.remove(self)
    def addPost(self,new_post):
        self.posts.insert(0,new_post)

        

