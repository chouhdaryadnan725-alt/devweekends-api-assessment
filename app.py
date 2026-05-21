import requests

print("--- Country Info Tool ---")
country_name = input("Enter country name: ")

# AI helped me write this URL and request structure
url = f"https://restcountries.com/v3.1/name/{country_name}"
response = requests.get(url)

# Checked if country exists or not
if response.status_code == 404:
    print("Country Name is invalid ! Write Correct spelling.")
else:
    data = response.json()[0]
    print("Country Name:", data['name']['common'])
    print("Capital:", data['capital'][0])
    print("Population:", data['population'])
  
