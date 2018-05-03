# coding: utf-8

# Começando com os imports
import csv
import matplotlib.pyplot as plt

# Vamos ler os dados como uma lista
print("Lendo o documento...")
with open("chicago.csv", "r") as file_read:
    reader = csv.reader(file_read)
    data_list = list(reader)
print("Ok!")

# Vamos verificar quantas linhas nós temos
print("Número de linhas:")
print(len(data_list))

# Imprimindo a primeira linha de data_list para verificar se funcionou.
print("Linha 0: ")
print(data_list[0])
# É o cabeçalho dos dados, para que possamos identificar as colunas.

# Imprimindo a segunda linha de data_list, ela deveria conter alguns dados
print("Linha 1: ")
print(data_list[1])

input("Aperte Enter para continuar...")
# TAREFA 1
# TODO: Imprima as primeiras 20 linhas usando um loop para identificar os dados.
print("\n\nTAREFA 1: Imprimindo as primeiras 20 amostras")
for line in data_list[1:21]:
    print(line)

# Vamos mudar o data_list para remover o cabeçalho dele.
data_list = data_list[1:]

# Armazena as 20 primeiras linhas em samples.
samples = data_list[:20]

# Nós podemos acessar as features pelo índice
# Por exemplo: sample[6] para imprimir gênero, ou sample[-2]

input("Aperte Enter para continuar...")
# TAREFA 2
# TODO: Imprima o `gênero` das primeiras 20 linhas

print("\nTAREFA 2: Imprimindo o gênero das primeiras 20 amostras")
for sample in data_list[:20]:
    print(sample[-2])

# Ótimo! Nós podemos pegar as linhas(samples) iterando com um for, e as colunas(features) por índices.
# Mas ainda é difícil pegar uma coluna em uma lista. Exemplo: Lista com todos os gêneros

input("Aperte Enter para continuar...")
# TAREFA 3
# TODO: Crie uma função para adicionar as colunas(features) de uma lista em outra lista, na mesma ordem


def column_to_list(data, index):
    """
    Cria uma lista com os valores de uma coluna.
    Argumentos:
        data: list
        index: int
    Retorna:
        Uma lista com valores da coluna informada pelo argumento index.
    """
    return [sample[index] for sample in data]


# Vamos checar com os gêneros se isso está funcionando (apenas para os primeiros 20)
print("\nTAREFA 3: Imprimindo a lista de gêneros das primeiras 20 amostras")
print(column_to_list(data_list, -2)[:20])

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert type(column_to_list(data_list, -2)) is list, "TAREFA 3: Tipo incorreto retornado. Deveria ser uma lista."
assert len(column_to_list(data_list, -2)) == 1551505, "TAREFA 3: Tamanho incorreto retornado."
assert column_to_list(data_list, -2)[0] == "" and column_to_list(data_list, -2)[1] == "Male", "TAREFA 3: A lista não coincide."
# -----------------------------------------------------

input("Aperte Enter para continuar...")
# Agora sabemos como acessar as features, vamos contar quantos Male (Masculinos) e Female (Femininos) o dataset tem
# TAREFA 4
# TODO: Conte cada gênero. Você não deveria usar uma função parTODO isso.
male = 0
female = 0

for gender in column_to_list(data_list, -2):
    if gender.lower() == "male":
        male += 1
    elif gender.lower() == "female":
        female += 1

# Verificando o resultado
print("\nTAREFA 4: Imprimindo quantos masculinos e femininos nós encontramos")
print("Masculinos: ", male, "\nFemininos: ", female)

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert male == 935854 and female == 298784, "TAREFA 4: A conta não bate."
# -----------------------------------------------------

input("Aperte Enter para continuar...")
# Por que nós não criamos uma função parTODO isso?
# TAREFA 5
# TODO: Crie uma função para contar os gêneros. Retorne uma lista.
# Isso deveria retornar uma lista com [count_male, count_female] (exemplo: [10, 15] significa 10 Masculinos, 15 Femininos)


def count_gender(data_list):
    """
    Totaliza o número de generos (masculino e feminino).
    Argumentos:
        data_list: list
    Retorna:
        Totais de generos [masculino, feminino].
    """
    male = 0
    female = 0
    for gender in column_to_list(data_list, -2):
        if gender.lower() == "male":
            male += 1
        elif gender.lower() == "female":
            female += 1
    return [male, female]


