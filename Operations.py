def print_contacts(file_name):
    with open(file_name, 'r', encoding='utf8') as file:
        all_contacts = file.readlines()
        if len(all_contacts) != 0:
            print('\n Все контакты:')
            for line in all_contacts:
                print(line.strip(), end='\n')
        else:
            print('\nСписок контактов пуст')

def connect_with_user():
    print('\nВведите Фамилию, Имя и номер телефона через пробел, например: Иванов Иван 79332342211')
    return(input())

def add_contacts(file_name):
    with open(file_name, 'r', encoding='utf8') as file:
        all_contacts = file.readlines()
    new_contact = connect_with_user()
    all_contacts.append('\n' + new_contact)
    with open(file_name, 'w', encoding='utf8') as file:
        file.writelines(all_contacts)
    print('\nГотово! Добавлен контакт:', new_contact)

def find_contact(file_name):
    with open(file_name, 'r', encoding='utf8') as file:
        all_contacts = file.readlines()
    print(all_contacts)
    print('\nВыберете критерий для поиска:\
        \n 1 - Фамилия\
        \n 2 - Имя\
        \n 3 - Телефон')
    command = int(input())
    print('\nВведите данные для поиска')
    data = input()
    for cont in all_contacts:
        cont_as_list = cont.strip().split()
        if data in cont_as_list[command - 1]:
            print('\nГотово! В списке контактов найдено: \n', cont)

def change_contact(file_name):
    with open(file_name, 'r', encoding='utf8') as file:
        all_contacts = file.readlines()
    print('\nВыберете критерий для изменения контакта:\
        \n 1 - Фамилия\
        \n 2 - Имя\
        \n 3 - Телефон')
    command = int(input())
    print('\nВведите данные для изменения')
    data = input()
    all_contacts_temp = []
    for contact in all_contacts:
        contact_as_list = contact.strip().split()
        if data in contact_as_list[command - 1]:
            print('\nИзменить', contact_as_list[command - 1], 'в контакте:', contact, ' ?\
            \n 1 - Да, изменить\
            \n 2 - Нет, оставить')
            temp = int(input())
            match temp:
                case 1:
                    print('\nВведите данные вместо ', contact_as_list[command - 1], 'в контакте:', contact)
                    temp_data = input()
                    print('\nГотово! В контакте:', contact, \
                          'сделана замена с:', contact_as_list[command - 1], 'на:', temp_data)
                    contact = contact.replace(contact_as_list[command - 1], temp_data)
                case 2:
                    return
        all_contacts_temp.append(contact)
    with open(file_name, 'w', encoding='utf8') as file:
        file.writelines(all_contacts_temp)

def remove_contact(file_name):
    with open(file_name, 'r', encoding='utf8') as file:
        all_contacts = file.readlines()
    print('\nВыберете критерий для удаления контакта:\
        \n 1 - Фамилия\
        \n 2 - Имя\
        \n 3 - Телефон')
    command = int(input())
    print('\nВведите данные для удаления')
    data = input()
    for contact in all_contacts:
        contact_as_list = contact.strip().split()
        if data in contact_as_list[command - 1]:
            print('\nУдалить контакт:', contact, 'Вы уверены ?\
            \n 1 - Да, удалить\
            \n 2 - Нет, оставить')
            temp = int(input())
            match temp:
                case 1:
                    print('\nУдален контакт:', contact)
                    all_contacts.remove(contact)
                case 2:
                    return
    with open(file_name, 'w', encoding='utf8') as file:
        file.writelines(all_contacts)