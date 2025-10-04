def write_entry():
    entry = input('Write your entry: ') + '\n'
    with open('Python-Rev/Problems/journal.txt', 'a') as file:
        file.write(entry)

def read_all():
    with open('journal.txt', 'r') as file:
        print('\nAll Journal Entries:')
        print(file.read())

def search():
    keyword = input('Enter keyword to search: ')
    found = False
    with open('journal.txt', 'r') as file:
        for line in file:
            if keyword.lower() in line.lower():
                print(line.strip())
                found = True
    if not found:
        print('No matching entries.')

while True:
    print('\n== File Journal ==')
    print('1. Add Entry')
    print('2. Read All Entries')
    print('3. Search Entries')
    print('4. Exit')

    choice = input("Choose option (1-4): ")

    if choice == '1':
        write_entry()
    elif choice == '2':
        read_all()
    elif choice == '3':
        search()
    elif choice == '4':
        print('Goodbye!')
        break
    else:
        print('Invalid Choice')