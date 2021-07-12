#!/usr/bin/env python3

import instaloader
import getpass

inst = instaloader.Instaloader()

username = input("Username: ")
password = getpass.getpass()

try:
    inst.login(username, password)
except instaloader.exceptions.BadCredentialsException:
    print("Invalid login")
    exit(1)

profile = instaloader.Profile.from_username(inst.context, username)

followers = []
following = []

for user in profile.get_followers():
    followers.append(user.username)
for user in profile.get_followees():
    following.append(user.username)

dont_follow_you_back = []
you_dont_follow_back = []

for username in following:
    if username not in followers:
        dont_follow_you_back.append(username)

for username in followers:
    if username not in following:
        you_dont_follow_back.append(username)


if len(dont_follow_you_back):
    print("------------ People that don't follow you back ({}) ------------".format(len(dont_follow_you_back)))
    for username in dont_follow_you_back:
        print(username)
        
if len(you_dont_follow_back):
    print("------------ People that you don't follow back ({}) ------------".format(len(you_dont_follow_back)))
    for username in you_dont_follow_back:
        print(username)
