*Written by Romeos CyberGypsy*
This script is specifically written for those who want to access their facebook accounts at the comfort of their terminal

Access and chat with Facebook friends at the comfort of your terminal
(C) Leusoft 2019
In case of any query, contact me at lewiswaigwa30@gmail.com
NOTE: To get a specific users ID, consider searching the target by username to display the ID
Usage: fb_chat.py [options]

Options:
  -h, --help            show this help message and exit
  --username=NAME       Facebook Username
  --password=PASSWORD   Facebook password
  -s USER, --search-for-user=USER
                        Search query. Search by name
  --search-for-group=GROUP
                        Search for a group by name
  -f                    Fetch info about all users you have chatted with
  -V TARGET_ID, --view-messages=TARGET_ID
                        View messages sent to the specified user. Enter the
                        targets ID
  -l LIMIT, --limit=LIMIT
                        Maximum number of messages to show. Defaults to 10
  -i ID, --id=ID        User to inbox or view messages
  -m MESSAGE, --message=MESSAGE
                        Message to send to user
  -I IMAGE, --image=IMAGE
                        Path to image file to send
  -v                    View my facebook ID
  --my-info             View my facebook info

  Example Usages:
  To search for a username on facebook, type as follows
    python fb_chat.py --username="facebook_username" --password="password" --search="target_username"

  To view messages sent between you and a specific user, type as follows
    python fb_chat.py --username="facebook_username" --password="password" --view-messages="target_id" --limit=<an integer>

  To send a message to a specific user by ID, type as follows
    python fb_chat.py --username="facebook_username" --password="password" --message="message" --id="target_id"

  To send an image file to a specific user by ID, type as follows
    python fb_chat.py --username="facebook_username" --password="password" --image="path to image" --id="target_id"

  To view your facebook ID, type as follows
    python fb_chat.py --username="facebook_username" --password="password" -v

  To fetch information about all users you've chatted with, type as follows
    python fb_chat.py --username="facebook_username" --password="password" -f

  To fetch your facebook information, type as follows
    python fb_chat.py --username="facebook_username" --password="password" --my-info

  To search for a facebook group by name, type as follows
    python fb_chat.py --username="facebook_username" --password="password" --search-for-group=group_id
    
