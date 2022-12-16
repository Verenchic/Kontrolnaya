#17
class Worker:
    def __init__(self, name, surname, rate, days):
        self.__name = name
        self.__surname = surname
        self.__rate = rate
        self.__days = days

    def getSalary(self):
        return self.__rate * self.__days

    def getInformation(self):
        return 'Name: {}\nSurname: {}\nRate: {}\nDays:{}'.format(self.__name, self.__surname, self.__rate, self.__days)


worker_first = Worker('Argus', 'Ford', 25, 21)
worker_second = Worker('Sugra', 'Drof', 52, 12)
amount_of_salaries = worker_first.getSalary() + worker_second.getSalary()
print('Сумма зарплат двух работиков: {}'.format(amount_of_salaries))




