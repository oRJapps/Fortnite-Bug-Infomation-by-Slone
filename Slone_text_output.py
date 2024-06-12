import requests
import json
import deepl


# URL of the Trello board in JSON format
url = "https://trello.com/b/Bs7hgkma/fortnite-community-issues.json"

# Sending a GET request to fetch the board data
response = requests.get(url)

#deepL Settings
with open('settings.json', 'r', encoding="utf-8") as config:
     rf =json.load(config)
     deepl_key = rf["DEEPL_KEY"]
     #JA,EN,PR...,
     language = rf["lang"]
     translator = deepl.Translator(deepl_key)



#Judge List(Trello)
def switchcase(idlist):
     if idlist == "5d42ac7f1de207797fe9222d":
          return "General Top Issues"
     elif idlist == "5a8ae9c6b95d537ef2173cd3":
          return "Battle Royale Top Issues"
     elif idlist == "6570d040174484f272ba5e90":
          return "LEGO Fortnite Top Issues"
     elif idlist == "6570d04e9f5cee5001ce32b1":
          return "Rocket Racing Top Issues"
     elif idlist == "6570d058de3aa75e45718897":
          return "Fortnite Festival Top Issues"
     elif idlist == "5a8ae9c6b95d537ef2173cd2":
          return "Save the World Top Issues"

# Checking if the request was successful
if response.status_code == 200:
    board_data = response.json()
    # Saving the board data to a file for later inspection
    with open('fortnite_community_issues.json', 'w') as f:
        json.dump(board_data, f, indent=4)
    print("Board data has been successfully retrieved and saved to 'fortnite_community_issues.json'.")

                           
else:
    print(f"Failed to fetch the board data. Status code: {response.status_code}")


    
path_all_text = "slone-all-infomation.txt"
with open('fortnite_community_issues.json', 'r') as f:
        with open(path_all_text, "a", encoding="utf-8", newline="\n") as all_file:
          all_file.truncate(0)
          for i in board_data["cards"]:
            
            if i["closed"] != True and i["labels"] !=[]:
                    #idListがInformation以外の場合データを取り出す
                    if i["idList"] != "5a8af516be70fabe10706245" :
                
                        name = str(i["name"])
                        desc = i["desc"]
                        #date
                        date =i["dateLastActivity"]
                        #label
                        label =i["labels"][0]["name"]
                        #list
                        list = switchcase(i["idList"])
                        #Trancelate Japanese
                        resault = translator.translate_text(name, target_lang=language)
                        
                        all_file.write(date+f":"+list+f":" + str(resault)+label+f'\n')
print(path_all_text+"を保存しました")
                        
path_text ="slone-NextUPdate-infomation.txt"     
with open('fortnite_community_issues.json', 'r') as f:
        with open(path_text, "a", encoding="utf-8", newline="\n") as file:
          file.truncate(0)
          for i in board_data["cards"]:
            if i["closed"] != True and i["labels"] !=[] and i["labels"][0]["name"]=="Fixed in Next Game Update":
                    #idListがInformation以外の場合データを取り出す
                    if i["idList"] != "5a8af516be70fabe10706245": 
                        #label
                        label =i["labels"][0]["name"]
          
                        name = str(i["name"])
                        desc = i["desc"]
                        #date
                        date =i["dateLastActivity"]
                        
                        #list
                        list = switchcase(i["idList"])
                        #Trancelate Japanese
                        resault = translator.translate_text(name, target_lang=language)
                        
                        file.write(date+f":"+list+f":" + str(resault)+label+f'\n')
print(path_text+"を保存しました")
                        
                        