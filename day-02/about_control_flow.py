"""
Sequential - default mode
Selection - used for decisions and branching
Repetition - used for looping, i.e., repeating a piece of code multiple times.
"""
## This is a Sequential statement
a = 20
b = 10
c = a - b
print("Subtraction is : ", c)

'''
if
if-else
nested if
if-elif-else
'''
if a:
    print(f"The name 'a' has Value {a}")


def demo_if_else():
    n = 5
    if n % 2 == 0:
        print("n is even")
    else:
        print("n is odd")


def demo_if():
    n = 10
    if n % 2 == 0:
        print("n is an even number")


def demo_nested_if():
    a = 20
    b = 10
    c = 15
    if a > b:
        if a > c:
            print("a value is big")
        else:
            print("c value is big")
    elif b > c:
        print("b value is big")
    else:
        print("c is big")


def demo_elif():
    x = 15
    y = 12
    if x == y:
        print("Both are Equal")
    elif x > y:
        print("x is greater than y")
    else:
        print("x is smaller than y")


def demo_for_loop():
    print("1st example")
    lst = [1, 2, 3]
    for i in range(len(lst)):
        print(lst[i], end=" \n")
    print("2nd example")
    for j in range(0, 5):
        print(j, end=" \n")


def demo_while_loop():
    m = 5
    i = 0
    while i < m:
        print(i, end=" ")
        i = i + 1
    print("End")


def demo_list_comprehension():
    """
    new_list = [ expression(element) for element in oldList if condition ]
    :return:
    """
    numbers = [12, 13, 14, ]
    doubled = [x * 2 for x in numbers]
    filtered_doubled = [x * 2 for x in numbers if x % 2 == 0]
    print(doubled)
    # print(filtered_doubled)
    matrix = [[j for j in range(3)] for i in range(3)]
    # print(matrix)

    lis = ["Even number" if i % 2 == 0
           else "Odd number" for i in range(8)]
    # print(lis)

    names = ["G", "G", "g"]
    ages = [25, 30, 35]
    person_tuples = [(name, age) for name, age in zip(names, ages)]
    print(person_tuples)

    # Explicit function
    def digit_sum(n):
        dsum = 0
        for ele in str(n):
            dsum += int(ele)
        return dsum

        # Initializing list

    List = [367, 111, 562, 945, 6726, 873]

    # Using the function on odd elements of the list
    new_list = [digit_sum(i) for i in List if i & 1]

    # Displaying new list
    print(new_list)


def demo_dictionary_comprehension():
    # Lists to represent keys and values
    keys = ['a', 'b', 'c', 'd', 'e']
    values = [1, 2, 3, 4, 5]

    # but this line shows dict comprehension here
    myDict = {k: v for (k, v) in zip(keys, values)}

    # We can use below too
    # myDict = dict(zip(keys, values))

    print(myDict)
