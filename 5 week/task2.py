class name:
    def __init__(self, first_name, last_name, full_name):
        self.first_name = first_name.capitalize()
        self.last_name = last_name.capitalize()
        self.full_name = full_name.title()


f_name = input('Enter the first name: ')
l_name = input('Enter the last name: ')
c = [f_name, l_name]
fullname = ''
for i in c:
    fullname += i + ' '
person = name(f_name, l_name, fullname)
print(person.first_name)
print(person.last_name)
print(person.full_name)
