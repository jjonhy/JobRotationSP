# Recebe a string de entrada do usuário
string = input("Digite uma string: ")

# Converte a string em uma lista de caracteres
lista_chars = list(string)

# Inverte a ordem dos caracteres na lista
tamanho = len(lista_chars)
for i in range(tamanho // 2):
    temp = lista_chars[i]
    lista_chars[i] = lista_chars[tamanho - i - 1]
    lista_chars[tamanho - i - 1] = temp

# Converte a lista de volta para uma string
string_invertida = "".join(lista_chars)

# Imprime a string invertida
print("A string invertida é:", string_invertida)
