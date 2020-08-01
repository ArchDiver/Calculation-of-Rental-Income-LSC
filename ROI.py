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
        return propName



    def morgage(self, propName=''):
        """
            This function sets all of the information needed to assess monthly morgage payments.
            requires a propName as a string

            M = P[r(1+r)^n/((1+r)^n)-1)]
                M = the total monthly mortgage payment.
                P = the principal loan amount.
                r = your monthly interest rate. Lenders provide you an annual rate so you’ll need to divide that figure by 12 (the number of months in a year) to get the monthly rate. If your interest rate is 5%, your monthly rate would be 0.004167 (0.05/12=0.004167)
                n = number of payments over the loan’s lifetime. Multiply the number of years in your loan term by 12 (the number of months in a year) to get the number of payments for your loan. For example, a 30-year fixed mortgage would have 360 payments (30x12=360)
        """
        while propName =='' or propName not in self.allProperties:
            if propName == '':
                propName = input("What is the name of the property?")
            else:
                print(f"{propName} is not currently in the list. Please add it then run this again.")
                propName = self.addProperty()
        self.allProperties[propName]['askingPrice'] = propAsk = (float(input("What is the asking price? $: ")))
        self.allProperties[propName]['downPayment'] = propDP = (float(input("How much are you going to put as a down payment? $: ")))
        self.allProperties[propName]['closeCost'] = (float(input("What are the closing costs? $")))
        self.allProperties[propName]['beginMorgage'] = propMorgage = (propAsk - propDP)
        self.allProperties[propName]['yearlyInterestRate'] = yearInterest = ((float(input("What is your interest rate? Only enter a whole number.")))/100)
        self.allProperties[propName]['monthlyInterestRate'] = monthInterest = (yearInterest/12)        
        self.allProperties[propName]['totalPayments'] = payments = (float((input("How many years is the loan?")))*12)
        self.allProperties[propName]['monthlyMorgage'] = monthlyMorgage = (propMorgage(((monthInterest*(1 + monthInterest)**payments)/(((1+monthInterest)**payments)-1))))
        print(f"The monthly morgage payments are going to be ${monthlyMorgage}")
        return monthlyMorgage



    def income(self, propName=''):
        """
            This method calculates how much income the property GENERATES.
            it can accept propName as an input
        """
        while propName =='' or propName not in self.allProperties:
            if propName == '':
                propName = input("What is the name of the property?")
            else:
                print(f"{propName} is not currently in the list. Please add it then run this again.")
                propName = self.addProperty()
        self.allProperties[propName]['rent'] = float(input("What is the total rent you expect to get on the property? $: "))
        self.allProperties[propName]['otherIncome'] = float(input("How much will you make on laundry, storage, etc.? $:"))
        self.allProperties[propName]['rentalIncome'] = rentalIncome = (self.allProperties[propName]['rent']) + (self.allProperties[propName]['otherIncome'])
        
        print(f"The current income on {propName} is {rentalIncome}")
        return rentalIncome



    def expenses(self, propName=''):
        while propName =='' or propName not in self.allProperties:
            if propName == '':
                propName = input("What is the name of the property?")
            else:
                print(f"{propName} is not currently in the list. Please add it then run this again.")
                propName = self.addProperty()
        self.allProperties[propName]['taxes'] = tax = float(input("What are the yearly taxes on the property? $"))/12
        self.allProperties[propName]['insurance'] = insurance = float(input("What is the monthly insurance cost? $"))        
        while True:
            wantUtility = input("Do you need to put in cost of utilities? (y/n) ").lower()
            if wantUtility == 'y':
                self.allProperties[propName]['electicity'] = elec = float(input("What is the monthly electric bill? $"))
                self.allProperties[propName]['waterSewage'] = waterSewage = float(input("What is the monthly water and sewage costs? $"))
                self.allProperties[propName]['garbage'] = garbage = float(input("What is the monthly garbage costs? $"))
                self.allProperties[propName]['heating'] = heat = float(input("What is the monthly heating costs? $"))
                self.allProperties[propName]['utilities'] = utilities = (elec + waterSewage + garbage + heat)
                break
            if wantUtility == 'n':
                self.allProperties[propName]['utilities'] = utilities = 0.0
                break
            else:
                print("Please enter only y or n. ")
                continue
        self.allProperties[propName]['hoa'] = hoa = float(input("What is the monthly HOA fee? $"))
        self.allProperties[propName]['landscaping'] = landscape = float(input("What is the monthly lawn/snow care cost? $"))
        self.allProperties[propName]['vacancyProtection'] = vacancy = float(input("What is the monthly amount set aside to take care of vacancies? $"))
        self.allProperties[propName]['repair'] = repair  = float(input("What is the monthly repair cost? $"))
        self.allProperties[propName]['capitalExpenses'] = capEx  = float(input("What is the monthly amount set aside for capital expenses? e.g. a new roof every ten years $"))
        self.allProperties[propName]['managment'] = managment  = float(input("What is the monthly managment cost? $"))
        if self.allProperties[propName]['monthlyMorgagePayments'] != None:
            morgage = self.allProperties[propName]['monthlyMorgagePayments']
        else:
            morgage = self.morgage(propName)
        self.allProperties[propName]['totalExpenses'] = totalExpenses = tax + insurance + utilities + hoa + landscape + vacancy + repair + capEx + managment + morgage
        print(f"The total expenses on {propName} will be ${totalExpenses}")
        return totalExpenses



    def cashFlow(self, propName='', income='', totalExpenses=''):
        while propName =='' or propName not in self.allProperties:
            if propName == '':
                propName = input("What is the name of the property?")
            else:
                print(f"{propName} is not currently in the list. Please add it then run this again.")
                propName = self.addProperty()

        if self.allProperties[propName]['rentalIncome'] is not None:
            income = self.allProperties[propName]['rentalIncome']
        else: 
            while self.allProperties[propName]['rentalIncome'] is None:
                income = self.income(propName)

        if self.allProperties[propName]['totalExpenses'] is not None:
            totalExpenses = self.allProperties[propName]['totalExpenses']
        else:
            while self.allProperties[propName]['totalExpenses'] is None:
                totalExpenses = self.expenses(propName)
        self.allProperties[propName]['cashFlow'] = cashFlow = income - totalExpenses
        self.allProperties[propName]['annualCashFlow'] = annualCash = (cashFlow * 12)        
        print(f"The monthly cash flow on {propName} is ${cashFlow}. With an annual cash flow of ${annualCash}")
        return annualCash



    def totalInvestment(self, propName =''):
        while propName =='' or propName not in self.allProperties:
            if propName == '':
                propName = input("What is the name of the property?")
            else:
                print(f"{propName} is not currently in the list. Please add it then run this again.")
                propName = self.addProperty()
        while self.allProperties[propName]['downPayment'] == None:
            self.morgage(propName)
        while self.allProperties[propName]['closeCost'] == None:
            self.morgage(propName)
        self.allProperties[propName]['initialRepairs'] = initRepair = (float(input("What are going to be the initial repair costs? $")))
        self.allProperties[propName]['misc_Initial_Investment_Costs'] = miscInit = (float(input("What is the total for any other inital investment costs? $")))
        self.allProperties[propName]['total_Initial_Investment'] = totalInitInvest = (self.allProperties[propName]['downPayment'] + self.allProperties[propName]['closeCost'] + initRepair + miscInit)
        print(f"The total initial investment on {propName} is ${totalInitInvest}.")
        return totalInitInvest



    def findROI(self, propName=''):
        while propName =='' or propName not in self.allProperties:
            if propName == '':
                propName = input("What is the name of the property?")
            else:
                print(f"{propName} is not currently in the list. Please add it then run this again.")
                propName = self.addProperty()
        while self.allProperties[propName]['annualCashFlow'] is None:
            annualCash = self.cashFlow(propName)
        while self.allProperties[propName]['total_Initial_Investment'] is None:
            totalInvest = self.totalInvestment(propName)
        self.allProperties[propName]['ROI'] = roi = (annualCash/totalInvest)
        print(f"The cash on cash ROI on {propName} is {roi}")
        return roi
    

    

    def fastFacts(self, propName =''):
        while propName =='' or propName not in self.allProperties:
            if propName == '':
                propName = input("What is the name of the property?")
            else:
                print(f"{propName} is not currently in the list. Please add it then run this again.")
                propName = self.addProperty()
        propType = input("For 'personal' or 'income'?" ).lower()
        if propType == 'personal':
            while self.allProperties[propName]['monthlyMorgage'] is None:
                self.cashFlow(propName)
            while self.allProperties[propName]['totalExpenses'] is None:
                self.cashFlow(propName) 
            while self.allProperties[propName]['total_Initial_Investment'] is None:
                self.totalInvestment(propName)
            print(propName)
            print("The monthly morgage: ", self.allProperties[propName]['monthlyMorgage'])
            print("Monthly Expenses: ", self.allProperties[propName]['totalExpenses'])
            print("Total Inital investment: ", self.allProperties[propName]['total_Initial_Investment'])
        if propType == 'income':
            while self.allProperties[propName]['monthlyMorgage'] is None:
                self.cashFlow(propName)
            while self.allProperties[propName]['rentalIncome'] is None:
                self.cashFlow(propName)
            while self.allProperties[propName]['totalExpenses'] is None:
                self.cashFlow(propName)            
            while self.allProperties[propName]['annualCashFlow'] is None:
                self.cashFlow(propName)
            while self.allProperties[propName]['total_Initial_Investment'] is None:
                self.totalInvestment(propName)
            while self.allProperties[propName]['ROI'] is None:
                self.findROI(propName)
            print(propName)
            print("The monthly morgage: ", self.allProperties[propName]['monthlyMorgage'])
            print("Income from the rental: ", self.allProperties[propName]['rentalIncome'])
            print("Monthly Expenses: ", self.allProperties[propName]['totalExpenses'])
            print("Annual cash flow: ", self.allProperties[propName]['annualCashFlow'])
            print("Total Inital investment: ", self.allProperties[propName]['total_Initial_Investment'])
            print("ROI: ", self.allProperties[propName]['ROI'])



    def fullFacts(self, propName=''):
        while propName =='' or propName not in self.allProperties:
            if propName == '':
                propName = input("What is the name of the property?")
            else:
                print(f"{propName} is not currently in the list. Please add it then run this again.")
                propName = self.addProperty()
        print(self.allProperties[propName])



def roiCash():
    prop = ROI({},{})
    while True:
        action = input("What do you want to do with the propterty?: \nAdd property \nFind morgage rate \nFind income \nAdd expenses \nCash flow \nInvestment cost \nFind ROI \nFast Facts \nFull Facts \nQuit").lower()
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
        if action == 'investment cost':
            prop.totalInvestment()
        if action == 'find roi':
            prop.findROI
            continue
        if action == 'fast facts':
            prop.findROI
            continue
        if action == 'full facts':
            prop.findROI
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