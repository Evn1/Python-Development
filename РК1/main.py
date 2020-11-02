from operator import itemgetter


class Computer:
    """Компьютеры"""

    def __init__(self, identifier, model, price, disp_class_identifier):
        self.identifier = identifier
        self.model = model
        self.price = price
        self.disp_class_identifier = disp_class_identifier


class DisplayClass:
    """Дисплейные классы"""

    def __init__(self, identifier, number):
        self.identifier = identifier
        self.number = number


class ComputerDisplayClass:
    """Связь многие ко многим"""

    def __init__(self, identifier, comp_identifier, disp_class_identifier):
        self.identifier = identifier
        self.comp_identifier = comp_identifier
        self.disp_class_identifier = disp_class_identifier


List_Computers = [
    Computer(1, "Apple", 80000, 3),
    Computer(2, "Acer", 30000, 1),
    Computer(3, "DELL", 35000, 4),
    Computer(4, "HP", 25000, 2),
    Computer(5, "Lenovo", 25000, 2),
    Computer(6, "Alienware", 70000, 3),
    Computer(7, "ASUS", 45000, 1),
    Computer(8, "MSI", 50000, 4),
]

List_DisplayClasses = [
    DisplayClass(1, "A100"),
    DisplayClass(2, "B200"),
    DisplayClass(3, "C300"),
    DisplayClass(4, "D400"),
]

List_Computers_DisplayClasses = [
    ComputerDisplayClass(1, 1, 3),
    ComputerDisplayClass(2, 2, 1),
    ComputerDisplayClass(3, 3, 4),
    ComputerDisplayClass(4, 4, 2),
    ComputerDisplayClass(5, 5, 2),
    ComputerDisplayClass(6, 6, 3),
    ComputerDisplayClass(7, 7, 1),
    ComputerDisplayClass(8, 8, 4),
    ComputerDisplayClass(9, 1, 4),
    ComputerDisplayClass(10, 2, 3),
    ComputerDisplayClass(11, 3, 2),
    ComputerDisplayClass(12, 4, 1),
]

if __name__ == '__main__':
    one_to_many = [(c.model, c.price, dc.number)
                   for dc in List_DisplayClasses
                   for c in List_Computers
                   if c.disp_class_identifier == dc.identifier
                   ]

    many_to_many_temp = [(dc.number, c_dc.comp_identifier)
                         for dc in List_DisplayClasses
                         for c_dc in List_Computers_DisplayClasses
                         if dc.identifier == c_dc.disp_class_identifier
                         ]

    many_to_many = [(number, c.model, c.price)
                    for number, comp_identifier in many_to_many_temp
                    for c in List_Computers
                    if c.identifier == comp_identifier
                    ]

    print("Задание №1")
    res = list(filter(lambda x: x[2].startswith("A"), one_to_many))
    for i in res:
        print(i)

    print("Задание №2")
    res = []
    for dc in List_DisplayClasses:
        comps = list(filter(lambda y: (y[2] == dc.number), one_to_many))
        if len(comps) > 0:
            prices = [price for _, price, _ in comps]
            prices_max = max(prices)
            res.append((dc.number, prices_max))
    res = sorted(res, key=itemgetter(1), reverse=True)
    for i in res:
        print(i)

    print("Задание №3")
    res = sorted(many_to_many, key=itemgetter(2))
    for i in res:
        print(i)
