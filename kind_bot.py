from instabot import Bot

bot = Bot()

x = 0

def add_people_you_like():
    with open(f"{your_username}.txt", "a") as txt_of_liked_people:
        while 0 == 0:
            add_following_account = input("Enter username of the account you want to add: ")
            if add_following_account == "q":
                break
            elif add_following_account in list_of_following():
                print("Account already exists. Press q to quit")
            else:
                txt_of_liked_people.write(add_following_account + "\n")
                print("Account has been added. Press q to quit")
            
def list_of_following():
    list_of_people_i_follow = []
    with open(f"{your_username}.txt", "r") as txt_of_following:
        for line in txt_of_following.readlines():
            guy_i_follow = (line.rstrip())
            list_of_people_i_follow.append(guy_i_follow)
    return list_of_people_i_follow

try:
    your_username = input("Enter your username: ")
    your_password = input("Enter your password: ") 
    #bot.login(username=your_username, password=your_password)
except:
    print("Username or password are not valid!")
    
try:
    with open(f"{your_username}.txt", "x") as just_creating:
        just_creating.close()
except:
    pass

while 0 == 0:
    start = input("What would you like to do? \n(r=run the script\nv=view people in my list,\na=add people to my list,\nd=delete people from my list,\nq=quit)\n: ").lower()

    if start == "q":
        print("See ya later")
        break
    
    while start == "r":
        print("Running")
        break
        
    while start == "v":
        print(list_of_following())
        break
        
    while start == "a":
        add_people_you_like()
        break
    
    while start == "d":
        print("Uhm deleting...")
        break