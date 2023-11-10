import json
import datetime

# Read the JSON document from a file
with open('json_file.json', 'r') as file:
    data = json.load(file)

# Find and print the Payee ID value
payee_id = data['payee']['id']
print(f"Payee ID: {payee_id}")

# Find any invoices that contain the text "583"
invoices_containing_583 = [invoice for invoice in data['invoiceIds'] if "583" in invoice]
print(f"Invoices containing '583': {invoices_containing_583}")

# Convert date/time fields to text in the format '%Y-%m-%dT%H:%M:%S'
for field in ['claimDateTime', 'fileDateTime', 'receivedDateTime']:
    timestamp = data[field] / 1e3  # Convert milliseconds to seconds
    datetime_obj = datetime.datetime.fromtimestamp(timestamp)
    data[field] = datetime_obj.strftime('%Y-%m-%dT%H:%M:%S')

# Write the json document back out to a new file
with open('modified_json_file.json', 'w') as file:
    json.dump(data, file, indent=4)

print("JSON document has been modified and saved to 'modified_json_file.json'")
