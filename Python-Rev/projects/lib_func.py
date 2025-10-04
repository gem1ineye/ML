import struct

Record_size = 60   # Corrected size
file_name = 'Python-Rev/projects/lib.dat'

# pack record into binary
def pack_record(book_id, title, author, stock):
    title = title.strip().encode().ljust(30)
    author = author.strip().encode().ljust(20)
    return struct.pack('i30s20si', book_id, title, author, stock)

# unpack binary into dict
def unpack_record(record_byte):
    book_id, title, author, stock = struct.unpack('i30s20si', record_byte)
    return {
        'Book_id': book_id,
        'Title': title.decode().strip(),
        'Author': author.decode().strip(),
        'Stock': stock
    }

def add_book():
    book_id = int(input('Enter the book id: '))
    title = input('Enter Title: ')
    author = input('Enter Author: ')
    stock = int(input('Enter stock: '))

    record = pack_record(book_id, title, author, stock)
    with open(file_name, 'ab') as f:
        f.write(record)
    print('✅ Record successfully added')

def view_books():
    with open(file_name, 'rb') as f:
        print("\n====== Books Record ======")
        while True:
            record = f.read(Record_size)
            if not record:
                break
            book = unpack_record(record)
            print(book)

def search_books():
    book_id = int(input('Enter the book id: '))
    with open(file_name, 'rb') as f:
        while True:
            record = f.read(Record_size)
            if not record:
                break
            book = unpack_record(record)
            if book["Book_id"] == book_id:
                print('✅ Book Found:', book)
                return
    print('❌ Book Not Found')

def delete_book():
    book_id = int(input('Enter the book id to delete: '))
    found = False

    with open(file_name, 'r+b') as f:
        index = 0
        while True:
            f.seek(index * Record_size)
            record = f.read(Record_size)
            if not record:
                break
            book = unpack_record(record)
            
            if book["Book_id"] == book_id:
                # set stock = 0 to mark deleted
                book['Stock'] = 0
                f.seek(index * Record_size)
                f.write(pack_record(book['Book_id'], book['Title'], book['Author'], book['Stock']))
                found = True
                print("🗑️ Book deleted (stock set to 0)")
                break
            index += 1

    if not found:
        print("❌ Book not found")
