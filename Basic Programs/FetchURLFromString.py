import re

#str = "I am blogger at https://172.19.5.28:8080/MSearchmanager"
str = "I am blogger at https://172.19.5.28:8080/MSearchmanager and also http://10.155.8.46:8080/solr and more over on http://www.amazon.in"

#http://urlregex.com    #Site for url regex for all languages

url = re.findall("http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+",str)
print(url)

