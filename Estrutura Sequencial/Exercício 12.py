#Tendo como dados de entrada a altura de uma pessoa, construa um algoritmo que calcule seu peso ideal
altura = float(input('Informe sua altura: '))
peso = (72.7 * altura) - 58
print(f'O peso ideial para sua altura de {altura} é de: {peso:.2f} KG')
