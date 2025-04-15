#faça um código para ler dois valores e realize a divisão do primerio pelo segundo valor
#recibido, caso o segundo valor digitado seja zero solicite novamente o valor informando que só aceitaremos
#valores diferente de zero

valor1 = int (input("Digite o valor um:"))
valor2= int(input("Digite o valor dois:"))

while valor2==0:
    valor2 = int(input("Digite o valor dois, novamente:"))

resultado=valor1/valor2
print (resultado)



