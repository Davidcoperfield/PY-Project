# Use the request library
import requests

# Set the Target Webpage
inputUrl = input("Enter the URL: ")
url = str(inputUrl)
r = requests.get(url)
print(r.text)