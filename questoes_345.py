#Questão 3
def questao_3():
    a = 9
    b = 128
    c = 49
    d = 100
    e = 13
    d = 200

#Questão 4
#Um interruptor deixo aceso por uns minutos e depois desligo
#O segundo eu deixo ligado
#O terceiro eu não mexo nele
# Caso eu entre em quaisquer uma das salas posso supor o seguinte:
# Se estiver quente a lâmpada é porque foi o primeiro interruptor 
# Se estiver aceso é porque foi o segundo pois deixei ligado
# Se estiver frio vai ser o terceiro porque foi o único que não mexi

#Questão 5
def inverter_string(string):
    string_invertida = ''
#Usamos o for para iterar pelo último índice (definido pela string original)
    for i in range(len(string) - 1, -1, -1):
        string_invertida += string[i]
    return string_invertida
#String do usuário
string_original = input("Digite uma string: ")
string_invertida = inverter_string(string_original)
print("String original:", string_original)
print("String invertida:", string_invertida)