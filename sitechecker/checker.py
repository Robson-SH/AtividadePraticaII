from http.client import HTTPConnection
from urllib.parse import urlparse

def site_is_online(url, timeout=2):
    """Retorna verdadeiro se o site estiver online ou retorna uma exception se estiver offline"""
    #Define uma exception genérica
    error = Exception("unknown error")
    #Testa apenas para o host
    parser = urlparse(url)
    host = parser.netloc or parser.path.split("/")[0]
    #Começa um looping usando as portas HTTPS e HTTP para testar se o site está online
    for port in (80, 443):
        connection = HTTPConnection(host=host, port=port, timeout=timeout)
        try:
            connection.request("HEAD", "/")
            return True #Retorna True se a conexão funcionar
        except Exception as e:
            error = e #Retorna um erro se não funcionar
        finally:
            connection.close() #Fecha a conexão
    raise error