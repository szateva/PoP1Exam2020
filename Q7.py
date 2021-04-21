""" Provide the implementation of three classes Person, Adult, Child that fullls the
following requirements. First, the classes must have the constructors as below:
class constructor functionality
Person sets the two given strings as the first and last names
Adult sets the two given strings as the first and last names,
and the third given string as the phone number
Child sets the two given strings as the first and last names,
and the two given Person objects as first and second parents
Second, the following methods must be present:
class method name functionality
Person get_info returns a string containing the first and the last names
separated by space
get_name returns a tuple containing the strings of the first and last name
Adult get_info same as for Person above
get_name same as for Person above
get_phone returns the phone number as a string
Child get_info returns a string containing the first and last names of the child,
then first and last names of first parent,
then first and last names of second parent,
all words separated by space
get_name same as for Person above
get_parents returns a tuple of two Person objects,
where the first is first parent and the second is second parent
Brevity, minimal repetition of code, and use of inheritance, is important for marking.
Provide full implementation of the three classes and their methods. For any of the
classes, do NOT provide methods or constructors other than listed above.
Indicative test cases:
p = Person("Mary", "Ann")
a = Adult("John", "Doe", "1234567")
c = Child("Richard", "Doe", p, a)
a.get_info()== "John Doe" #must be True
c.get_name()==("Richard", "Doe") #must be True
c.get_info()== "Richard Doe Mary Ann John Doe" #must be True
c.get_parents() == (p,a) #must be True """


class Person:
    def __init__(self, fname, lname):
        self.first_name = fname
        self.last_name = lname

    def get_info(self):
        return "" + self.first_name + " " + self.last_name

    def get_name(self):
        name = (self.first_name, self.last_name)
        return name


class Adult(Person):
    def __init__(self, fname, lname, p_no):
        super().__init__(fname, lname)
        self.phone_no = p_no

    def get_phone(self):
        PNo = self.phone_no
        return PNo

class Child(Person):
    def __init__(self, fname, lname, parent1, parent2):
        super().__init__(fname, lname)
        self.first_parent = parent1
        self.second_parent = parent2
    def get_info(self):
        return "" + self.first_name + " " + self.last_name + " " + self.first_parent.first_name + " " + self.first_parent.last_name + " " + self.second_parent.first_name +" " + self.second_parent.last_name

    def get_parents(self):
        parents = (self.first_parent, self.second_parent)
        return parents


p = Person("Mary", "Ann")
a = Adult("John", "Doe", "1234567")
c = Child("Richard", "Doe", p, a)
print(a.get_info() == "John Doe")
print("must be True")
print(c.get_name() == ("Richard", "Doe"))
print("must be True")
print(c.get_info() == "Richard Doe Mary Ann John Doe")
print("must be True")
print(c.get_parents() == (p, a))
print("must be True")
