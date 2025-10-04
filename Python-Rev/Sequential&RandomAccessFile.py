# Reading file in binary mode (important for random access)
with open('Python-Rev/data.txt', 'rb') as file:
    # Read first 4 bytes
    print(file.read(4))      # Output will be in bytes, e.g. b'data'
    
    # Current cursor position
    print(file.tell())       # → 4 (since we already read 4 bytes)
    
    #seek(offset,whence) 
    # (offset means how much pointer upu have to move, whence from where you start the pointer)
    
    # -------------------------------
    # seek(offset, whence)
    # offset → how many bytes to move
    # whence → from where to start
    #    0 → from start of file
    #    1 → from current cursor position
    #    2 → from end of file
    # -------------------------------
    
    # Move cursor to position 3 (from start)
    file.seek(3, 0)
    print('\n', file.read(2))   # Read 2 bytes starting at position 3
    
    # Move cursor 4 bytes before end of file
    file.seek(-4, 2)
    print(file.read(2))         # Read 2 bytes near the end
