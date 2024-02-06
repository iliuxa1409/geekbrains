def work_with_phonebook():
    choice = choose_option()
    filename = 'phonebook.txt'
    phone_book = read_book(filename)
    while choice != 7:
        if choice == 1:  # display the phonebook
            for i in phone_book:
                print(', '.join(i.values()))
        elif choice == 2:   # find contact
            for i in find_contact(phone_book):
                print(i)
        elif choice == 3:   # add contact
            add_contact(filename, write_new_line())
        elif choice == 4:   # save in txt
            name = input("Input the name of the file without .txt extension: "
                         ).strip()
            save_book(name + '.txt', phone_book)
        elif choice == 5:  # change the information
            change(phone_book, filename)
        elif choice == 6:  # delete information
            delete_record(phone_book, filename)
        choice = choose_option()


def choose_option():
    print("Выберите одну из операций:\n"
          "1. Отобразить весь справочник\n"
          "2. Найти абонента\n"
          "3. Добавить абонента в справочник\n"
          "4. Сохранить справочник в текстовом формате\n"
          "5. Изменить информацию\n"
          "6. Удалить информацию\n"
          "7. Закончить работу")
    return int(input("Введите номер требующейся операции: "))


def read_book(file):
    phone_book = []
    fields = ['Surname', 'Name', 'Phone Number', 'Description']
    with open(file, 'r', encoding='utf-8') as f:
        for line in f:
            record = dict(zip(fields, line.strip().split(', ')))
            phone_book.append(record)
    return phone_book


def find_contact(book):
    while True:
        try:
            x = int(input("Search by:\n"
                          "1. Surname\n"
                          "2. Name\n"
                          "3. Phone Number\n"
                          "4. Description\n"
                          "5. I know something\n"
                          "6. Main menu\n"
                          "Please enter the number corresponding to your choice: "))
            if x not in range(1, 7):
                print("Invalid choice. Please enter a number between 1 and 6.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter a number.")

    if x == 1:
        return find_sur(book)
    elif x == 2:
        return find_name(book)
    elif x == 3:
        return find_num(book)
    elif x == 4:
        return find_descr(book)
    elif x == 5:
        return find_anything(book)
    elif x == 6:
        work_with_phonebook()


def find_sur(book):
    sur = input('Give me the Surname or part of it: ').lower()
    results = [i for i in book if sur in i['Surname'].lower()]
    if not results:
        return "Ooops, there's nothing like that"
    return results


def find_name(book):
    sur = input('Give me the Name or part of it: ')
    results = [i for i in book if sur in i['Name'].lower()]
    if not results:
        return "Ooops, there's nothing like that"
    return results


def find_num(book):
    sur = input('Give me the Phone Number or part of it: ')
    results = [i for i in book if sur in i['Phone Number']]
    if not results:
        return "Ooops, there's nothing like that"
    return results


def find_descr(book):
    sur = input('Give me the Description or part of it: ')
    results = [i for i in book if sur in i['Description'].lower()]
    if not results:
        return "Ooops, there's nothing like that"
    return results


def find_anything(book):
    sur = input('Give me the Phone Number or part of it: ')
    results = [i for i in book if sur in i.values()]
    if not results:
        return "Ooops, there's nothing like that"
    return results


def write_new_line():
    surname = input('Input the surname: ').upper()
    name = input('Input the name: ').upper()
    number = input('Input the phone number: ')
    descr = input('Input the description: ').title()
    new_line = f'{surname}, {name}, {number}, {descr}'
    return new_line


def add_contact(file, new_line):
    try:
        with open(file, 'r', encoding='utf-8') as f:
            lines = f.readlines()
    except FileNotFoundError:
        lines = []

    try:
        if new_line + '\n' not in lines:
            lines.append(new_line)
            with open(file, 'w', encoding='utf-8') as f:
                f.writelines(lines)
            print('Contact added successfully!')
        else:
            print('This contact already exists in the phonebook.')
    except Exception as e:
        print(f"An error occurred while adding the contact: {e}")


def save_book(filename, book):
    with open(filename, 'w', encoding='utf-8') as f:
        for i in book:
            f.write(', '.join(i.values()) + '\n')


def change(book, file):
    line = choose_one(book)
    for i in book:
        if i == line:
            if input('Do you want to change Surname') == 'y':
                i['Surname'] = input('New info: ').upper()
            if input('Do you want to change Name') == 'y':
                i['Name'] = input('New info: ').upper()
            if input('Do you want to change Phone Number') == 'y':
                i['Phone Number'] = input('New info: ')
            if input('Do you want to change Description') == 'y':
                i['Description'] = input('New info: ').lower()
    if input('The contact is changed for the session'
             'Do you want to delete it forever? y/n').lower() == 'y':
        save_book(file, book)


def choose_one(book):
    print("First of all, we need to find the contact")
    for rec in find_contact(book):
        print(rec)
        if input("Is it this one y/n").lower() == 'y':
            return rec
    return 'No such record, but you can start again'


def delete_record(book, file):
    line_del = choose_one(book)
    for record in book:
        if record == line_del:
            book.remove(record)
    if input('The contact is deleted for the session'
             'Do you want to delete it forever? y/n').lower() == 'y':
        save_book(file, book)


work_with_phonebook()
