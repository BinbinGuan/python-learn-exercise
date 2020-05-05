import urllib.request
import urllib.parse

url='http://www.baidu.com'
hearder={
   'User-Agent':'Mozilla/5.0 (X11; Fedora; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
}

request=urllib.request.Request(url,headers=hearder)
reponse=urllib.request.urlopen(request).read()

fhandle=open("./1.html","wb")
fhandle.write(reponse)
fhandle.close()