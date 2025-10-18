'''
-----------------------------------------
🧠 Concept Recap:
-----------------------------------------
Uni-tasking → System executes only one task at a time.
               Example: Old DOS systems (run one program, then another).

Multitasking → CPU switches quickly between multiple tasks,
               creating an illusion of parallel execution.
               Example: Running browser + music player simultaneously.

Multithreading → A single program (process) runs multiple threads concurrently.
                 Threads share the same memory space.
                 Example: A browser — one thread for UI, another for loading,
                 another for video playback.
-----------------------------------------
'''

# -----------------------------------------
# Ways of Implementing Multithreading
# -----------------------------------------
# ✅ 1. By defining a function and passing it to Thread(target=function)
# ✅ 2. By extending the Thread class and overriding its run() method

from threading import *

# -----------------------------------------
# (1) Function-based Multithreading
# -----------------------------------------
def dis():
    # Function to print uppercase alphabets (A–Z)
    for i in range(65, 91):
        print(chr(i))

# Creating a thread and assigning target function
t = Thread(target=dis, name='Alphabets')

# Start thread execution (runs 'dis()' concurrently)
t.start()

# Wait for thread 't' to finish before continuing main thread
t.join()

# Main thread now prints ASCII codes for A–Z
for i in range(65, 91):
    print(i)


# -----------------------------------------
# (2) Class-based Multithreading
# -----------------------------------------
class Alpha(Thread):         # Inherit from Thread class
    def run(self):
        # run() method executes automatically when thread starts
        for i in range(65, 91):
            print(chr(i))

# Create thread object
t1 = Alpha()

# Start execution (calls run() internally)
#t1.start()


from threading import Thread, Lock

# -----------------------------------------
# Thread function with Lock for synchronization
# -----------------------------------------
def fun(arg):
    # Acquire the lock before entering critical section
    l.acquire()
    try:
        # Print each character from the string argument
        for i in arg:
            print(i, end='')   # end='' prevents extra newlines
        print()  # move to next line after printing one string
    finally:
        # Always release lock (even if an error occurs)
        l.release()


# Create a Lock object (used for synchronizing threads)
#l = Lock()
l=Semaphore(2)

# Creating threads and passing arguments (note the comma in args tuple)
t2 = Thread(target=fun, args=('HELLO WORLD',))
t3 = Thread(target=fun, args=('doma is og bhai',))

# Start both threads
t2.start()
t3.start()

# Wait for both threads to complete
t2.join()
t3.join()


# The difference between semaphore and mutex is mutex. 
# only allow one at a time while in sempahore we can assign how much thread we allowed in one go.
'''
Mutex → 1 thread at a time.
Semaphore → N threads at a time.
'''  