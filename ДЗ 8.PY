# Задача 38: Создать телефонный справочник возможностью 
# добавления записей и чтения. Пользователь также может 
# ввести фамилию, тогда программа должны вывести на экран 
# все записи с этой фамилий. Также пользователь может 
# добавлять новых людей в справочник в режиме экспорт.

# Поиск:
def change_file():
    find_info = input()
    new_info = input()
    with open(path_file,'r+',encoding='UTF-8') as f:
        for line in f:
            if find_info.casefold() in line.casefold():
                if input("Да/Нет") == "Да":
                    lst = (line.strip()).split(' ')
                    print(lst)
                else: continue


# Весь код:
# 1.
def read_file():
    with open(path_file,'r',encoding='UTF-8') as f:
        for line in f:
            print(line.strip())

def write_file():
    with open(path_file,'a',encoding='UTF-8') as f:
        f.writelines('\n'+input())


def find_file():
    find_info = input()
    with open(path_file,'r',encoding='UTF-8') as f:
        for line in f:
            if find_info.casefold() in line.casefold():
                print(line)


def change_file():
    find_info = input()
    new_info = input()
    with open(path_file,'r+',encoding='UTF-8') as f:
        for line in f:
            if find_info.casefold() in line.casefold():
                if input("Да/Нет") == "Да":
                    lst = (line.strip()).split(' ')
                    print(lst)
                else: continue




def main():
    find_file()
    


path_file = r"Справочник.txt"
if __name__ == '__main__':
    main()
    
    
    
    
    
# 2.
# # Задача 38: Дополнить телефонный справочник возможностью изменения и удаления данных. 
# # Пользователь также может ввести имя или фамилию, и Вы должны реализовать функционал для изменения и удаления данных

def change_function():                                      
    change = input('Введите команду a - записать контакт; b - прочитать контакт; c - найти контакт; d - заменить контакт; e - удалить контакт: ')                     
    if change == 'a':
        writing_in_file()
    if change == 'b':
        read_file()
    if change == 'c':
        find_file()
    if change == 'd':
        change_contact()
    if change == 'e':
        delete_file()


def writing_in_file():
       with open(file_path, 'a') as f:
            f.writelines('\n'+input("Введите ФИО и телефон(на английском): "))


def read_file():                           
    with open(file_path, 'r') as f:                         
        for line in f:
            print(line)


def find_file():
    find_info = input("Введите инфорацию, которую хотите найти(на английском): ")
    with open(file_path,'r') as f:
        for line in f:
            if find_info.casefold() in line.casefold():
                print(line)

def change_contact():
    data_str = input("Введите контакт (например, имя)(на английском): ")
    user_lst = []
    with open("Справочник.txt", "r", encoding="utf-8") as d:
        lst = d.readlines()
        for line in lst:
            if data_str in line:
                user_lst.append(line)
    print(*user_lst)
    answer = int(input("Введите строчку, которую хотите заменить(на английском): "))
    new_contact = input("Введите новый контакт: ") + "\n"
    
    with open("Справочник.txt", "w", encoding="utf-8") as d:
        for line in lst:
            if user_lst[answer - 1] != line:
                d.write(line)
            else:
                d.write(new_contact)
    print("Готово!")


def delete_file():
    with open(file_path, 'r', encoding="utf-8") as f:
        X = input('Введите Имя или Фамилию для удаления(на английском): ')
        lines = f.readlines()
        with open(file_path, 'w', encoding="utf-8") as f:
            for line in lines:
                if X in line:
                    print("Строка удалена")
                else:
                    print(line)    
                    f.write(line)


file_path = r"Справочник.txt"
change_function()