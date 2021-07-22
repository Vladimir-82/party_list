from random import shuffle


class Person:
    def __init__(self, name, contr):
        self.name = name
        self.contr = contr

    def get_info(self):
        return self.name, self.contr


persons_list = []
summory = []
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

for mem in persons_list:
    if mem.contr < middle:
        creditors_list.append(mem)
    elif mem.contr > middle:
        debitors_list.append(mem)

while True:

    if debitors_list[0].contr - middle == middle - creditors_list[0].contr:
        print(creditors_list[0].name, 'должен', debitors_list[0].name, round(debitors_list[0].contr - middle, 2),
              'рублей')
        creditors_list[0].contr = middle
        debitors_list[0].contr = middle


    elif debitors_list[0].contr - middle > middle - creditors_list[0].contr:
        print(creditors_list[0].name, 'должен', debitors_list[0].name, round(middle - creditors_list[0].contr, 2),
              'рублей')
        debitors_list[0].contr = debitors_list[0].contr - (middle - creditors_list[0].contr)
        creditors_list[0].contr = middle

    else:
        print(creditors_list[0].name, 'должен', debitors_list[0].name, round(debitors_list[0].contr - middle, 2),
              'рублей')
        creditors_list[0].contr = creditors_list[0].contr + debitors_list[0].contr - middle
        debitors_list[0].contr = middle

    if debitors_list[0].contr == middle:
        del debitors_list[0]
    if creditors_list[0].contr == middle:
        del creditors_list[0]

    if len(debitors_list) < 1 or len(creditors_list) < 1:
        break
