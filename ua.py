import requests

# -- add all their request headers to a list
headers_to_send = []
for header_name in bottle.request.headers:
    headers_to_send.append({
        "name":  header_name,
        "value": bottle.request.headers.get(header_name),
    })

# -- set up the request
headers = {
    'X-API-KEY': "df8c92180ca9f796d36e6a44c6c5c6d0",
}
post_data = {
    "headers": headers_to_send,
}

# -- make the request to the whatismybrowser server
result = requests.post("https://api.whatismybrowser.com/api/v3/detect", data=json.dumps(post_data), headers=headers)

# -- analyse the API response
print(result.json())
print(result.json().get("detection").get("simple_software_string"))  # etc
