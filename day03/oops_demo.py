class BluePrint:
    def __init__(self, val1, val2):
        self.attribute1 = val1
        self.attribute2 = val2


copy1 = BluePrint(10, 20)
copy2 = BluePrint(30, 40)

print(copy1)
print(copy2)
print(BluePrint)
print(dir(copy1))
print(dir(copy2))
print(dir(BluePrint))


class BluePrintWithMethods():
    def __init__(self, value):
        self.attribute1 = value

    def user_defined_method(self):
        print(f"This instance has value:  {self.attribute1}")


class BluePrintWithClassAttributes():
    class_attribute = None

    def __init__(self, instance_value):
        self.attribute1 = instance_value
        if self.class_attribute:
            self.class_attribute += 1
        else:
            self.class_attribute = 1
    def __str__(self):
        return f"{self.attribute1} : {self.class_attribute}"


