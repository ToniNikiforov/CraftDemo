import requests
from requests import auth
import json


GITHUB_TOKEN = "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"
username=str(input("Enter the username of the GitHub user: "))
Github_response = requests.get(f'https://api.github.com/users/{username}',headers={'Authorization': f'token {GITHUB_TOKEN}'})
Github_response_json= Github_response.json()
Github_Username=Github_response_json['login']
Github_Name=Github_response_json['name']
Github_Email=Github_response_json['email']
Github_Avatar=Github_response_json['avatar_url']
Github_Twitter = Github_response_json['twitter_username']
Github_company=Github_response_json['company']
print(type(Github_response_json['email']))


FRESHDESK_TOKEN = 'yX8wS8f61MaoCYIggGHN'
Freshdesk_domain = str(input('Enter the Freshdesk subdomain: '))
Freshdesk_password = "Random123?"
headers = { "Content-Type" : "application/json" }
Freshdesk_FilterSearchContact = requests.get("https://"+ Freshdesk_domain +'.freshdesk.com/api/v2/search/contacts?query="email : '+Github_Email+'"', auth = (FRESHDESK_TOKEN, Freshdesk_password), headers = headers)
print(Freshdesk_FilterSearchContact.json())#[0]['id']
'''
create_contact_info = { "name" : Github_Username, "email" : Github_Email }
headers = { "Content-Type" : "application/json" }


Freshdesk_CreateContact = requests.post("https://"+ Freshdesk_domain +".freshdesk.com/api/v2/contacts", auth = (FRESHDESK_TOKEN, Freshdesk_password), data = json.dumps(create_contact_info), headers = headers)
print(Freshdesk_CreateContact.json())

contact_id = str(Freshdesk_CreateContact.json()['id'])
update_contact_info = { "name":Github_Name, "twitter_id":Github_Twitter,"job_title":'Journalist'}

Freshdesk_UpdateContact = requests.put("https://"+ Freshdesk_domain +".freshdesk.com/api/v2/contacts/"+contact_id, auth = (FRESHDESK_TOKEN, Freshdesk_password), data = json.dumps(update_contact_info), headers = headers)
print(Freshdesk_UpdateContact.json())
'''