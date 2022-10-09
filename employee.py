"""Employee pay calculator."""
"""ENTER YOUR SOLUTION HERE!"""

class Employee:
    def __init__(self, name, salary=0, wage=0, numOfHours=0, bonusCommision=0, contractCommision=0, numOfContracts=0):
        self.name = name
        self.salary = salary
        self.wage = wage
        self.numOfHours = numOfHours
        self.bonusCommision = bonusCommision
        self.contractCommision = contractCommision
        self.numOfContracts = numOfContracts

    def get_pay(self):
        pay = self.salary + (self.wage*self.numOfHours) + self.bonusCommision + (self.contractCommision*self.numOfContracts)
        return pay

    def __str__(self):
        if self.salary>0:
            if self.salary>0 and self.contractCommision>0:
                return f'{self.name} works on a monthly salary of {self.salary} and receives a commission for {self.numOfContracts} contract(s) at {self.contractCommision}/contract. Their total pay is {self.get_pay()}.'
            elif self.salary>0 and self.bonusCommision>0:
                return f'{self.name} works on a monthly salary of {self.salary} and receives a bonus commission of {self.bonusCommision}. Their total pay is {self.get_pay()}.'
            else:
                return f'{self.name} works on a monthly salary of {self.salary}. Their total pay is {self.get_pay()}.'

        if self.wage>0:
            if self.wage>0 and self.contractCommision>0:
                return f'{self.name} works on a contract of {self.numOfHours} hours at {self.wage}/hour and receives a commission for {self.numOfContracts} contract(s) at {self.contractCommision}/contract. Their total pay is {self.get_pay()}.'
            elif self.wage>0 and self.bonusCommision>0:
                return f'{self.name} works on a contract of {self.numOfHours} hours at {self.wage}/hour and receives a bonus commission of {self.bonusCommision}. Their total pay is {self.get_pay()}.'
            else:
                return f'{self.name} works on a contract of {self.numOfHours} hours at {self.wage}/hour. Their total pay is {self.get_pay()}.'



# Billie works on a monthly salary of 4000.  Their total pay is 4000.
billie = Employee('Billie',4000,0,0,0,0,0)

# Charlie works on a contract of 100 hours at 25/hour.  Their total pay is 2500.
charlie = Employee('Charlie',0,25,100,0,0,0)

# Renee works on a monthly salary of 3000 and receives a commission for 4 contract(s) at 200/contract.  Their total pay is 3800.
renee = Employee('Renee',3000,0,0,0,200,4)

# Jan works on a contract of 150 hours at 25/hour and receives a commission for 3 contract(s) at 220/contract.  Their total pay is 4410.
jan = Employee('Jan',0,25,150,0,220,3)

# Robbie works on a monthly salary of 2000 and receives a bonus commission of 1500.  Their total pay is 3500.
robbie = Employee('Robbie',2000,0,0,1500,0,0)

# Ariel works on a contract of 120 hours at 30/hour and receives a bonus commission of 600.  Their total pay is 4200.
ariel = Employee('Ariel',0,30,120,600,0,0)
