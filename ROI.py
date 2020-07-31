class ROI():
    def __inti__(self, property, allProperties):
        self.property = property
        self.allProperties = allProperties

    def addProperty(self, propName=''):
        if propName == '':
            propName = input("What do you want to call the property? ")
        else:
            while propName in self.allProperties and propName !='':
                print(f"You already have a property with that name.")
                propName = input("What do you want to call the property? ")
            self.allProperties[propName] = {}
            propAddress = input("What is the propterty address? ")
            self.allProperties[propName]['address'] = propAddress
        
        return 


    def morgage(self, propName):
        """
            This function sets all of the information needed to assess monthly morgage payments.
            requires a propName as a string

            M = P[r(1+r)^n/((1+r)^n)-1)]
                M = the total monthly mortgage payment.
                P = the principal loan amount.
                r = your monthly interest rate. Lenders provide you an annual rate so you’ll need to divide that figure by 12 (the number of months in a year) to get the monthly rate. If your interest rate is 5%, your monthly rate would be 0.004167 (0.05/12=0.004167)
                n = number of payments over the loan’s lifetime. Multiply the number of years in your loan term by 12 (the number of months in a year) to get the number of payments for your loan. For example, a 30-year fixed mortgage would have 360 payments (30x12=360)
        """
        if propName not in self.allProperties:
            self.addProperty(propName)
        else:
            propAsk = float(input("What is the asking price? $: "))
            self.allProperties[propName]['askingPrice'] = propAsk

            propDP = float(input("How much are you going to put as a down payment? $: "))
            self.allProperties[propName]['downPayment'] = propDP

            propMorgage = propAsk - propDP
            self.allProperties[propName]['beginMorgage'] = propMorgage
            yearInterest = (int(input("What is your interest rate? Only enter a whole number.")))/100
            self.allProperties[propName]['yearlyInterestRate'] = yearInterest
            monthInterest = yearInterest/12
            self.allProperties[propName]['monthlyInterestRate'] = monthInterest        
            payments = int((input("How many years is the loan?")))*12
            self.allProperties[propName]['totalPayments'] = payments
            monthlyMorgage = propMorgage(((monthInterest*(1 + monthInterest)**payments)/(((1+monthInterest)**payments)-1)))
            self.allProperties[propName]['monthlyMorgagePayments'] = monthlyMorgage
            print(f"The monthly morgage payments are going to be ${monthlyMorgage}")


    def income(self, propName=''):
        """
            This method calculates how much income the property GENERATES.
            it can accept propName as an input
        """
        while propName =='' or propName not in self.allProperties:
            if propName == '':
                propName = input("What is the name of the property?")
            else:
                print(f"{propName} is not currently in the list. Please add it then run 'income' again.")
                self.addProperty('')
        self.allProperties[propName]
        self.allProperties[propName]['rent'] = float(input("What is the total rent you expect to get on the property? $: "))
        self.allProperties[propName]['otherIncome'] = float(input("How much will you make on laundry, storage, etc.? $:"))
        self.allProperties[propName]['rentalIncome'] = rentalIncome = (self.allProperties[propName]['rent']) + (self.allProperties[propName]['otherIncome'])
        
        print(f"The current income on {propName} is {rentalIncome}")
        return self

    def expenses(self):
        while propName =='' or propName not in self.allProperties:
            if propName == '':
                propName = input("What is the name of the property?")
            else:
                print(f"{propName} is not currently in the list. Please add it then run 'income' again.")
                self.addProperty('')
        tax = float(input("What are the yearly taxes on the property? $"))/12
        insurace = float(input("What is the monthly insurace cost? $"))        
        utilities = 0.0
        while True:
            wantUtility = input("Do you need to put in cost of utilities? (y/n)").lower()
            if wantUtility == y:
                elec = float(input("What is the monthly electric bill? $"))
                waterSewage = float(input("What is the monthly water and sewage costs? $"))
                garbage = float(input("What is the monthly garbage costs? $"))
                heat = float(input("What is the monthly heating costs? $"))
                utilities = (elec + waterSewage + garbage + heat)
                break
            if wantUtility == 'n':
                break
            else:
                print("Please enter only y or n.")
                continue


    def cashFlow(self):
        while propName =='' or propName not in self.allProperties:
            if propName == '':
                propName = input("What is the name of the property?")
            else:
                print(f"{propName} is not currently in the list. Please add it then run 'income' again.")
                self.addProperty('')


    def findROI(self):
        while propName =='' or propName not in self.allProperties:
            if propName == '':
                propName = input("What is the name of the property?")
            else:
                print(f"{propName} is not currently in the list. Please add it then run 'income' again.")
                self.addProperty('')


def roiCash():
    prop = ROI({},{})
    While True:
        action = input("What do you want to do with the propterty?: \nAdd property \nFind morgage rate \nFind income \nAdd expenses \nCash flow \nFind ROI  \nQuit").lower()
        if action == 'add property':
            prop.addProperty()
            continue
        if action == 'find morgage rate':
            prop.morgage
            continue
        if action == 'find income':
            prop.income()
            continue
        if action == 'add expenses':
            prop.expenses()
            continue
        if action == 'find ROI':

            continue
        if action == 'quit':
            quit = input("Are you sure you want to quit? All data will be lost. (y/n)").lower()
            if quit == 'n':
                continue
            if quit =='y':
                break
            else:
                print("That was not acceptable. Sending you to the main menu.")
                continue        
        else:
            print("That is not an accpeted value. Please try again.")
            continue