print("\nTAREFA 5: Imprimindo o resultado de count_gender")
print(count_gender(data_list))

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert type(count_gender(data_list)) is list, "TAREFA 5: Tipo incorreto retornado. Deveria retornar uma lista."
assert len(count_gender(data_list)) == 2, "TAREFA 5: Tamanho incorreto retornado."
assert count_gender(data_list)[0] == 935854 and count_gender(data_list)[1] == 298784, "TAREFA 5: Resultado incorreto no retorno!"
# -----------------------------------------------------

input("Aperte Enter para continuar...")
# Agora que nós podemos contar os usuários, qual gênero é mais prevalente?
# TAREFA 6
# TODO: Crie uma função que pegue o gênero mais popular, e retorne este gênero como uma string.
# Esperamos ver "Masculino", "Feminino", ou "Igual" como resposta.


def most_popular_gender(data_list):
    """
    Função que identifica qual gênero com maior número de registros em uma lista.
    Argumentos:
        data_list: list
    Retorna:
        Gênero (Masculino, Feminino ou Igual).
    """
    count = count_gender(data_list)
    if count[0] == count[1]:
        return "Igual"
    elif count[0] > count[1]:
        return "Masculino"
    else:
        return "Feminino"


print("\nTAREFA 6: Qual é o gênero mais popular na lista?")
print("O gênero mais popular na lista é: ", most_popular_gender(data_list))

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert type(most_popular_gender(data_list)) is str, "TAREFA 6: Tipo incorreto no retorno. Deveria retornar uma string."
assert most_popular_gender(data_list) == "Masculino", "TAREFA 6: Resultado de retorno incorreto!"
# -----------------------------------------------------

# Se tudo está rodando como esperado, verifique este gráfico!
gender_list = column_to_list(data_list, -2)
types = ["Male", "Female"]
quantity = count_gender(data_list)
y_pos = list(range(len(types)))
plt.bar(y_pos, quantity)
plt.ylabel('Quantidade')
plt.xlabel('Gênero')
plt.xticks(y_pos, types)
plt.title('Quantidade por Gênero')
plt.show(block=True)

input("Aperte Enter para continuar...")
# TAREFA 7


def count_column_value(column_list):
    """
    Agrupa e soma os valores de uma coluna de uma lista.
    Argumentos:
        column_list: list
    Retorna:
        Dicionário com o valor da colna e a soma.
    """
    data = {}
    for column in column_list:
        if column:
            try:
                data[column] += 1
            except KeyError:
                data[column] = 1
    return data


# TODO: Crie um gráfico similar para user_types. Tenha certeza que a legenda está correta.
print("\nTAREFA 7: Verifique o gráfico!")

user_types_list = column_to_list(data_list, -3)
user_types_sumarized = count_column_value(user_types_list)
print("Valores: ", user_types_sumarized)
types = user_types_sumarized.keys()
quantity = user_types_sumarized.values()
y_pos = list(range(len(types)))
plt.bar(y_pos, quantity)
plt.ylabel('Quantidade')
plt.xlabel('Tipos')
plt.xticks(y_pos, types)
plt.title('Quantidade por Tipos')
plt.show(block=True)


input("Aperte Enter para continuar...")
# TAREFA 8
# TODO: Responda a seguinte questão
male, female = count_gender(data_list)
print("\nTAREFA 8: Por que a condição a seguir é Falsa?")
print("male + female == len(data_list):", male + female == len(data_list))
answer = "Porque 316867 linhas do arquivo estão com a coluna 'Gender' em branco. E valores em branco não estão sendo somados."
print("resposta:", answer)

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert answer != "Escreva sua resposta aqui.", "TAREFA 8: Escreva sua própria resposta!"
# -----------------------------------------------------

input("Aperte Enter para continuar...")
# Vamos trabalhar com trip_duration (duração da viagem) agora. Não conseguimos tirar alguns valores dele.
# TAREFA 9
# TODO: Ache a duração de viagem Mínima, Máxima, Média, e Mediana.
# Você não deve usar funções prontas parTODO isso, como max() e min().


def to_float(data):
    """
    Converte os valores de uma lista para float (ignora valores em branco).
    Argumentos:
        data: list
    Retorna:
        Lista com os valores convertidos para float.
    """
    return [float(i) for i in data if i]


