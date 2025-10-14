import pickle

# -----------------------------------------
# Student Class Definition
# -----------------------------------------
class Student:
    def __init__(self, id, name, no):
        # Initialize student attributes
        self.stu_id = id
        self.name = name
        self.marks = no

    def __repr__(self):
        # Custom string representation for displaying object details
        return f"{self.name} ({self.stu_id}) - Marks: {self.marks}"


# -----------------------------------------
# Function to Save (Serialize) Student Data
# -----------------------------------------
def sav(student_list, filename='Python-Rev/Problems/student.pkl'):
    """
    ✅ Saves (pickles) a list of Student objects to a binary file.
    - 'wb' → write in binary mode.
    - pickle.dump() → converts objects into binary format.
    """
    with open(filename, 'wb') as file:
        pickle.dump(student_list, file)
    print(f"✅ Student data saved successfully to {filename}")


# -----------------------------------------
# Function to Load (Deserialize) Student Data
# -----------------------------------------
def load_stu(filename='Python-Rev/Problems/student.pkl'):
    """
    ✅ Loads (unpickles) data back into Python objects.
    - 'rb' → read in binary mode.
    - pickle.load() → converts binary data back into Python objects.
    """
    with open(filename, 'rb') as file:
        data = pickle.load(file)
        return data


# -----------------------------------------
# Object Creation and Testing
# -----------------------------------------

# Creating student objects
s1 = Student('S001', 'Harshit', {'Maths': 94, 'English': 68})
s2 = Student('S002', 'Ronit',   {'Maths': 55, 'English': 98})
s3 = Student('S003', 'Manoj',   {'Maths': 14, 'English': 78})

# List of Student objects
Students = [s1, s2, s3]

# Saving all student records to file
sav(Students)

# Loading student records back from file
loaded_students = load_stu()

# Displaying loaded student data
print('\n📚 Student Records:')
for x in loaded_students:
    print(x)
