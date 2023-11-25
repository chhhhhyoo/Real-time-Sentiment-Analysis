import json

with open('../../data/raw/tweet_data.json', 'r') as file:
    data = [json.loads(line) for line in file]

users_data = {}
for item in data:
    username = item['username']
    score = item['followers_count'] + item['retweet_count']
    if username in users_data:
        users_data[username] += score
    else:
        users_data[username] = score

sorted_users = sorted(users_data.items(), key=lambda x: x[1], reverse=True)

for user, score in sorted_users[:10]:
    print(f"{user} - Score: {score}")
