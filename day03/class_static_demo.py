class MyClass:
    def __init__(self, value):
        self.value = value

    def get_value(self):
        return self.value


# Create an instance of MyClass
obj = MyClass(10)

# Call the get_value method on the instance
print(obj.get_value())  # Output: 10


class ClassWithStatic:
    def __init__(self, value):
        self.value = value

    @staticmethod
    def get_max_value(x, y):
        return max(x, y)


# Create an instance of MyClass
obj = ClassWithStatic(10)

print(ClassWithStatic.get_max_value(20, 30))

print(obj.get_max_value(20, 30))
