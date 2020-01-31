#Interact with your facebook account without using facebook app
#at the comfort of your terminal

'''
Name: facebook_API
Author: Romeos CyberGypsy
Email: lewiswaigwa30@gmail.com
Telegram: https://t.me/Romeos_CyberGypsy
Version: 1.1
(C) Leusoft
'''

from fbchat import Client
from fbchat.models import *
import optparse
from termcolor import colored
import os
import sys


class Engine:
    #initializing out constructor
    def __init__(self):
        print(colored(" _   _","blue"))
        print(colored("|_  | )","blue","on_green"))
        print(colored("|   |_)  CHAT APP FOR TERMINAL","blue","on_green"))
        print(" ")
        print(colored("[+] Written by Romeos CyberGypsy"))
        print(colored("Access and chat with Facebook friends at the comfort of your terminal","yellow"))
        print(colored("(C) Leusoft 2019","green"))
        print("In case of any query, contact me at:")
        print(colored("1. Email: lewiswaigwa30@gmail.com \n2. Telegram: https://t.me/Romeos_CyberGypsy \n3. Facebook: Romeos CyberGypsy","blue"))
        print(" ")
        print(colored("NOTE: To get a specific users ID, consider searching the target by username first to display the ID","red"))
        print(" ")
        self.parser = optparse.OptionParser()
        self.parser.add_option("--username", dest = "name", help = "Facebook Username")
        self.parser.add_option("--password", dest = "password", help = "Facebook password")
        self.parser.add_option("-s", "--search-for-user", dest = "user", help = "Search query. Search by name")
        self.parser.add_option("--search-for-group", dest = "group", help = "Search for a group by name")
        self.parser.add_option("-f", action = "store_true", dest = "", help = "Fetch info about all users you have chatted with")
        self.parser.add_option("-V","--view-messages", dest ="target_id", help = "View messages sent to the specified user. Enter the targets ID")
        self.parser.add_option("-l","--limit", dest = "limit", help = "Maximum number of messages to show. Defaults to 10")
        self.parser.add_option("-i", "--id", dest = "id", help = "User to inbox or view messages")
        self.parser.add_option("-m","--message", dest = "message", help = "Message to send to user")
        self.parser.add_option("-I","--image", dest = "image", help = "Path to image file to send")
        self.parser.add_option("-v", action = "store_true", help = "View my facebook ID")
        self.parser.add_option("--my-info", action = "store_true", help = "View my facebook info")
        #parse the values of the arguments provided
        (self.values, self.keys) = self.parser.parse_args()

        try:
            #logging in to your facebook account
            self.client = Client(self.values.name, self.values.password)


        except KeyboardInterrupt:
            #handle the keyboard KeyboardInterrupt error
            print(colored("[-] Exiting safely","red"))

        except Exception as e:
            #print out any other Exception that may arise
            print(e)
            sys.exit()

        if sys.argv[3] == "-i" or "--id" in sys.argv[3] or sys.argv[3] == "-m" or "--message" in sys.argv[3]:
            self.send_message(self.values.id, self.values.message)

        elif sys.argv[3] == "-s" or "--search-for-user" in sys.argv[3]:
            self.search_user(self.values.user)

        elif sys.argv[3] == "-V" or "--view-messages" in sys.argv[3]:
            self.view_messages(self.values.target_id, self.values.limit)

        elif sys.argv[3] == "-I" or "--image" in sys.argv[3]:
            self.send_image(self.values.image, self.values.id)

        elif sys.argv[3] == "-v":
            self.my_id()

        elif  sys.argv[3] == "-f":
            self.fetch_users()

        elif "--search-for-group" in sys.argv[3]:
            self.search_for_group(self.values.group)

        elif sys.argv[3] == "--my-info":
            self.myinfo()

        else:
            sys.exit()



    def send_message(self, user, message):
        #Code to send messages
        self.client.send(Message(text = message), thread_id = user, thread_type = ThreadType.USER)
        print(colored("[+] Message sent...","green"))

        sys.exit()



    def search_user(self, username):
        #code to search for username on facebook
        #one name is enough for the search
        users = self.client.searchForUsers(username)
        x = 1
        print(colored("SEARCH RESULTS:","red","on_green"))
        for user in users:
            print(colored("User {}" .format(str(x)),"blue"))
            x=x+1
            name = colored(user.name,"green")
            id = colored(user.uid,"greenpyt")
            photo = colored(user.photo,"green")
            url = colored(user.url,"green")
            friendship = colored(user.is_friend,"green")
            print("Name: {}" .format(name))
            print("User ID: {}" .format(id))
            print("Photo url: {}" .format(photo))
            print("Profile url: {}" .format(url))
            print("Friend: {}" .format(friendship))
            print("-"*10)



    def view_messages(self, user, limit):
        #code to view messages between you and the specified users
        if limit == None:
            limit = "10"

        print(colored("[+] Reading messages...","blue"))
        messages = self.client.fetchThreadMessages(thread_id = user, limit = int(limit))
        #The messages arrive in a reversed order
        #so lets reverse them again
        messages.reverse()
        for message in messages:
            print(message.text)

    def send_image(self, path, userid):
        #sends an image stored in your local machine
        #a path can be e.g c:\\Images\\image.jpg
        self.client.sendLocalImage(path, message = Message(text = "Image"), thread_id = userid, thread_type = ThreadType.USER)
        print(colored("[+] Image sent successfully","green"))

    def my_id(self):
        #prints your facebook ID
        print(colored("Your Facebook ID is {}" .format(self.client.uid),"blue"))

    def fetch_users(self):
        #fetch info about users that you've chatted with recently

        users = self.client.fetchAllUsers()
        print(colored("[+] Fetching users information","green"))
        x = 1
        print(users)
        for user in users:
            print("User {}" .format(str(x)))
            print("Username: {}" .format(user.name))
            print("User ID: {}" .format(user.uid))
            print("User profile url: {}" .format(user.url))
            print("*"*10)
            x+=1

    def myinfo(self):
        print(colored("[+] My info","blue"))
        name = colored(self.values.name, "green")
        id = colored(self.client.uid,"green")
        phone = colored(self.client.getPhoneNumbers(),"green")
        logged = colored(self.client.isLoggedIn(),"green")
        print("Name: {}" .format(name))
        print("ID: {}" .format(id))
        print("Phone numbers: {}" .format(phone))
        print("Logged in: {}" .format(logged))

    def search_for_group(self, name):
        groups = self.client.searchForGroups(name)
        x = 1
        for group in groups:
            print(colored("Group {}" .format(str(x)),"blue"))
            print("Name: {}" .format(group.name))
            print("ID: {}" .format(group.uid))
            print("Group URL: {}" .format(group.url))
            print("-"*10)


if __name__ == '__main__':
    #start the facebook engine by creating an instance of class engine
    #runs the constructor by default
    obj = Engine()
