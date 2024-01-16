## Site Acessivel ##
import urllib
import urllib.request

try:
    urllib.request.urlopen("http://www.pudim.com.br/")
except:
    print("\033[91mO site Pudim não está acessivel no momento\033[0m")   
else:
     print("\033[92mO site Pudim está acessivel\033[0m")       