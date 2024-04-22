def adder_factory(value_to_add):
    def adder(value_to_add_with):
        return value_to_add_with + value_to_add

    return adder


def salutor(salutation: str):
    def add_salutation(name: str):
        return salutation.capitalize() + ". " + name.capitalize()

    return add_salutation


tens_adder = adder_factory(10);
twentys_adder = adder_factory(20);
thousands_adder = adder_factory(1000)
mr_decorator = salutor("mr")
mrs_decorator = salutor("mrs")

#print("-" * tens_adder(1))
#print(tens_adder(100))
#print(tens_adder(200))
#print("-" * twentys_adder(1))
#print(twentys_adder(100))
#print(twentys_adder(200))

#print("*" * twens_adder(2))
print(mrs_decorator("Wife"))
print(mr_decorator("Husband"))
print(mr_decorator("Suresh"))
print(mrs_decorator("Lorem ipsum "))
