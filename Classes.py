from datetime import date


class User:
    key = -1
    user_dict = {}
    def __init__(self, name, email, password, city,career,network, friends=0, posts=[]):
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

    
    def addToGraph(self):
        SocialGraph.addVertex(self.network)
        for key in range(len(self.network.adj_matrix)):
            if key !=self.key:
                if self.city==self.user_dict[key].city and self.career==self.user_dict[key].career:
                    SocialGraph.addEdge(self.network,self.mykey,key,-3)
                elif self.career==self.user_dict[key].career:
                    SocialGraph.addEdge(self.network,self.mykey,key,-2)
                elif self.career==self.user_dict[key].career:
                    SocialGraph.addEdge(self.network,self.mykey,key,-1)
                

    def deleteUser(self):
        User.key-=1
        del User.user_dict[self.mykey]
        SocialGraph.deleteVertex(self.mykey)
        del self

    def getFriends(self):
        friends_lst=[0]*self.friends
        print("***"+self.name+"'s friends\n"+"***")
        if self.friends ==0:
            print("No friends Found!")
        else:
            i=1
            for node in len(self.network.adj_matrix[self]):
                edge_value=self.network.adj_matrix[self][node]
                if edge_value is int and edge_value>=0:
                    friends_lst[i-1]=node
                    print(i+". "+self.user_dict[node].name+"\n")
                    i+=1
        return friends_lst
    
    def getPosts(self):
        print("***"+self.name+"'s posts\n"+"***")
        if self.posts ==[]:
            print("No posts Found!")
        else:
            i=1
            for post in self.posts:
                print("______________")
                print(i+".\n",post.content,"\n","likes:"+len(post.likes)+"\n",post.date)

    def addFriend(self,new_friend):
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
        for node in range(len(self.network.adj_matrix)):
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
        edge_value=self.network.adj_matrix[self.mykey][afriend.mykey]
        if edge_value==0:
            self.network.addEdge(self.mykey,afriend.mykey,'x')
        elif edge_value>0:
            self.network.addEdge(self.mykey,afriend,edge_value*-1)
        
    def addPost(self,new_post):
        self.posts.insert(0,new_post)

    def getProfile(self):
        print(self.name)
        print(self.city,"|",self.career)
        print("______________")
        friends_lst=self.getFriends()
        self.getPosts()
    def uppdateProfile(self,attribute,change):
        if hasattr(self, attribute):
            setattr(self, attribute, change)
        else:
            raise AttributeError(f"User object has no attribute '{attribute}'")

class Posts:
    def __init__(self,content,likes=[],date=date.today()):
        self.content = content
        self.date=date
        self.likes=likes
    def addLike(self):
        self.likes+=1

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
    
    def deleteVertex(self,index):
        if 0 <= index < self.num_users:
            for i in self.num_users:
                self.adj_matrix[index][i],self.adj_matrix[self.num_users-1][i]=self.adj_matrix[self.num_users-1][i], self.adj_matrix[index][i]
            for i in self.num_users:
                self.adj_matrix[i][index],self.adj_matrix[i][self.num_users-1]=self.adj_matrix[i][self.num_users-1], self.adj_matrix[i][index]
            self.adj_matrix.pop()
            self.num_users-=1
            for i in self.num_users:
                self.adj_matrix[i].pop()

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

    def bfs(self,target,attribute,start_index=0):
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
        for i in range(len(self.adj_matrix)):
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

    def mergeSortBy(self,lst, attribute):
        if len(lst) <= 1:
            return lst
        mid = len(lst) // 2
        left = SocialGraph.mergeSortBy(self,lst[:mid], attribute)
        right = SocialGraph.mergeSortBy(self,lst[mid:], attribute)
        return SocialGraph.merge(left, right, attribute)
    
    def convertMatrixToGraph(matrix):
        Graph=SocialGraph(0)
        Graph.adj_matrix=[row[:] for row in matrix]
        return Graph
    def suggestFriend(self,user:User):
        not_friend = []
        for node in range(len(self.adj_matrix)):
            edge_weight=self.adj_matrix[node][user.key]
            if edge_weight is int and edge_weight < 0:
                not_friend.append(edge_weight,node)
        
        not_friend.sort(key=lambda x: x[0])

        return not_friend