def my_min(data):
    """
    Encontra o menor valor em uma lista de números.
    Argumentos:
        data: list
    Retorna:
        Menor valor da lista.
    """
    # primeiro valor da lista ordenada.
    return sorted(data)[0]


def my_max(data):
    """
    Encontra o maior valor em uma lista de números.
    Argumentos:
        data: list
    Retorna:
        Maior valor da lista.
    """
    # ultimo valor da lista ordenada.
    return sorted(data)[-1]


def my_sum(data):
    """
    Soma os valores de uma lista de números.
    Argumentos:
        data: list
    Retorna:
        Soma dos valores da lista.
    """
    sum = 0
    for i in data:
        sum += i
    return sum


def my_mean(data):
    """
    Calcula a média de uma lista de números.
    Argumentos:
        data: list
    Retorna:
        Valor médio da lista.
    """
    return my_sum(data) / len(data)


def my_median(data):
    """
    Calcula o valor mediano de uma lista de números.
    Argumentos:
        data: list
    Retorna:
        Valor mediano.
    """
    # solução: https://gist.github.com/DevScience/602c3b066549b64a32e5
    sorted_data = sorted(data)
    middle = len(sorted_data) // 2
    median = 0

    if len(sorted_data) % 2 == 0:
        median = (sorted_data[middle + 1] + sorted_data[middle + 2]) / 2
    else:
        median = sorted_data[middle + 1] * 1

    return median


trip_duration_list = to_float(column_to_list(data_list, 2))
min_trip = my_min(trip_duration_list)
max_trip = my_max(trip_duration_list)
mean_trip = my_mean(trip_duration_list)
median_trip = my_median(trip_duration_list)


print("\nTAREFA 9: Imprimindo o mínimo, máximo, média, e mediana")
print("Min: ", min_trip, "Max: ", max_trip, "Média: ", mean_trip, "Mediana: ", median_trip)

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert round(min_trip) == 60, "TAREFA 9: min_trip com resultado errado!"
assert round(max_trip) == 86338, "TAREFA 9: max_trip com resultado errado!"
assert round(mean_trip) == 940, "TAREFA 9: mean_trip com resultado errado!"
assert round(median_trip) == 670, "TAREFA 9: median_trip com resultado errado!"
# -----------------------------------------------------

input("Aperte Enter para continuar...")
# TAREFA 10
# Gênero é fácil porque nós temos apenas algumas opções. E quanto a start_stations? Quantas opções ele tem?
# TODO: Verifique quantos tipos de start_stations nós temos, usando set()

start_stations = column_to_list(data_list, 3)
start_stations = set(start_stations)

print("\nTAREFA 10: Imprimindo as start stations:")
print(len(start_stations))
print(start_stations)

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert len(start_stations) == 582, "TAREFA 10: Comprimento errado de start stations."
# -----------------------------------------------------

input("Aperte Enter para continuar...")
# TAREFA 11
# Volte e tenha certeza que você documenteou suas funções. Explique os parâmetros de entrada, a saída, e o que a função faz. Exemplo:
# def new_function(param1: int, param2: str) -> list:

"""
Função de exemplo com anotações.
    Argumentos:
        param1: O primeiro parâmetro.
        param2: O segundo parâmetro.
    Retorna:
        Uma lista de valores x.
"""

input("Aperte Enter para continuar...")
# TAREFA 12 - Desafio! (Opcional)
# TODO: Crie uma função para contar tipos de usuários, sem definir os tipos
# para que nós possamos usar essa função com outra categoria de dados.
print("Você vai encarar o desafio? (yes ou no)")
answer = "yes"


def count_items(column_list):
    """
    Sumariza a valor de um acoluna.
    Argumentos:
        column_list: list
    Retorna:
        Valores e Totais.
    """
    dic = count_column_value(column_list)
    item_types = dic.keys()
    count_items = dic.values()
    return item_types, count_items


if answer == "yes":
    print("Possíveis valores: ", set(column_to_list(data_list, -2)))
    print("Não concordo com o assertion, valores em branco não são gêneros.")

    # ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
    column_list = column_to_list(data_list, -2)
    types, counts = count_items(column_list)
    print("\nTAREFA 11: Imprimindo resultados para count_items()")
    print("Tipos:", types, "Counts:", counts)
    assert len(types) == 3, "TAREFA 11: Há 3 tipos de gênero!"
    assert sum(counts) == 1551505, "TAREFA 11: Resultado de retorno incorreto!"
    # -----------------------------------------------------
