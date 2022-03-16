# Question number 1
def hello_name(user_name):
    print("Hello " + user_name.upper() + "!")

hello_name('USERNAME')



# Questions number 2
def first_odds():
    """
        Print all the odds numbers bewtweens 1-100.
    """

current_number = 0

while current_number < 100:
    if current_number % 2 == 1:
        print(current_number)
    current_number += 1



# Question number 3 
def max_num_in_list(a_list):
    """return largest number in a list"""

    max_number = max(a_list)
    return max_number

number_list = [12, 470,73,88,65,40]

def max_num_2(a_list):
    print(max_num_2(number_list))




# QAuestion 4: write functions that returns True if the given year is a leap year
def is_leap_year(a_year):
    num = a_year
    if num  % 400 ==0:
        print(True)
    elif num % 4 == 0 and num % num % 100!=0:
        print(False)

def leap_year_2(a_year):
    """return whether a given year is a leap year"""
    return a_year % 400== 0 or a_year % 4== 0 and a_year % 100 != 0

is_leap_year(2024)
print(leap_year_2(2000))



# Question number 5
def is_consecutive(a_list):
    status = True
    if len(a_list) >1:
        for number in range(len(a_list)):
            if a_list[number] == a_list[number + 1]:
                continue
            else:
                statues = False
            return status

print('is this consecutive: ',is_consecutive([1,2,3,5,6,7]))

def consecutive_2(a_list):
    return a_list == list(range(min(a_list), max (a_list)+1))

print(is_consecutive([2,3,4,5,6,7]))


