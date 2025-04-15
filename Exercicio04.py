i = 1
soma = 0
numAluno = int(input("Digite o número de alunos: "))

while i <=numAluno:
    vnota = float(input("Digite a nota: "))
    soma += vnota
    i += 1
media = soma/numAluno
print(f"Sua média: {media}")