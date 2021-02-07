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

persons_list = []
summory = []
debitors_list = []
creditors_list = []


members = int(input("Введите колличество участников:"))
for member in range(1, members+1):
    mem = Person(name=str(input('Введите имя участника:')),
                 contr=float(input('Введите взнос:')))
    persons_list.append(mem)

for mem in persons_list:
    summory.append(mem.contr)
middle = sum(summory)/members
print(middle)


for i in range(len(persons_list)):
    if persons_list[i].contr<middle:
        creditor = persons_list[i].contr
    else:
        debitor = persons_list[i].contr
    counter(debitor=debitor, creditor=creditor,middle=middle)




