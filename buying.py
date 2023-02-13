import time
from ticket_alert import data
from ticket_alert import event_name


def check_ticket_availability(data):
    # Make a request to the Ticketmaster API to check for ticket availability

    # Assuming the API returns a JSON response with a ticket_status field
    # ticket_data = api_response.json()
    # ticket_status = ticket_data["ticket_status"]
    ticket_status = "onsale"  # this should be replaced by the actual ticket status obtained from the API

    if ticket_status == "onsale":
        data
    else:
        print("Tickets are not currently available")


    while True:

        check_ticket_availability()
        time.sleep(60)  # Wait 60 seconds before checking again

response = data
