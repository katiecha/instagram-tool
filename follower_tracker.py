import json
with open('followers_and_following/followers_1.json') as file:
    followers_json = json.load(file)

with open('followers_and_following/following.json') as file:
    following_json = json.load(file)

following_list = []
for following in following_json["relationships_following"]:
    following_list.append(following["title"])

for follower in followers_json:
    if follower["string_list_data"][0]["value"] in following_list:
        following_list.remove(follower["string_list_data"][0]["value"])

following_list = sorted(following_list)

print("=" * 60)
print("Instagram Follower Tracker".center(60))
print("=" * 60)
print(f"\nTotal followers: {len(followers_json)}")
print(f"Total following: {len(following_json['relationships_following'])}")
print(f"Accounts not following you back: {len(following_list)}")
print("\n" + "-" * 60)
print("Users you follow who don't follow you back:")
print("-" * 60)

for i, username in enumerate(following_list, 1):
    print(f"{i:3d}. {username}")