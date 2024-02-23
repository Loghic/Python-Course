class User:

    def __init__(self, user_id, username):
        self.id = user_id
        self.username = username
        self.followers = 0 #If its not needed to be provided at decleration
        self.following = 0
        # print("new user being created...")

    def follow(self, user): #self follows user
        """Gives a follow to specified user"""
        user.followers += 1
        self.following += 1

""" 
#possible to add attributes like this
user_1 = User()
user_1.id = "001"
user_1.username = "angela"
print(user_1.username)
"""

user_1 = User("001", "Angela")
user_2 = User("002", "Jack")
print(user_1.username)
print(user_1.followers)
user_1.follow(user_2)
print(user_1.followers)
print(user_2.followers)
