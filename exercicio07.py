nota1 = float (input("Digite o valor um:"))
while nota1 <0 or nota1>10:
    nota1 = float(input("Nota inválida, digite novamente:"))
nota2= float(input("Digite o valor dois:"))
while nota2 <0 or nota2>10:
    nota2 = float(input("Nota inválida, digite novamente:"))

media=(nota1+nota2)/2
print (media)
