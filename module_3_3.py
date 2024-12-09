def print_params(a=1, b='строка', c=True):
    print(f"a = {a}")
    print(f"b = {b}")
    print(f"c = {c}")

# Вызовы функции с разным количеством аргументов
print_params()  # Вызов без аргументов
print_params(5)  # Вызов с одним аргументом
print_params(5, 'другая строка')  # Вызов с двумя аргументами
print_params(5, 'другая строка', False)  # Вызов со всеми аргументами
print_params(b=25)  # Вызов с ключевым аргументом b
print_params(c=[1, 2, 3])  # Вызов с ключевым аргументом c

values_list = [10, 'новый текст', False]
values_dict = {'a': 20, 'b': 'еще один текст', 'c': True}

print_params(*values_list)  # Распаковка списка
print_params(**values_dict)  # Распаковка словаря

values_list_2 = [30, 'последний текст']

print_params(*values_list_2, c=42)  # Распаковка списка + аргумент
