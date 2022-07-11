import requests
import json


GITHUB_TOKEN = "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"
FRESHDESK_TOKEN = 'yX8wS8f61MaoCYIggGHN'

username=str(input("Enter the username of the GitHub user: "))
Github_response = requests.get(f'https://api.github.com/users/{username}',headers={'Authorization': f'token {GITHUB_TOKEN}'})
Github_response_json= Github_response.json()
Github_Username=Github_response_json['login']
Github_Name=Github_response_json['name']
Github_Email=Github_response_json['email']
Github_Twitter = Github_response_json['twitter_username']
Github_location=Github_response_json['location']
Github_bio=Github_response_json['bio']





Freshdesk_domain = str(input('Enter the Freshdesk subdomain: '))
Freshdesk_password = "Random123?"
headers = { "Content-Type" : "application/json" }
try:

    Freshdesk_FilterSearchContact = requests.get(
        "https://" + Freshdesk_domain + '.freshdesk.com/api/v2/contacts?email=' + Github_Email,
        auth=(FRESHDESK_TOKEN, Freshdesk_password), headers=headers)
    print(Freshdesk_FilterSearchContact.json())
    contact_id = Freshdesk_FilterSearchContact.json()[0]['id']
    print(contact_id)
    update_contact_info = { "name":Github_Name, "twitter_id":Github_Twitter, "address" : Github_location , "description" : Github_bio }

    Freshdesk_UpdateContact = requests.put(
        "https://"+ Freshdesk_domain +".freshdesk.com/api/v2/contacts/"+str(contact_id),
        auth = (FRESHDESK_TOKEN, Freshdesk_password), data = json.dumps(update_contact_info), headers = headers)

    Freshdesk_UpdateResponse=Freshdesk_UpdateContact.status_code

except:
    create_contact_info = { "name" : Github_Username, "email" : Github_Email , "address" : Github_location , "description" : Github_bio , "twitter_id" : Github_Twitter}
    headers = { "Content-Type" : "application/json" }


    Freshdesk_CreateContact = requests.post(
        "https://"+ Freshdesk_domain +".freshdesk.com/api/v2/contacts",
        auth = (FRESHDESK_TOKEN, Freshdesk_password), data = json.dumps(create_contact_info), headers = headers)

    Freshdesk_CreateResponse=Freshdesk_CreateContact.status_code




