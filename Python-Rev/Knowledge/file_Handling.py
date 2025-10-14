# Open file in read mode ('r')
file = open('Python-Rev/data.txt', 'r')      #Creating file object

# Read entire file content as a single string
data = file.read()
print(data)

# Always close file after use (to free system resources)
file.close()

'''
r: read
w: write
r+ : read and write
w+: write and read
a: append
a+: append and read
x: write in a new file only  if there already that file then it will throw an error
rb: read a binary file
wb: write binary file
ab: append binary

'''


# ---------------- W mode ----------------
# 'w' = write mode → creates new file or overwrites existing one
file1 = open('Python-Rev/data.txt', 'w')
st = ' sending it to file'
file1.write(st)
file1.close()


# ---------------- A mode ----------------
# 'a' = append mode → adds content at the end of the file
file1 = open('Python-Rev/data.txt', 'a')
st = ' adding adding'
file1.write(st)
file1.close()


# ---------------- R+ mode ----------------
# 'r+' = read + write → file must already exist
file1 = open('Python-Rev/data.txt', 'r+')
data = file1.read()       # read existing content
st = '  testing r+'       # write new content (cursor will be at end after read)
file1.write(st)
file1.close()


# ---------------- W+ mode ----------------
# 'w+' = write + read → creates new file or clears existing content
file1 = open('Python-Rev/data.txt', 'w+')
st = ' send with w+'
file1.write(st)

# move cursor back to start (0,0) to read again
file1.seek(0, 0)
dat1 = file1.read()
print(dat1)

file1.close()

#File Operation

# ---------- Reading from file ----------
f = open('Python-Rev/sample.txt', 'r')

dat = f.read(5)           # Reads first 5 characters
print(dat)

f.seek(0, 0)              # Move cursor to beginning
dat1 = f.read(8)          # Reads first 8 characters
print(dat1)

f.seek(0, 0)              # Reset cursor to start again
dat2 = f.readlines()      # Reads all lines into a list
print(dat2)

f.close()


# ---------- Writing to file ----------
f = open('Python-Rev/sample.txt', 'w')

# writelines() writes a list of strings (each must end with \n if you want line breaks)
f.writelines(['one\n', 'two\n', 'Three'])


f.seek(0,0)

# truncate() cuts off content (if no size given, it cuts at current cursor position)
f.truncate()

f.close()
