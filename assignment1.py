##########################################
## CE151 ASSIGNMENT 1: DO NOT REMOVE    ##
##########################################
import unittest


##########################################
## CE151 ASSIGNMENT 1: DO NOT REMOVE    ##
##########################################

#### Exercise 1
def fun_exercise_1(x, y):
    if x == 0:
        sum = 0
        for num in y:
            sum += num
        return sum
    elif x % 2 == 0:
        sum = 0
        for num in y:
            sum += num * 2
        return sum
    else:
        sum = 0
        for num in y:
            sum += num - 1
        return sum


#### Exercise 2
def fun_exercise_2(y):
    if y[0] % 2 == 1:
        prod = 1
        for num in y:
            prod = prod * (num * 2)
        return prod
    elif y[2] % 2 == 1:
        sum = 0
        for num in y:
            sum += num / 2
        return sum
    else:
        sum = 0
        for num in y:
            sum += num ** 2
        return sum


#### Exercise 3
def fun_exercise_3(y):
    z = []
    for i in range(len(y)//2):
        if y[-i-1] < y[i]:
            z.append(True)
        else:
            z.append(False)
    return z

#### Exercise 4
def fun_exercise_4(y):
    y.sort()
    list_len = len(y)
    if list_len == 0:
        return None
    elif list_len < 5:
        len_to_use = list_len - 2
        return y[len_to_use]
    else:
        return y[-3]


#### Exercise 5
def fun_exercise_5(x):
    word = x.lower()
    word_reversed = word[-1::-1]
    is_palindrome = word == word_reversed
    if is_palindrome:
        return False
    else:
        return True


#### Exercise 6
def fun_exercise_6(x):
    ascii_m = 109
    ascii_z = 122

    char_list = []

    for index in range(0, len(x)):
        is_char_added = False

        for ascii_num in range(ascii_m, ascii_z + 1):
            if x[index] == chr(ascii_num):
                # Uppercase ASCII = Lowercase ASCII - 32
                char_to_add = chr(ascii_num - 32)
                char_list.append(char_to_add)
                is_char_added = True

        if not is_char_added:
            char_to_add = x[index]
            char_list.append(char_to_add)

    string_to_return = "".join(char_list)

    return string_to_return

#### Exercise 7
def fun_exercise_7(x):
    for word in x:
        for second_word in x:
            if word in second_word and word != second_word:
                return x.index(word)
    return -1


#### Exercise 8
def fun_exercise_8(x):
    all_characters = { }
    for char in x:
        if char in all_characters:
            all_characters[char] += 1
        else:
            all_characters[char] = 0
    value_list = list(all_characters.values())
    value_list.sort()
    second_most_char = value_list[-2]
    for key, value in all_characters.items():
        if value == second_most_char:
            return key




##############################################
## BEGIN: CE151 TEST CODE: DO NOT REMOVE    ##
##############################################
class TestAssignment1(unittest.TestCase):

    # function 1
    def test1_exercise_1(self):
        self.assertTrue(fun_exercise_1(3, [4, 2, 3]) == 6)

    def test2_exercise_1(self):
        self.assertTrue(fun_exercise_1(2, [2, 3, 4]) == 18)

    def test3_exercise_1(self):
        self.assertTrue(fun_exercise_1(0, [5, 3, 2]) == 10)

    def test4_exercise_1(self):
        self.assertTrue(fun_exercise_1(3, [1, 1, 1]) == 0)

    # function 2
    def test1_exercise_2(self):
        self.assertTrue(fun_exercise_2([3, 2, 4]) == 192)

    def test2_exercise_2(self):
        self.assertTrue(fun_exercise_2([6, 2, 3]) == 5.5)

    def test3_exercise_2(self):
        self.assertTrue(fun_exercise_2([6, 5, 4]) == 77)

    def test4_exercise_2(self):
        self.assertTrue(fun_exercise_2([1, 2, 3]) == 48)

    # function 3 *****
    def test1_exercise_3(self):
        self.assertTrue(fun_exercise_3([2, 3, 4, 5, 6, 7]) == [False, False, False])

    def test2_exercise_3(self):
        self.assertTrue(fun_exercise_3([6, 4, 3, 2, 1, 0]) == [True, True, True])

    def test3_exercise_3(self):
        self.assertTrue(fun_exercise_3([6, 5, 4, 2]) == [True, True])

    def test4_exercise_3(self):
        self.assertTrue(fun_exercise_3([1, 2, 3, 4]) == [False, False])

    # function 4
    def test1_exercise_4(self):
        self.assertTrue(fun_exercise_4([5, 3, 4, 2, 6]) == 4)

    def test2_exercise_4(self):
        self.assertTrue(fun_exercise_4([3, 2, 6]) == 3)

    def test3_exercise_4(self):
        self.assertTrue(fun_exercise_4([]) == None)

    def test4_exercise_4(self):
        self.assertTrue(fun_exercise_4([2, 3, 4, 7, 6, 5]) == 5)

    # function 5
    def test1_exercise_5(self):
        self.assertTrue(fun_exercise_5("osso") == False)

    def test2_exercise_5(self):
        self.assertTrue(fun_exercise_5("goat") == True)

    def test3_exercise_5(self):
        self.assertTrue(fun_exercise_5("Mom") == False)

    def test4_exercise_5(self):
        self.assertTrue(fun_exercise_5("boat") == True)

    # function 6
    def test1_exercise_6(self):
        self.assertTrue(fun_exercise_6("osso") == "OSSO")

    def test2_exercise_6(self):
        self.assertTrue(fun_exercise_6("goat") == "gOaT")

    def test3_exercise_6(self):
        self.assertTrue(fun_exercise_6("bag") == "bag")

    def test4_exercise_6(self):
        self.assertTrue(fun_exercise_6("boat") == "bOaT")

    # function 7
    def test1_exercise_7(self):
        list1 = ["goat"]
        ptr = fun_exercise_7(list1)
        self.assertTrue(ptr == -1)

    def test2_exercise_7(self):
        list1 = ["soul", "soulmate", "origin"]
        ptr = fun_exercise_7(list1)
        self.assertTrue(ptr == 0)

    def test3_exercise_7(self):
        list1 = ["FASER", "submission", "online", "drive", "frequent"]
        ptr = fun_exercise_7(list1)
        self.assertTrue(ptr == -1)

    def test4_exercise_7(self):
        list1 = ["banana", "applejuice", "kiwi", "strawberry", "apple", "peer"]
        ptr = fun_exercise_7(list1)
        self.assertTrue(ptr == 4)

    # function 8
    def test1_exercise_8(self):
        self.assertTrue(fun_exercise_8("GTTAAA") == "T")

    def test2_exercise_8(self):
        self.assertTrue(fun_exercise_8("unforeseen") == "n")

    def test3_exercise_8(self):
        self.assertTrue(fun_exercise_8("developed") == "d")

    def test4_exercise_8(self):
        self.assertTrue(fun_exercise_8("circumstances") == "s")


if __name__ == '__main__':
    unittest.main()
##############################################
## END: CE151 TEST CODE: DO NOT REMOVE      ##
##############################################
