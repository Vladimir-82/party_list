from random import shuffle


class Person:
    def __init__(self, name, contr):
        self.name = name
        self.contr = contr

    def get_info(self):
        return self.name, self.contr

    def counter(self, middle):
        pass
        # if self.contr - middle > middle - self.contr:


summory = []

persons_list = []

members = int(input("Введите колличество участников:"))
for member in range(1, members + 1):
    mem = Person(name=str(input('Введите имя участника:')),
                 contr=float(input('Введите взнос:')))
    persons_list.append(mem)

for mem in persons_list:
    summory.append(mem.contr)
middle = sum(summory) / members

print(mem.get_info())

# print(middle)

# for mem in persons_list:
#     if mem.contr < middle:
#         creditors_list.append(mem.contr)
#     elif mem.contr > middle:
#         debitors_list.append(mem.contr)
