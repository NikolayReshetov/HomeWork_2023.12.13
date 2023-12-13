from Operations import *

CONTACTS = 'Contacts.txt'

def interface():
    while True:
        print('\n Выберете действие:\
            \n 1 - Добавить контакт\
            \n 2 - Вывести контакты\
            \n 3 - Найти контакт\
            \n 4 - Изменить контакт\
            \n 5 - Удалить контакт\
            \n 0 - Выйти')
        command = int(input())
        match command:
            case 1:
                add_contacts(CONTACTS)
            case 2:
                print_contacts(CONTACTS)
            case 3:
                find_contact(CONTACTS)
            case 4:
                change_contact(CONTACTS)
            case 5:
                remove_contact(CONTACTS)
                pass
            case 0:
                break

if __name__ == '__main__':
    interface()