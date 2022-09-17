
cook_book = []

try:
    with open('recipes.txt', 'r', encoding='utf-8') as f:
        for line in f:
            dish_name = line.rstrip('\n')
            recipe = {dish_name:[]}
            dish_count = f.readline()
            for i in range(int(dish_count)):
                prod_all = f.readline()
                prod_name, prod_count, prod_ue = prod_all.split(' | ')
                prod_ever = {'ingredient_name': prod_name, 'quantity': prod_count, 'measure': prod_ue.rstrip('\n')}
                recipe[dish_name].append(prod_ever)
            f.readline()
            cook_book.append(recipe)

    print(cook_book)

except FileNotFoundError:
    print('File not found!!!')



#def get_shop_list_by_dishes(person, book):
#    for recipes in book:
#        print(recipes[0].title(), ":")
#        for ingredient in recipes[1]:
#            print(f"{ingredient[0]} {ingredient[1]*person} {ingredient[2]}")
#        print("\n")



#person_count = input('Введите количество персон: ')

