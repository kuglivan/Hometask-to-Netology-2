
# Задача 1:
def get_dict(file):
    cook_book = (x.split('\n') for x in file.split('\n\n'))
    cook_book = {x[0]: [dict(zip(('ingredient_name', 'quantity', 'measure'), x[i].split(' | '))) for i in
                  range(2, 2 + int(x[1]))] for x in cook_book}
    return cook_book

# Задача 2:
def get_shop_list_by_dishes(dishes, person_count):

    with open("cook_file", 'rt', encoding='utf-8') as f:
        file_document = f.read()
    cook_book = get_dict(file_document)

    shop_list = {}
    for dish in dishes:
        for ingredients in cook_book[dish]:
            quantity = int(ingredients['quantity']) * person_count
            dict_of_quantity_and_measure = {}
            dict_of_quantity_and_measure['measure'] = ingredients["measure"]
            dict_of_quantity_and_measure['quantity'] = quantity
            if ingredients['ingredient_name'] not in shop_list:
                shop_list[ingredients['ingredient_name']] = dict_of_quantity_and_measure
            else:
                shop_list[ingredients['ingredient_name']][quantity] += quantity

    return shop_list

# Задача 3:
def work_with_txt_files():

    main_file = ''
    with open("1.txt", encoding='utf-8') as file:
        len_1st_file = len(file.readlines())
    with open("2.txt", encoding='utf-8') as file:
        len_2nd_file = len(file.readlines())
    with open("3.txt", encoding='utf-8') as file:
        len_3rd_file = len(file.readlines())

    if len_1st_file <= len_2nd_file:
        if len_1st_file <= len_3rd_file:
            if len_2nd_file <= len_3rd_file:
                main_file = add_file_1(main_file, len_1st_file)
                main_file = add_file_2(main_file, len_2nd_file)
                main_file = add_file_3(main_file, len_3rd_file)
            else:
                main_file = add_file_1(main_file, len_1st_file)
                main_file = add_file_3(main_file, len_3rd_file)
                main_file = add_file_2(main_file, len_2nd_file)
        else:
            main_file = add_file_3(main_file, len_3rd_file)
            main_file = add_file_1(main_file, len_1st_file)
            main_file = add_file_2(main_file, len_2nd_file)
    else:
        if len_1st_file >= len_3rd_file:
            if len_2nd_file <= len_3rd_file:
                main_file = add_file_2(main_file, len_2nd_file)
                main_file += add_file_3(main_file, len_3rd_file)
                main_file += add_file_1(main_file, len_1st_file)
            else:
                main_file = add_file_3(main_file, len_3rd_file)
                main_file = add_file_2(main_file, len_2nd_file)
                main_file = add_file_1(main_file, len_1st_file)
        else:
            main_file = add_file_2(main_file, len_2nd_file)
            main_file = add_file_1(main_file, len_1st_file)
            main_file = add_file_3(main_file, len_3rd_file)

    with open("main_file", "wt", encoding='utf-8') as file:
        file.write(main_file)


def add_file_1(main_file, len):
    with open("1.txt", encoding='utf-8') as file:
        main_file += f'1.txt\n{len}\n{file.read()}\n'
        return main_file

def add_file_2(main_file, len):
    with open("2.txt", encoding='utf-8') as file:
        main_file += f'2.txt\n{len}\n{file.read()}\n'
        return main_file

def add_file_3(main_file, len):
    with open("3.txt", encoding='utf-8') as file:
        main_file += f'3.txt\n{len}\n{file.read()}\n'
        return main_file


def main():

    # Вывод 1 задания в консоль:
    with open("cook_file", 'rt', encoding='utf-8') as f:
        file_document = f.read()
    cook_book = get_dict(file_document)
    print(cook_book, '\n')

    # Вывод 2 задания в консоль 2-мя способами:
    print(f"{get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2)}\n")

    for line in get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2):
        print(f"{line}: {get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2)[line]}")

    # Использование фу-ии для создания итогового файла:
    work_with_txt_files()

main()