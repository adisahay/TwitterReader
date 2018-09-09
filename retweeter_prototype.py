import twitter, csv

inputFile = "input_tweetIds.csv"
outputFile = "locations.csv"

# Twitter developer credentials
consumer_key = "",
consumer_secret = "",
access_token_key = "",
access_token_secret = ""

with open("input_twitter_api_credentials.csv") as credfile:
    # Read only the second row and ignore the rest
    credentials = list(csv.reader(credfile, delimiter=","))[1:2][0]
    consumer_key = credentials[0]
    consumer_secret = credentials[1]
    access_token_key = credentials[2]
    access_token_secret = credentials[3]

api = twitter.Api(consumer_key="".join(consumer_key),
                consumer_secret="".join(consumer_secret),
                access_token_key="".join(access_token_key),
                access_token_secret="".join(access_token_secret))

# Fetch a list of tweet ids and run the 'getRetweeters' for each of them
# TBD: The list can be fetched from a file or by waiting for live tweets
tweetIdList = []
with open(inputFile, "r") as inputCSV:
    tweets = list(csv.reader(inputCSV, delimiter=","))[1:]
    tweets = [int(tweet[0]) for tweet in tweets]
    tweetIdList = tweets

statuses = api.GetStatuses(tweetIdList, include_entities=False, map=True)

with open(outputFile, "w") as outputCSV:
    writer = csv.writer(outputCSV)
    # Prepare heading row
    writer.writerow(["Handles", "Tweet IDs", "Retweeter Handles", "Locations"])
    found = 0
    totalCount = 0
    for tweetId in tweetIdList:
        # Error handling for invalid IDs
        if statuses[tweetId] == None:
            continue

        print ("Fetching retweeters for Tweet ID: " + str(tweetId))
        # Fetch the retweeters for this tweet
        retweeters = api.GetRetweeters(tweetId)

        print ("Getting retweeters location to CSV file: " + outputFile)
        count = 1
        for user in list(retweeters):
            user_info = api.GetUser(user)
            # Filter out empty location values
            if user_info.location != "":
                writer.writerow([statuses[tweetId].AsDict()["user"]["screen_name"], tweetId, user_info.screen_name, user_info.location])
                found += 1

            # Update the percentage progress
            print("\r" + str(count * 100 // len(retweeters)) + "% Completed", end="", flush=True)
            count += 1
        totalCount += (len(retweeters))
        print ()

print ("\nFinished writing to CSV file.")
print ("Total number of retweeters: " + str(totalCount))
print ("Total number of locations found: " + str(found))
