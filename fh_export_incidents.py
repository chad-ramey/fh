"""
Script: Export FireHydrant Incidents to CSV

Description:
This Python script exports incident data from FireHydrant to a CSV file. The user is prompted to 
enter the location of a configuration file that contains the FireHydrant API token. The script 
then retrieves all incidents using the FireHydrant API, handling pagination, and saves the data 
to a CSV file named `firehydrant_incidents.csv`.

Functions:
- `load_firehydrant_token(file_path)`: Reads the FireHydrant API token from a specified JSON configuration file.
- `fetch_incidents(url, headers)`: Retrieves incidents data from the FireHydrant API, handling pagination.
- `write_incidents_to_csv(incidents, csv_headers)`: Writes the retrieved incidents data to a CSV file.

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
   - The script will read the token from the file, retrieve all incidents from FireHydrant, and export 
     them to `firehydrant_incidents.csv`.

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
firehydrant_token = load_firehydrant_token(config_file)

url = "https://api.firehydrant.io/v1/incidents"
headers = {
    'Content-Type': 'application/json',
    'Authorization': f'Bearer {firehydrant_token}'
}

# Initialize variables for pagination
incidents = []
page = 1
per_page = 20  # Number of incidents per page

while True:
    response = requests.get(f"{url}?page={page}&per_page={per_page}", headers=headers)
    
    # Check if the request was successful
    if response.status_code == 200:
        data = response.json()['data']
        incidents.extend(data)
        
        # If less data than per_page, it means we reached the last page
        if len(data) < per_page:
            break
        page += 1
    else:
        print(f"Failed to retrieve data. Status code: {response.status_code}")
        break

# Define the CSV file headers
csv_headers = ["id", "name", "created_at", "started_at", "discarded_at", "summary", 
               "customer_impact_summary", "description", "current_milestone", "number", 
               "priority", "severity", "severity_color", "severity_impact", "severity_condition", 
               "tag_list", "private_id", "organization_id", "active", "labels", "incident_url", 
               "private_status_page_url", "organization_name", "customers_impacted", "monetary_impact", 
               "monetary_impact_cents", "last_update", "last_note", "report_id", "ai_incident_summary", 
               "channel_name", "channel_reference", "channel_id", "channel_status", "retro_exports", 
               "created_by_name", "created_by_email"]

# Write data to CSV file
with open('firehydrant_incidents.csv', mode='w', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=csv_headers)
    writer.writeheader()
    for incident in incidents:
        incident_data = {
            "id": incident.get("id"),
            "name": incident.get("name"),
            "created_at": incident.get("created_at"),
            "started_at": incident.get("started_at"),
            "discarded_at": incident.get("discarded_at"),
            "summary": incident.get("summary"),
            "customer_impact_summary": incident.get("customer_impact_summary"),
            "description": incident.get("description"),
            "current_milestone": incident.get("current_milestone"),
            "number": incident.get("number"),
            "priority": incident.get("priority"),
            "severity": incident.get("severity"),
            "severity_color": incident.get("severity_color"),
            "severity_impact": incident.get("severity_impact"),
            "severity_condition": incident.get("severity_condition"),
            "tag_list": incident.get("tag_list"),
            "private_id": incident.get("private_id"),
            "organization_id": incident.get("organization_id"),
            "active": incident.get("active"),
            "labels": incident.get("labels"),
            "incident_url": incident.get("incident_url"),
            "private_status_page_url": incident.get("private_status_page_url"),
            "organization_name": incident.get("organization", {}).get("name"),
            "customers_impacted": incident.get("customers_impacted"),
            "monetary_impact": incident.get("monetary_impact"),
            "monetary_impact_cents": incident.get("monetary_impact_cents"),
            "last_update": incident.get("last_update"),
            "last_note": incident.get("last_note"),
            "report_id": incident.get("report_id"),
            "ai_incident_summary": incident.get("ai_incident_summary"),
            "channel_name": incident.get("channel_name"),
            "channel_reference": incident.get("channel_reference"),
            "channel_id": incident.get("channel_id"),
            "channel_status": incident.get("channel_status"),
            "retro_exports": incident.get("retro_exports"),
            "created_by_name": incident.get("created_by", {}).get("name"),
            "created_by_email": incident.get("created_by", {}).get("email")
        }
        writer.writerow(incident_data)

print("Data has been exported to firehydrant_incidents.csv")
