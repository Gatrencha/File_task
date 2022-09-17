
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

