import urllib.request
respense2=urllib.request.Request("https://www.tianyancha.com/")
response=urllib.request.urlopen(respense2)
print(response.read())