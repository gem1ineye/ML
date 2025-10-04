import struct

# Function to add player record in binary file
def add(id, name):
    with open('Python-Rev/projects/players.dat', 'ab') as file:
        # Convert name to bytes → fixed size of 10 bytes (padded with spaces if shorter)
        name = name.encode().ljust(10)
        
        # pack() converts Python values → binary data
        # 'i10s' means → int (4 bytes) + string of 10 bytes
        record = struct.pack('i10s', id, name)
        
        # write the binary record to file
        file.write(record)


# Function to search record by index (like array index)
def search(index):
    Record_Size = 14   # 4 bytes (int) + 10 bytes (string)
    
    with open('Python-Rev/projects/players.dat', 'rb') as file:
        # Move pointer to (index * record_size)
        file.seek(index * Record_Size)
        
        # Read exactly 1 record
        record = file.read(Record_Size)
        
        if record:
            # Unpack binary → Python values
            id, name = struct.unpack('i10s', record)
            print('id:', id, '\n', 'name:', name.decode().strip())
        else:
            print('No record Found')


# Adding players
add(27, 'Harshit')
add(30, 'Manan')
add(21, 'Dev')
add(20, 'Akash')

# Searching record
search(0)   # will give Harshit
search(1)   # will give Manan
search(3)   # will give Akash
