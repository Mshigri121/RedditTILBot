import requests
import json
import time

# url = f"https://www.reddit.com/r/todayilearned/new/.json"
# til = requests.get(url, headers={'User-agent': 'm0'}).json()
# fact = til["data"]["children"][0]["data"]["title"]
# source = til["data"]["children"][0]["data"]["url"]

txtlist = open("TIL List.txt","a+") #This command will create a text file that will be copy the printed fact into the file. Each new fact will subsequently be added on the line under the previous one.

# check = fact[4].isalpha()
# print(check)
# print(source)
# print(fact)
# print(fact[4:])
# if fact[0:3] == "TIL":
#     print("It works wow.")
# else:
#     print("Does not work.")

while True:
    try:
        start = input("Press any key to start !")
        url = f"https://www.reddit.com/r/todayilearned/new/.json"
        til = requests.get(url, headers={'User-agent': 'm0'}).json()
        fact = til["data"]["children"][0]["data"]["title"]
        if fact[0:3] == "TIL":
            print("New fact detected !")
            if fact[4].isalpha() == True:
                new_fact = fact[4].capitalize() + fact[5:]
            else:
                new_fact = fact[5].capitalize() + fact[6:]
        else:
            print("Does not work.")
        print(new_fact)
        print("Source: " + source)
        txtlist.write(new_fact + "\n")
        txtlist.close()
        end = input("To view your list of TIL facts, please enter in the command: read. To end script please type: stop. Otherwise press any key to continue. (Please allow a 15 second delay when obtaining another fact.)")
        end = end.lower()
        if end == "stop":
            txtlist.close()
            break
        elif end == "read":
            txtlist = open("TIL List.txt", "r+")
            print (txtlist.read())
            txtlist.close()
            time.sleep(15)
            continue
        else:
            txtlist.close()
            time.sleep(15)
            continue
    except KeyError:
        print("Sorry we are looking into the error.")
        continue