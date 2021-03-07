class Employee:
    def __init__(self, value = None, childs = []):
        self.value, self.childs= value, childs
        self.f = self.g = -1 # f - employee idze, g - emplyee nie idzie

    def printer(self, depth):
        output = ""
        for i in range(depth):
            output += "- - - - "
        depth, output = depth + 1, output + "> " + str(self.value)
        print (output)
        if self.childs != None:
            for i in self.childs: i.printer (depth)
        return ""
    
    def __str__(self):
        return self.printer(0)

def f(employee):
    if employee.f >= 0: return employee.f
    myScore = employee.value
    for i in employee.childs: myScore += g(i)
    employee.f = max(myScore, g(employee))
    return employee.f

def g(employee):
    if employee.g >= 0: return employee.g
    employee.g = 0
    for i in employee.childs: employee.g += f(i)
    return employee.g

intern1, intern2, intern3 = Employee(5, []), Employee(1, []), Employee(2, [])
employee1, employee2, employee3 = Employee(10, [intern1]), Employee(2, [intern2, intern3]), Employee(5, [])
boss = Employee(10, [employee1, employee2, employee3])

print (boss)
print (max(f(boss), g(boss)))