from lib_func import *

def show_menu():
    while True:
        print('1. Add Book')
        print('2. View Books')
        print('3. Search Book by ID')
        print('4. Delete Book')
        print('5. Exit')
        choice=input('Enter your choice from 1-5')
    
        if choice=='1':
            add_book()
        elif choice=='2':
            view_books()
        elif choice=='3':
            search_books()
        elif choice=='4':
            delete_book()
        elif choice=='5':
            break
        else:
            print('Invalid choice')

if __name__=="__main__":
    show_menu()
    
          