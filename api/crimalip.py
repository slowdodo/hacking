import requests

# Set the API endpoint and your API key
endpoint = "https://api.criminalip.com/v1/ip/{ip}"
api_key = "YOUR_API_KEY"

# Set the IP address to check
ip = "1.1.1.1"

# Send the request to the API
response = requests.get(endpoint.format(ip=ip), headers={"X-API-Key": api_key})

# Check the response status code
if response.status_code == 200:
  # Print the response data
  print(response.json())
else:
  # Print the error message
  print(response.text)