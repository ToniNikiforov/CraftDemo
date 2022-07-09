import requests
import json


GITHUB_TOKEN = "YOUR_API_KEY"
username=str(input("Enter the username of the GitHub user: "))
Github_response = requests.get(f'https://api.github.com/users/{username}')
Github_response_json= Github_response.json()
Github_Username=Github_response_json['login']
Github_Name=Github_response_json['name']
Github_Email=Github_response_json['email']
Github_Avatar=Github_response_json['avatar_url']
print((Github_response_json))

FRESHDESK_TOKEN = "YOUR_API_KEY"
Freshdesk_domain = str(input('Enter the Freshdesk subdomain: '))
Freshdesk_password = "Random123?"

create_contact_info = { "name" : f"{Github_Username}", "email" : f"{Github_Email}" }
headers = { "Content-Type" : "application/json" }

contact_id = 'CONTACT_ID'
update_contact_info = {  "avatar":f"{Github_Avatar}", "job_title":"Journalist"}

Freshdesk_CreateContact = requests.post("https://"+ Freshdesk_domain +".freshdesk.com/api/v2/contacts", auth = (FRESHDESK_TOKEN, Freshdesk_password), data = json.dumps(create_contact_info), headers = headers)
Freshdesk_UpdateContact = requests.put("https://"+ Freshdesk_domain +".freshdesk.com/api/v2/contacts/"+contact_id, auth = (FRESHDESK_TOKEN, Freshdesk_password), data = json.dumps(update_contact_info), headers = headers)