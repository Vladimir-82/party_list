from random import choice


class Person:
    def __init__(self, name, contr):
        self.name = name
        self.contr = contr

    def get_info(self):
        return self.name, self.contr


def counter(debitor, creditor, middle):
    if debitor - middle == middle - creditor:
        creditor = middle
        debitor = middle

    elif debitor - middle > middle - creditor:
        debitor = debitor - (middle - creditor)
        creditor = middle
    else:
        creditor = creditor + debitor - middle
        debitor = middle
    return debitor, creditor

# def counter(debitor, creditor, middle):
#     if debitor - middle == middle - creditor:
#         creditor = middle
#         debitor = middle
#
#     elif debitor - middle > middle - creditor:
#         debitor = debitor - (middle - creditor)
#         creditor = middle
#     else:
#         creditor = creditor + debitor - middle
#         debitor = middle
#     return debitor, creditor




summory = []

persons_list = []
debitors_list = []
creditors_list = []

members = int(input("Введите колличество участников:"))
for member in range(1, members + 1):
    mem = Person(name=str(input('Введите имя участника:')),
                 contr=float(input('Введите взнос:')))
    persons_list.append(mem)

for mem in persons_list:
    summory.append(mem.contr)
middle = sum(summory) / members
# print(middle)

# for mem in persons_list:
#     if mem.contr < middle:
#         creditors_list.append(mem.contr)
#     elif mem.contr > middle:
#         debitors_list.append(mem.contr)


# for i in range(len(persons_list)):
#     if persons_list[i].contr < middle:
#         print(persons_list[i].contr)
while persons_list.contr.count(middle) != len(persons_list):
    debitor = choice()
