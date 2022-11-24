from datetime import datetime
import time

"""
Exercise 61: Working with Incorrect Parameters to Find the Average Using
Assert with Functions
"""

def avg(marks):
    assert len(marks) != 0
    return round(sum(marks)/len(marks), 2)

sem1_marks = [62, 65, 75]
print("Average marks for semester 1:" ,avg(sem1_marks))

ranks = []
print("Average of marks for semester 1:",avg(ranks))

"""
Exercise 60: Creating and Writing Content to Files to Record the Date and
Time in a Text File
"""
def open_and_write_file():
    f = open('/home/spawn/tmp/log.txt', 'w')
    for i in range(0,10):
        print(datetime.now().strftime('%Y%m%d_%H:%M:%S - '),i)
        f.write(datetime.now().strftime('%Y%m%d_%H:%M:%S - '))
        time.sleep(1)
        f.write(str(i))
        f.write("\n")
    f.close()


"""
Exercise 59: Reading Partial Content from a Text File

"""

def read_file():
    with open("/home/spawn/tmp/pg37431.txt") as f:
        #print(f.read(5)) # Read 5 characters
        #print(f.readline()) # Read one line
        for line in f:
            print(line)


"""
Exercise 58: Reading a Text File Using Python
"""

# f = open('/home/spawn/tmp/pg37431.txt')
# text = f.read()

