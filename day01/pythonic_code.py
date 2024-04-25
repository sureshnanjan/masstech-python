def variable_declaration():
    notPythonicVarName: str = "hai this is string"
    pythonic_var_name: str = "hai this is string, with pythonic code"
    a, b = 0, 1
    d, e = "data", 100
    f = "single variable"
    name: str = "variable with type, only work with python 3"


def looping_through_lists():
    # Bad Code (Not Pythonic Code)
    data = ["one", "two", "three"]
    for i in range(0, len(data)):
        print(data[i])
    # Pythonic Code
    data = ["one", "two", "three"]
    for val in data:
        print(val)
    # output from both code
    # one
    # two
    # three


def looping_through_list_with_index():
    # Bad Code (Not Pythonic Code)
    data = ["one", "two", "three"]
    for i in range(len(data)):
        print(f'{i}:{data[i]}')
    # Pythonic Code
    data = ["one", "two", "three"]
    for idx, val in enumerate(data):
        print(f'{idx}:{val}')
    # output from both code


def looping_list_backwards():
    # Bad Code (Not Pythonic Code)
    colors = ["red", "green", "blue", "black", "white"]
    for idx in range(len(colors) - 1, -1, -1):
        print(f"{colors[idx]}")
    # Pythonic Code
    colors = ["red", "green", "blue", "black", "white"]
    for color in reversed(colors):
        print(f"{color}")


def looping_over_two_collections():
    names = ["neelam", "rosy", "kali", "swetha"]
    colors = ["blue", "rose", "black", "white", "red", "green"]
    # Bad Code (Not Pythonic Code)
    n = min(len(names), len(colors))
    for idx in range(n):
        print(f'{names[idx]} --- {colors[idx]}')
    # Pythonic Code
    for name, color in zip(names, colors):
        print(f'{name} --- {color}')


def create_a_list_of_numbers():
    # Not Soo Good (Not so Pythonic Code)
    list_number = []
    for i in range(10):
        list_number.append(i)
    print(list_number)
    # Pythonic Code
    # List Comprehension
    list_number = [idx for idx in range(10)]
    print(list_number)


def looping_over_dictionary():
    '''
    Looping over a dictionary could be achieved much more elegantly by assigning the
    value as Key-Value pair in <key>, <val> pattern in a for in construct
    :return:
    '''
    color_map = {"neelam": "blue", "verde": "green", "kali": "black"}
    # Good Pythonic
    for key in color_map:
        print(f'{key} --- {color_map[key]}')
    # More Pythonic
    for key, val in color_map.items():
        print(f'{key} --- {val}')


def construct_dictionary_from_pairs():
    """

    :return:
    """
    names = ["scarlet", "verde", "neelam", "kali"]
    colors = ["red", "green", "blue", "black"]
    # Not So Pythonic
    d = {}
    for name, color in zip(names, colors):
        d[name] = color
    # More Pythonic Code
    d = dict(zip(names, colors))


def count_with_dictionary():
    """

    :return: None
    """
    colors = ["red", "green", "blue", "green", "red", "green"]
    # Not Soo Pythonic Code
    d = {}
    for color in colors:
        if color not in d:
            d[color] = 0
        d[color] += 1

    # Pythonic Code
    d = {}
    for color in colors:
        d[color] = d.get(color, 0) + 1
    # Another Pythonic Code
    from collections import defaultdict
    d = defaultdict(int)
    for color in colors:
        d[color] += 1


looping_through_lists()
