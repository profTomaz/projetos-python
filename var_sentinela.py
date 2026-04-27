#Exemplo de Uso da Variável Sentinela

while True:
    comando = input("Digite um Comando - Para Parar Digite: 'Sair' ")
if comando == "sair":
 break
 print(f"Executando: {comando}")
print("programa Encerrado")