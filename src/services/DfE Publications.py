import requests

url = "https://api.education.gov.uk/statistics/v1/publications"

response = requests.get(url)

print(response.text)
