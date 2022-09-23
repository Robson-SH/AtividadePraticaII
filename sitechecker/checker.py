from http.client import HTTPConnection
from urllib.parse import urlparse

def site_is_online(url, timeout=2):
    # Retorna verdadeiro se o site estiver online
    # Senão, retorna uma exception
    error = Exception("unknown error")
    parser = urlparse(url) #Testa apenas para o host
    host = parser.netloc or parser.path.split("/")[0]
    for port in (80, 443):
        