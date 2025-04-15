pin= 1234
tentativa=0
maxtentativas = 3
senha = int (input("Digite a sua senha:"))

while senha != pin and tentativa < maxtentativas:
    tentativa += 1
    senha=int (input("Senha errada digite novamente:"))

if tentativa == maxtentativas:
    print("Senha bloqueada")
else:
    print ("Login efetuado com sucesso!")



