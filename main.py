import os

cook_book = {}
try:
    with open('recipes.txt', 'r', encoding='utf-8') as f:
        for line in f:
            dish_name = line.rstrip('\n')
            recipe = []
            dish_count = f.readline()
            for i in range(int(dish_count)):
                prod_all = f.readline()
                prod_name, prod_count, prod_ue = prod_all.split(' | ')
                prod_ever = {'ingredient_name': prod_name, 'quantity': int(prod_count), 'measure': prod_ue.rstrip('\n')}
                recipe.append(prod_ever)
            f.readline()
            cook_book[dish_name] = recipe
    print(cook_book)

except FileNotFoundError:
    print('File not found!!!')


def get_shop_list_by_dishes(person, list):
    all_recep = {}
    for cook in list:
        for recipes,recept in cook_book.items():
            if recipes == cook:
                for recept in cook_book[recipes]:
                    ingr = recept['ingredient_name']
                    quant = int(recept['quantity']) * person
                    if ingr in all_recep.keys():
                        quant = int(recept['quantity']) * person + all_recep[ingr]['quantity']
                    ue = recept['measure']
                    prod_rep = {ingr :{'measure' : ue, 'quantity' : quant}}
                    all_recep.update(prod_rep)

    print(all_recep)


cook_count = int(input('Введите количество блюд: '))
cook_list = []

for i in range(cook_count):
    print('Блюдо номер ', i + 1)
    dish = input('Введите название блюда: ')
    if dish in cook_book.keys():
        cook_list.append(dish)
    else:
        print('Такого блюда нет в меню!')


person_count = int(input('Введите количество персон: '))
get_shop_list_by_dishes(person_count,cook_list)

current_directory = os.getcwd()
my_dir ='sort'
full_path = current_directory + "\\" + my_dir

def sort_files():
    ls = [f for f in os.listdir(full_path)if os.path.isfile(os.path.join(full_path, f))]
    ls.sort()

    dict_files = {}
    sorted_dict = {}
    file_names = {}
    sorted_names = {}

    for file_name in ls:
        f_name = full_path + "\\" + file_name
        count_line = sum(1 for line in open(f_name, 'r', encoding='utf-8'))
        dict_files[count_line] = f_name
        file_names[count_line] = file_name

    for k in sorted(dict_files.keys()):
        sorted_dict[k] = dict_files[k]
        sorted_names[k] = file_names[k]
    print(sorted_dict)

    for j in sorted_dict.keys():
        with open(sorted_dict[j], encoding='utf-8') as first, open('result.txt', 'a', encoding='utf-8') as second:
            second.write(sorted_names[j])
            second.write('\n')
            data = first.read()
            second.write(data)
            second.write('\n')
            second.write(str(j))
            second.write('\n')

print(sort_files())

