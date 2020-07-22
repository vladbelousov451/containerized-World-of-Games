
import random
import time
import Utils

def generate_sequence(difficulty):
    List_number = []
    for x in range(difficulty):
        Rand_number = random.randint(1 , 101 )
        List_number.append(Rand_number)
    print(List_number)
    time.sleep(0.7)
    Utils.Screen_cleaner()
    return  List_number

def get_list_from_user(difficulty):
    List_number = []
    for x in range(difficulty):
        Alerted_number = input("Please Print the number you see below:  ")
        List_number.append(Alerted_number)
    return  List_number


def is_list_equal( Generated_list , Alrted_list):
    if(Generated_list == Alrted_list):
        return True
    else:
        return False


def play( difficulty):
    print("Welcome to the Memory Game ")
    Generated_list = generate_sequence(difficulty)
    Alrted_list = get_list_from_user(difficulty)
    Answer = is_list_equal(Generated_list , Alrted_list)
    return Answer



