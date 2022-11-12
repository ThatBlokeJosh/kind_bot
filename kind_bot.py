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

def remove_following():
    list_of_users = []
    checkpoint = 0
    with open(f"{your_username}.txt", "r") as mby_nothing_to_remove:
        if mby_nothing_to_remove.readlines() == []:
            print("Your list is empty")
        else:
            with open(f"{your_username}.txt", "r") as remove_users:
                for line in remove_users.readlines():
                    user = (line.rstrip())
                    list_of_users.append(user)
                    
                while checkpoint == 0:
                    print(list_of_users)
                    with open(f"{your_username}.txt", "r") as remove_users:
                        guy_i_follow = input("Enter the username you want to delete: ")
                        text = remove_users.read()
                        list = []        
                        for line in text.splitlines():
                            list.append(line)
                            
                        if guy_i_follow in list_of_users:
                            list.remove(guy_i_follow)
                            with open(f"{your_username}.txt", "w") as remove_users:
                                for line in list:
                                    remove_users.write(line + "\n")

                                print("Username was removed")
                                checkpoint = 1
                        else:
                            print("Username not found")
                            break
                                   
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
    start = input("What would you like to do? \n(l=like post of people in your list,\nv=view people in my list,\na=add people to my list,\nd=delete people from my list,\nm=send message,\nq=quit)\n: ").lower()

    if start == "q":
        print("See ya later")
        break
    
    elif start == "r":
        print("Running")
        
    elif start == "v":
        print(list_of_following())
        
    elif start == "a":
        add_people_you_like()
    
    elif start == "d":
        remove_following()
    
    else:
        print("Invalid input")
