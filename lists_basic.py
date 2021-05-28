# Principais métodos aplicados em listas
animals = ["pangolin", "cassowary", "sloth", "dog"];
animals[0]   # 'pangolin'
animals[1]   # 'cassowary'
animals[2]   # 'sloth'
animals[3]   # 'dog'

# animals[4]   # IndexError: list index out of range

lis = list() # equivalente a l = []
lis = list(['a', 'b', 'c']) # equivalente a l = ['a', 'b, 'c']

myList = [1, 2, 3, 4]
for number in myList:
    print (number * 2)
    
choices = ['pizza', 'pasta', 'salad', 'nachos']

print('Your choices are:')
for index, item in enumerate(choices):
    print(index, item)

# Se quisermos copiar uma lista podemos realizar uma simples atribuição,
# mas manteremos uma relação entre as duas, ou melhor,
# ambas apontam para o mesmo objeto e as alterações em uma afetará a outra
lista_a = [6, 7, 8, 9]
lista_b = list_a

# Se quisermos copiar uma lista sem manter a referência entre elas, podemos utilizar o operador de fatia [:]
# Temos cópias independentes, um clone
lista_c = [6, 7, 8, 9]
lista_d = lista_c[:]

# Juntando listas (join lists)
m = [1, 2, 3]
n = [4, 5, 6]
o = m + n
print(o) # [1, 2, 3, 4, 5, 6]

o += [7, 8, 9]
print(o) # [1, 2, 3, 4, 5, 6, 7, 8, 9]

# Funções nativas para listas
nums = ["um"]
print(nums) # ['um']

# append
nums.append("dois")
nums.append("tres")
nums.append("quatro")
print(nums) # ['um', 'dois', 'tres', 'quatro']

# index
animals = ["ant", "bat", "cat"]
print(animals.index("bat")) # 1
print('dog' in animals)
print('cat' in animals)

# insert
animals = ["ant", "bat", "cat"]
animals.insert(1, "dog")
print(animals) # ["ant", "dog", "bat", "cat"]

# remove
animals = ["ant", "bat", "cat"]
animals.remove("ant")
print(animals) # ["bat", "cat"]

# pop
animals = ["ant", "bat", "cat"]
animals.pop(0) # 'ant'
print(animals) # ["bat", "cat"]

# del
animals = ["ant", "bat", "cat"]
del(animals[0])
print(animals) # ["bat", "cat"]

# sort
lista = ["c", "b", "a"]
print(lista) # ['c', 'b', 'a']
lista.sort()
print(lista) # ['a', 'b', 'c']

# sorted
lista = ["c", "b", "f", "a"]
print(sorted(lista))