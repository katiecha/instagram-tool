import json
with open('followers_1.json') as file:
    followers_json = json.load(file)

with open('following.json') as file:
    following_json = json.load(file)

following_list = []
for following in following_json["relationships_following"]:
    following_list.append(following["string_list_data"][0]["value"])

for follower in followers_json:
    if follower["string_list_data"][0]["value"] in following_list:
        following_list.remove(follower["string_list_data"][0]["value"])

following_list = sorted(following_list)

for username in following_list:
    print(username)