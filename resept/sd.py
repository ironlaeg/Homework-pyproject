
def read_cook_book(filename):
    cook_book = {}
    with open(filename, 'r', encoding='utf-8') as file:
        while True:
            dish_name = file.readline().strip()
            if not dish_name:
                break

            ingredient_count = int(file.readline().strip())

            ingredients = []
            for _ in range(ingredient_count):
                ingredient_line = file.readline().strip()
                ingredient_name, quantity, measure = ingredient_line.split(' | ')
                ingredients.append({
                    'ingredient_name': ingredient_name,
                    'quantity': int(quantity),
                    'measure': measure
                })

            cook_book[dish_name] = ingredients
            file.readline()

    return cook_book





def get_shop_list_by_dishes(dishes, person_count):
    shop_list = {}
    for dish in dishes:
        if dish in cook_book:
            for ingredient in cook_book[dish]:
                name = ingredient['ingredient_name']
                measure = ingredient['measure']
                quantity = ingredient['quantity'] * person_count

                if name in shop_list:
                    shop_list[name]['quantity'] += quantity
                else:
                    shop_list[name] = {'measure': measure, 'quantity': quantity}

    return shop_list



def merge_files(file_list, output_file):
    file_info = []
    for filename in file_list:
        with open(filename, 'r', encoding='utf-8') as file:
            lines = file.readlines()
            file_info.append({
                'filename': filename,
                'line_count': len(lines),
                'content': lines
            })

    file_info.sort(key=lambda x: x['line_count'])

    with open(output_file, 'w', encoding='utf-8') as outfile:
        for info in file_info:
            outfile.write(f"{info['filename']}\n")
            outfile.write(f"{info['line_count']}\n")
            outfile.writelines(info['content'])
            outfile.write('\n')




if __name__ == '__main__':

    cook_book = read_cook_book('recipes.txt')
    print("Cook Book:")
    print(cook_book)


    shop_list = get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2)
    print("\nShop List:")
    print(shop_list)

    file_list = ['1.txt', '2.txt']
    merge_files(file_list, 'result.txt')
    print("\nФайлы объединены в result.txt")