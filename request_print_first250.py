import requests
res=requests.get("https://www.rfc-editor.org/rfc/rfc1918.txt")
res.status_code == requests.codes.ok
print(res.status_code)
len(res.text)
print(res.text[:1000])