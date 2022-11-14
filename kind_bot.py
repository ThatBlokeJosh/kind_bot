from instabot import Bot
import glob
import os
cookie_del = glob.glob("config/*cookie.json")
try:
    os.remove(cookie_del[0])
except:
    pass

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

def like_posts(username):
    bot.like_user(username, amount=10)
    
def comments():
    list_of_users = []
    with open(f"{your_username}.txt", "r") as comment_users:
        for line in comment_users.readlines():
            user = (line.rstrip())
            user_id = bot.get_user_id_from_username(user)
            media_id = bot.get_last_user_medias(user_id, count=1)
            bot.comment(media_id, "ILY <3 (tohle je jen bot (za chvili udelam nejakou API s komentarema na urovni))")
            
your_username = input("Enter your username: ")
your_password = input("Enter your password: ") 
    
bot.login(username=your_username, password=your_password)
    
try:
    with open(f"{your_username}.txt", "x") as just_creating:
        just_creating.close()
except:
    pass

while 0 == 0:
    start = input("l=like post of people in your list,\nv=view people in my list,\na=add people to my list,\nd=delete people from my list,\nm=send message,\nq=quit)\nc=comment posts\n: ").lower()

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
    
    elif start == "c":
        comments()
    
    else:
        print("Invalid input")
