from dynamic import sum_to_n  

"""
Exercise 52: Summing Integers
"""
sum_to_n(10000)
sum_to_n(10000)

"""
Activity 11: The Fibonacci Function with Recursion
"""
def fibonacci_recursive(n):
    if n == 0 or n == 1:
        return n
    else: 
        return fibonacci_recursive(n - 2) + fibonacci_recursive(n - 1) 

#print(fibonacci_recursive(3))        

"""
Exercise 51: Factorials with Iteration and Recursion
"""

def factorial_recursive(n):
    if n == 1:
        return 1
    else:
        return n * factorial_recursive(n - 1)


def factorial_iterative(n):
    result = 1;
    for i in range(n):
        result = result * (i + 1)

    return result 


#print(factorial_iterative(5))
#print(factorial_recursive(5))

"""
Exercise 50: Recursive Countdown
"""

def countdown(n):
    if n == 0:
        print("End")
    else: 
        print(n)
        countdown(n -1)

#countdown(7)

"""
Activity 10: Formatting customer names"
"""

def fibonacci_iterative(n):
   
    previus = 0
    current = 1
    print(previus, end= ", ")
    print(current, end= ", ")
    for _ in range(1, n):
        current_old = current;
        current = previus + current
        previus = current_old
        print(current, end=", ")
    print()
    return current

#fibonacci_iterative(3)

"""
Activity 9: Formatting customer names"
"""
def format_customer(first_name, last_name, location=None):
     full_name = f"{first_name} {last_name}"
     if location:
         return f"{full_name} ({location})"
     else:
         return full_name

#print(format_customer("John", "Smith"))
#print(format_customer("John", "Doe", location="Bogota"))


"""
Using **kwargs"
"""
def convert_usd_to_pesos(amount, rate=0.75):
    return amount / rate
    

def convert_and_sum_list(usd_list, **kwargs):

    total = 0
    for amount in usd_list:
       total += convert_usd_to_pesos(amount, **kwargs)
    return total

#print(convert_and_sum_list([1, 3]))
#print(convert_and_sum_list([1, 3], rate=0.8))

"""
Example binary search"
"""
def binary_search():
    l = [2, 3, 5, 8, 11, 12, 18]
    search_for = 11
    
    slice_start = 0
    slice_end = len(l) - 1 
    found = False
    while slice_start <= slice_end and not found:
        location = (slice_start + slice_end) // 2
        print("Location   : ", location)
        print("slice_start: ", slice_start)
        print("slice_end  : ", slice_end)
        if l[location] == search_for:
            found = True
        else:
            if search_for < l[location]:
                slice_end = location - 1
            else:
                slice_start = location + 1


