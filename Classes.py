from datetime import date


class User:
    key = -1
    def __init__(self, name, email, password, city, friends=[], posts=[]):
        self.name=name
        self.email=email
        self.friends=friends
        self.posts=posts
        self.city=city
        self.password=password
        User.key+=1
        self.mykey= User.key
    def getFriends(self):
        print("***"+self.name+"'s friends\n"+"***")
        if self.friends ==[]:
            print("No friends Found!")
        else:
            i=1
            for user in self.friends:
                print(i+". "+user.name+"\n")
                i+=1
    def getPosts(self):
        print("***"+self.name+"'s posts\n"+"***")
        if self.posts ==[]:
            print("No posts Found!")
        else:
            for post in self.posts:
                print("______________")
                print(post.date+":\n",post.content,"\n",len(post.likes))

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

class Posts:
    def __init__(self,content,likes=[],date=date.today()):
        self.content = content
        self.date=date
        self.likes=likes

class SocialGraph:
    def __init__(self, num_vertices):
        self.num_vertices = num_vertices
        self.adj_matrix = [[0] * num_vertices for _ in range(num_vertices)]

    def addVertex(self):
        # O(N), N being the number of vertices => O(V)
        self.num_vertices += 1
        for row in self.adj_matrix:
            row.append(0)
        self.adj_matrix.append([0] * self.num_vertices)
        print("Added vertex", self.num_vertices - 1, "\n")
