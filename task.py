# Use the request library
import requests

# Set the Target Webpage
url = "http://172.18.58.80/index.php"
r = requests.get(url)

# This will get the status code
print("Status code:")
print("\t *", r.status_code)

# This will just get just the headers
h = requests.head(url)
print("Header:")
print("**********")
# To print line by line
for x in h.headers:
    print("\t ", x, ":", h.headers[x])
print("**********")
print(r.text)

# This will modify the headers user-agent
headers = {
    "User-Agent" : "Mobile"
}
url2 = 'http://172.18.58.80/headers.php'
rh = requests.get(url2, headers=headers)
print(rh.text)
