from datetime import date


class User:
    key = -1
    user_dict = {}
    def __init__(self, name, email, password, city,career,network, friends=[], posts=[]):
        self.name=name
        self.email=email
        self.friends=friends
        self.posts=posts
        self.city=city
        self.password=password
        self.network=network
        self.career=career
        User.key+=1
        self.mykey= User.key  
        User.user_dict[self.mykey]=self
        SocialGraph.addVertex(self.network)
        for key in len(self.network.adj_matrix):
            if key !=self.key:
                if self.city==self.user_dict[key].city:
                    SocialGraph.addEdge(self.network,self.mykey,key,-1)
                if self.career==self.user_dict[key].career:
                    SocialGraph.addEdge(self.network,self.mykey,key,-2)
    
    def deleteUser(self):
        User.key-=1
        del User.user_dict[self.mykey]
        SocialGraph.deleteVertix(self.mykey)
        del self


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
        edge_value=self.network.adj_matrix[self.mykey][new_friend.mykey]
        if type(edge_value) is int and edge_value<0:
            self.network.addEdge(self.mykey,new_friend.mykey,edge_value*-1)
            print("Friend added")
        elif type(edge_value) is not int:
            self.network.addEdge(self.mykey,new_friend.mykey,0)
            print("Friend added")
        else:
            print("Already Friends")
        #adding edges for common friends
        for node in len(self.network.adj_matrix):
            if node!=self.mykey:
                check_friendship=self.network.adj_matrix[new_friend.mykey][node]
                if check_friendship is int and check_friendship>=0:
                    edge_value=self.network.adj_matrix[self.mykey][node]
                    if edge_value is int and edge_value>=0:
                        self.network.addEdge(self.mykey,node,edge_value+1)
                    elif edge_value is int and edge_value<0:
                        self.network.addEdge(self.mykey,node,edge_value-1)
                    else:
                        self.network.addEdge(self.mykey,node,-1)


    def removeFriend(self,afriend):
        if afriend in self.friends:
            self.friends.reomve(afriend)
            afriend.friends.remove(self)
        edge_value=self.network.adj_matrix[self.mykey][afriend.mykey]
        if edge_value==0:
            self.network.addEdge(self.mykey,afriend.mykey,'x')
        elif edge_value>0:
            self.network.addEdge(self.mykey,afriend,edge_value*-1)
        
    def addPost(self,new_post):
        self.posts.insert(0,new_post)

class Posts:
    def __init__(self,content,likes=[],date=date.today()):
        self.content = content
        self.date=date
        self.likes=likes

class SocialGraph:
    def __init__(self, num_users):
        self.num_users = num_users
        self.adj_matrix = [['x'] * num_users for _ in range(num_users)]

    def addVertex(self):
        # O(N), N being the number of vertices => O(V)
        self.num_users += 1
        for row in self.adj_matrix:
            row.append('x')
        self.adj_matrix.append(['x'] * self.num_users)
        print("Added user", self.num_users - 1, "\n")
    
    def addEdge(self, user_key1, user_key2, weight):
    # O(1)
        if 0 <= user_key1 < self.num_users and 0 <= user_key2 < self.num_users:
            # To ensure that both user_key1 and user_key2 exist
            self.adj_matrix[user_key1][user_key2] = weight
            self.adj_matrix[user_key2][user_key1] = weight
            print("Added and edge between", user_key1, "and", user_key2, "\n")
        elif ((user_key1 < 0 or user_key1 >= self.num_users)
            and (user_key2 < 0 or user_key2 >= self.num_users)):
            print("Invalid users", user_key1, "and", user_key2, "\n")
        elif (user_key1 < 0 or user_key1 >= self.num_users):
            print("Invalid user", user_key1, "\n")
        else:
            print("Invalid user", user_key2, "\n")

    def bfs(self,target,attribute):
        start_index = 0
        visited = [False] * len(self.adj_matrix)
        queue = [start_index]
        result=[]

        while queue:
            node = queue.pop(0)  # Pop the first element
            if not visited[node]:
                visited[node] = True
                if getattr(User.user_dict[node], attribute) == target:
                    result.append(node)
            
                for i, edge in enumerate(self.adj_matrix[node]):
                    if edge=='x':
                        connected=False
                    else:
                        connected=True
                    if connected and not visited[i]:
                        queue.append(i)
        
        return result
    def getAll(self):
        users=[0]*len(self.adj_matrix)
        for i in len(self.adj_matrix):
            users[i]=User.user_dict[i]
        return users
    
    def merge(left, right, attribute):
        merged = []
        i = j = 0
        while i < len(left) and j < len(right):
            if getattr(left[i], attribute) <= getattr(right[j], attribute):
                merged.append(left[i])
                i += 1
            else:
                merged.append(right[j])
                j += 1
        while i < len(left):
            merged.append(left[i])
            i += 1
        while j < len(right):
            merged.append(right[j])
            j += 1
        return merged

    def mergeSortBy(lst, attribute):
        if len(lst) <= 1:
            return lst
        mid = len(lst) // 2
        left = SocialGraph.mergeSort(lst[:mid], attribute)
        right = SocialGraph.mergeSort(lst[mid:], attribute)
        return SocialGraph.merge(left, right, attribute)

