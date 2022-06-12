#python code to shorten a link
import requests
api_key = "21e1aaf8c250543ca9d50018215c00cca4f09"
url = input("Enter URL to be shortend : ")
short = "https://cutt.ly/api/api.php"

response = requests.get(str(short),params={"key":api_key,"short":url})
#print(response.text)
if response.json()['url']['status']==7:
    shortlink = response.json()['url']['shortLink']
    print("Shortented link : ",shortlink)