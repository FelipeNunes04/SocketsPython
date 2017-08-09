from socket import *

serverPort = 20000
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('',serverPort))
serverSocket.listen(1)
print("O servidor esta pronto para recepcao.")
while True:
    connectionSocket, addr = serverSocket.accept()
    message = connectionSocket.recv(2048).decode()
    requisicao = message.split()
    arquivo,http = requisicao[1], requisicao[2]
    try:
        file = open(arquivo[1:],"r")
        texto = file.read()
        existe = True
    except Exception:
        existe = False

    if(existe):
        resultado ="""%s 200 OK
        Content-Type: text/html  \r\n \r\n

        %s
        """%(http,texto)
    else:
        file = open("404.html","r")
        texto = file.read()
        resultado ="""%s 404 NOT FOUND
        Content-Type: text/html  \r\n \r\n

        %s
        """%(http,texto)

    connectionSocket.send(resultado.encode())
    connectionSocket.close()
