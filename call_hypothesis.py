import requests
import random
import schedule
import time

def make_api_call():
    # Define the API endpoint URL
    url = "https://api.hypothes.is/api/search"

    # Define the query parameters
    params = {
        "group": "Y5Ve61rM",
        "user": "acct:jessieyuct@hypothes.is"
    }

    # Define the headers with the bearer token
    headers = {
        "Authorization": "Bearer 6879-pIfUcba5PiKFOCJJQKZ8tFk6EIe1TmYDrqi01MI4BfQ"
    }

    # Make the API call using the GET method
    response = requests.get(url, params=params, headers=headers)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Process the response data
        data = response.json()
        # Return the data
        return data
    else:
        # Handle the error if the request was not successful
        print("Error:", response.status_code, response.text)
        # Return None or handle the error case as per your requirement
        return None

def select_random_prompts(data, num_prompts):
    # Check if the data is available
    if data is None:
        return []

    # Get the list of prompts
    prompts = data['rows']

    # Randomly select the specified number of prompts
    selected_prompts = random.sample(prompts, num_prompts)

    return selected_prompts

def update_prompts():
    # Call the API and retrieve data
    data = make_api_call()

    # Select 6 random prompts from the data
    selected_prompts = select_random_prompts(data, 6)

    # Save the selected prompts to a JSON file
    with open('prompts.json', 'w') as file:
        json.dump(selected_prompts, file)

    print("Prompts updated successfully!")

# Schedule the script to run every Monday at 5:00 AM
schedule.every().monday.at("05:00").do(update_prompts)

# Run the scheduled tasks indefinitely
while True:
    schedule.run_pending()
    time.sleep(1)
