"""
Exercise 77: Refactoring Instance Methods Using a Static Method
"""


import datetime

class Diary():

    def __init__(self, birthday: datetime.date, chrismas: datetime.date) -> None:
        self.birthday = birthday
        self.chrismas = chrismas

# Reformat static method    
#    def show_birthday(self)-> str:
#       return self.birthday.strftime('%d-%b-%y') 
#
#
#    def show_chrismas(self)-> str:
#       return self.chrismas.strftime('%d-%b-%y') 

    @staticmethod
    def format_date(date: datetime.date) -> str:
        return date.strftime('%d-%b-%y')
        

    def show_birthday(self)-> str:
        return self.format_date(self.birthday)


    def show_chrismas(self)-> str:
        return self.format_date(self.chrismas)




my_diary = Diary(datetime.date(2022, 11, 28), datetime.date(2022, 12, 24));

print(my_diary.show_chrismas())
