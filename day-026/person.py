class Person():

    def __init__(self, first_name: str, last_name: str) -> None:
        self.first_name = first_name
        self.last_name = last_name

    #Exercise 79: The Full Name Property

    @property
    def full_name(self):
        return '%s %s' % (self.first_name, self.last_name)

    
    @full_name.setter
    def full_name(self, name: str) -> None:
        first, last = name.split(' ')
        self.first_name = first
        self.last_name = last


"""Exercise 81: Inheriting from the Person Class """

class Baby(Person):

    def speak(self):
        print('Blah blah blah blah blah')


class Adult(Person):

    def speak(self):
        print('Hello, my name is %s' % self.full_name)



class BetterPerson(Person):

    @property
    def full_name(self):
        return '%s %s' % (self.first_name, self.last_name)

    @full_name.setter
    def full_name(self, name: str)-> None:
        names = name.split(' ')
        self.first_name = names[0]
        if len(names) > 2:
            self.last_name = ' '.join(names[1:])
        elif len(names) == 2:
            self.last_name = names[1]


"""Exercise 82: Sub-Classing the datetime.date Class"""


customer = Person("John", "Doe")
print(customer.full_name)

customer.full_name = "Waylon Smithers"
print(customer.full_name)

tom = Baby('Maggie', 'Simpson')
homer = Adult('Homer', 'Simpson')
tom.speak()
homer.speak()

my_person = BetterPerson('Mary', 'Smith')
my_person.full_name = 'Mary Anne Smith'

print(my_person.first_name)
print(my_person.last_name)

import datetime

class MyDate(datetime.date):

    def add_days(self, n):
        return self + datetime.timedelta(n)


d = MyDate(2019, 12, 1)
print(d.add_days(40))
print(d.add_days(400))


class Calendar():

    def book_appointment(self, date):
        print('Booking appointment for date %s' % date)
        
class OrganizedAdult(Adult, Calendar):
    pass

class OrganizedBaby(Baby, Calendar):
    pass

andres = OrganizedAdult('Andres', 'Gomez')
boris = OrganizedBaby('Boris', 'Bumblebutton')
andres.speak()
boris.speak()
boris.book_appointment(datetime.date(2018,1,1))
