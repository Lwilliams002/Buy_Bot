import requests
import json


from buying import check_ticket_availability

# Define the API endpoint and include your API key
url = "https://app.ticketmaster.com/discovery/v2/events?apikey=I5jjDofsEMwSojQNJFqs33iXlWFutL2Q&keyword=ufc"

# Make the API request and retrieve the response
response = requests.get(url)
data = False
# Check the status code of the response to make sure it was successful
if response.status_code == 200:
    # Parse the response data as JSON
    data = json.loads(response.text)

    # Extract the relevant information from the response data
    for event in data['_embedded']['events']:
        event_name = event['name']
        event_date = event['dates']['start']['localDate']
        ticket_status = event['dates']['status']['code']

        # Check if the event is called "UFC 287" and the ticket status is "onsale"
        if event_name == "UFC 286" and ticket_status == "onsale":
            print("Event:", event_name)
            print("Date:", event_date)
            print("Ticket status:", ticket_status)
            print("\n")
            # Alert you that the event is available
            print("ALERT: UFC 287 tickets are now on sale!")

            header = {"Content-Type": "application/json; charset=utf-8",
                      "Authorization": "Basic Y2Y2YTJjZGUtOGQxYy00ODg4LTkyMzEtMDMyNDVkMTM5MzBh"}
            payload = {
                "app_id": "fa32a5ea-2417-4434-8c10-2cc0269de6a8",
                "name": "UFC_buy_bot",
                "sms_from": "+18556462105",
                "contents": {
                    "en": "Ticket Alert",
                    "en": "UFC 287 tickets are now on sale!"
                },
                #
                "include_phone_numbers": ["3059158174"]
            }
            req = requests.post("https://onesignal.com/api/v1/notifications", headers=header, data=json.dumps(payload))

            print(req.status_code, req.reason)

            # Check the status code of the response to make sure it was successful
            if req.status_code == 200:
                print("Push notification sent successfully")
                print(req.text)

                check_ticket_availability(data)
            else:
                print("Failed to send push notification:", req.text)


else:
    print("Request failed with status code:", response.status_code)
