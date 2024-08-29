"""
Script: Export FireHydrant Users to CSV

Description:
This Python script exports user data from FireHydrant to a CSV file. The user is prompted to enter 
the location of a configuration file that contains the FireHydrant API token. The script then retrieves 
all users using the FireHydrant API, handling pagination, and saves the data to a CSV file named `firehydrant_users.csv`.

Functions:
- `load_firehydrant_token(file_path)`: Reads the FireHydrant API token from a specified JSON configuration file.
- `fetch_users(url, headers, params)`: Retrieves users data from the FireHydrant API, handling pagination.
- `write_users_to_csv(users, csv_filename)`: Writes the retrieved users data to a CSV file.

Usage:
1. **Configuration File Setup:**
   - Create a JSON file (e.g., `config.json`) on your computer containing the FireHydrant API token:
     ```json
     {
         "firehydrant_token": "your-firehydrant-token"
     }
     ```
   - Ensure that this file is securely stored and accessible only by authorized users.

2. **Running the Script:**
   - When prompted, provide the full path to your `config.json` file.
   - The script will read the token from the file, retrieve all users from FireHydrant, and export 
     them to `firehydrant_users.csv`.

Notes:
- **Security Considerations:** Ensure that the `config.json` file is stored in a secure location and 
  has appropriate access controls to prevent unauthorized access to the API token.
- **Customization:** You can modify the script to include additional fields or change the structure of the CSV file.

Author: Chad Ramey
Date: August 29, 2024
"""

import requests
import csv
import json

# Function to read the FireHydrant API token from a JSON file
def load_firehydrant_token(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)["firehydrant_token"]

# Prompt the user for the configuration file location
config_file = input("Please enter the full path to your configuration file (e.g., config.json): ")
authorization_token = load_firehydrant_token(config_file)

url = "https://api.firehydrant.io/v1/users"
params = {
    'per_page': 100,
    'page': 1
}

headers = {
  'Content-Type': 'application/json',
  'Authorization': authorization_token
}

# Create a CSV file to write the data
csv_filename = 'firehydrant_users.csv'
with open(csv_filename, 'w', newline='', encoding='utf-8') as csvfile:
    csv_writer = csv.writer(csvfile)
    
    # Write the header row
    csv_writer.writerow(["id", "name", "email", "slack_user_id", "slack_linked", "created_at", "updated_at"])

    while True:
        response = requests.get(url, headers=headers, params=params)
        data = response.json()

        if 'data' not in data or not data['data']:
            print("No more data or unexpected response format.")
            break

        for user in data['data']:
            csv_writer.writerow([
                user['id'],
                user['name'],
                user['email'],
                user['slack_user_id'],
                user['slack_linked?'],
                user['created_at'],
                user['updated_at']
            ])

        params['page'] += 1

print(f"All users exported to {csv_filename}")
