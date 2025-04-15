x = 0
soma = 0
media=0
aluno=int(input("Quantos alunos na sala:"))
while x<aluno:
    nota=float(input("Qual a nota do aluno:"))
    soma+=nota
    x+=1
media=soma/aluno
print (media)




