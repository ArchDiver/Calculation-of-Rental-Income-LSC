import os  #to use 'clear()'
def clear():#to use 'clear()'
    os.system( 'cls' )

class ROI():
    def __init__(self, property, allProperties):
        self.property = property
        self.allProperties = allProperties



    def addProperty(self, propName=''):
        # while propName == 'quit':
        #     break
        if propName == '':
            propName = input("What do you want to call the property? ").lower()
            # while propName == 'quit':
            #     break             
        else:
            while propName in self.allProperties and propName !='':
                print(f"You already have a property with that name.")
                propName = input("What do you want to call the property? ").lower()
                # while propName == 'quit':
                #     break
        self.allProperties[propName] = {}
        self.allProperties[propName]['address'] = input("What is the propterty address? ").lower()
    
        print(f"\n{propName} was added to your list of properties.\n")
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
                propName = input("\nWhat is the name of the property? ").lower()
            else:
                print(f"{propName} is not currently in the list. Please add it. Then you will be returned here.")
                propName = self.addProperty()
        self.allProperties[propName]['askingPrice'] = propAsk = (float(input("What is the asking price? $: ")))
        self.allProperties[propName]['downPayment'] = propDP = (float(input("How much are you going to put as a down payment? $: ")))
        self.allProperties[propName]['closeCost'] = (float(input("What are the closing costs? $: ")))
        self.allProperties[propName]['beginMorgage'] = propMorgage = (propAsk - propDP)
        self.allProperties[propName]['yearlyInterestRate'] = yearInterest = ((float(input("What is your interest rate? Only enter a number but do NOT include the % ")))/100)
        self.allProperties[propName]['monthlyInterestRate'] = monthInterest = (yearInterest/12)        
        self.allProperties[propName]['totalPayments'] = payments = (float((input("How many years is the loan? ")))*12)
        self.allProperties[propName]['monthlyMorgage'] = monthlyMorgage = (propMorgage*(((monthInterest* (1 + monthInterest) ** payments)/(((1 + monthInterest) ** payments)-1))))
        print(f"\nThe monthly morgage payments are going to be ${monthlyMorgage}\n")
        return monthlyMorgage



    def income(self, propName=''):
        """
            This method calculates how much income the property GENERATES.
            it can accept propName as an input
        """
        while propName =='' or propName not in self.allProperties:
            if propName == '':
                propName = input("\nWhat is the name of the property? ").lower()
            else:
                print(f"{propName} is not currently in the list. Please add it. Then you will be returned here.")
                propName = self.addProperty()
        self.allProperties[propName]['rent'] = float(input("What is the total rent you expect to get on the property? $: "))
        self.allProperties[propName]['otherIncome'] = float(input("How much will you make on laundry, storage, etc.? $: "))
        self.allProperties[propName]['rentalIncome'] = rentalIncome = (self.allProperties[propName]['rent']) + (self.allProperties[propName]['otherIncome'])
        
        print(f"\nThe current income on {propName} is {rentalIncome}\n")
        return rentalIncome



    def expenses(self, propName=''):
        while propName =='' or propName not in self.allProperties:
            if propName == '':
                propName = input("\nWhat is the name of the property? ").lower()
            else:
                print(f"{propName} is not currently in the list. Please add it. Then you will be returned here.")
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
                print(f"\nYour total utilities are ${utilities}\n")
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
        if 'monthlyMorgage' in self.allProperties[propName].keys():
            morgage = self.allProperties[propName]['monthlyMorgage']
        else:
            print("\nYou need to run the morgage calculator to estimate expenses. You will be sent fill that out, then returned here.\n")
            morgage = self.morgage(propName)
        self.allProperties[propName]['totalExpenses'] = totalExpenses = tax + insurance + utilities + hoa + landscape + vacancy + repair + capEx + managment + morgage
        print(f"\nThe total expenses on {propName} will be ${totalExpenses}\n")
        return totalExpenses



    def cashFlow(self, propName='', income='', totalExpenses=''):
        while propName =='' or propName not in self.allProperties:
            if propName == '':
                propName = input("\nWhat is the name of the property? ").lower()
            else:
                print(f"{propName} is not currently in the list. Please add it. Then you will be returned here.")
                propName = self.addProperty()

        while 'rentalIncome' not in self.allProperties[propName].keys():
            income = self.income(propName)
            break
        income = self.allProperties[propName]['rentalIncome']
        while 'totalExpenses' not in self.allProperties[propName].keys():
            totalExpenses = self.expenses(propName)
            break
        totalExpenses = self.allProperties[propName]['totalExpenses']
        self.allProperties[propName]['cashFlow'] = cashFlow = income - totalExpenses
        self.allProperties[propName]['annualCashFlow'] = annualCash = (cashFlow * 12)        
        print(f"\nThe monthly cash flow on {propName} is ${cashFlow}. With an annual cash flow of ${annualCash}\n")
        return annualCash



    def totalInvestment(self, propName =''):
        while propName =='' or propName not in self.allProperties:
            if propName == '':
                propName = input("\nWhat is the name of the property? ").lower()
            else:
                print(f"{propName} is not currently in the list. Please add it. Then you will be returned here.")
                propName = self.addProperty()
        while 'downPayment' not in self.allProperties[propName].keys():
            self.morgage(propName)
            break
        while 'closeCost' not in self.allProperties[propName].keys():
            self.morgage(propName)
            break
        self.allProperties[propName]['initialRepairs'] = initRepair = (float(input("What are going to be the initial repair costs? $")))
        self.allProperties[propName]['misc_Initial_Investment_Costs'] = miscInit = (float(input("What is the total for any other inital investment costs? $")))
        self.allProperties[propName]['total_Initial_Investment'] = totalInitInvest = (self.allProperties[propName]['downPayment'] + self.allProperties[propName]['closeCost'] + initRepair + miscInit)
        print(f"\nThe total initial investment on {propName} is ${totalInitInvest}.\n")
        return totalInitInvest



    def findROI(self, propName=''):
        while propName =='' or propName not in self.allProperties:
            if propName == '':
                propName = input("\nWhat is the name of the property? ").lower()
            else:
                print(f"{propName} is not currently in the list. Please add it. Then you will be returned here.")
                propName = self.addProperty()
        while 'annualCashFlow' not in self.allProperties[propName].keys():
            self.cashFlow(propName)
            break
        while 'total_Initial_Investment' not in self.allProperties[propName].keys():
            self.totalInvestment(propName)
        self.allProperties[propName]['ROI'] = roi = ((self.allProperties[propName]['annualCashFlow'])/(self.allProperties[propName]['total_Initial_Investment']))*100
        print(f"\nThe cash on cash ROI on {propName} is {roi}\n")
        return roi
    

    

    def fastFacts(self, propName =''):
        while propName =='' or propName not in self.allProperties:
            if propName == '':
                propName = input("\nWhat is the name of the property? ").lower()
            else:
                print(f"{propName} is not currently in the list. Please add it. Then you will be returned here.")
                propName = self.addProperty()
        propType = input("For 'personal' or 'income'? " ).lower()
        if propType == 'personal':
            while 'monthlyMorgage' not in self.allProperties[propName].keys():
                self.cashFlow(propName)
                break
            while 'totalExpenses' not in self.allProperties[propName].keys():
                self.cashFlow(propName)
                break 
            while 'total_Initial_Investment'  not in self.allProperties[propName].keys():
                self.totalInvestment(propName)
                break
            print(propName)
            print("The monthly morgage: ", self.allProperties[propName]['monthlyMorgage'])
            print("Monthly Expenses: ", self.allProperties[propName]['totalExpenses'])
            print("Total Inital investment: ", self.allProperties[propName]['total_Initial_Investment'])
            print("\n\n")
        if propType == 'income':
            while 'monthlyMorgage' not in self.allProperties[propName].keys():
                self.cashFlow(propName)
                break
            while 'rentalIncome' not in self.allProperties[propName].keys():
                self.cashFlow(propName)
                break
            while 'totalExpenses' not in self.allProperties[propName].keys():
                self.cashFlow(propName)
                break
            while 'annualCashFlow' not in self.allProperties[propName].keys():
                self.cashFlow(propName)
                break
            while 'total_Initial_Investment' not in self.allProperties[propName].keys():
                self.totalInvestment(propName)
                break
            while 'ROI' not in self.allProperties[propName].keys():
                self.findROI(propName)
                break
            print(propName)
            print("The monthly morgage: ", self.allProperties[propName]['monthlyMorgage'])
            print("Income from the rental: ", self.allProperties[propName]['rentalIncome'])
            print("Monthly Expenses: ", self.allProperties[propName]['totalExpenses'])
            print("Annual cash flow: ", self.allProperties[propName]['annualCashFlow'])
            print("Total Inital investment: ", self.allProperties[propName]['total_Initial_Investment'])
            print("ROI: ", self.allProperties[propName]['ROI'])
            print("\n\n")



    def fullFacts(self, propName=''):
        while propName =='' or propName not in self.allProperties:
            if propName == '':
                propName = input("What is the name of the property? ").lower()
            else:
                print(f"{propName} is not currently in the list. Please add it. Then you will be returned here.")
                propName = self.addProperty()
        print(f"\nInformation on {propName}:")
        for k, v in self.allProperties[propName].items():
            print(k,": ", v)
        print("\n")



    def remove(self, propName=''):
        while propName =='' or propName not in self.allProperties:
            if propName == '':
                propName = input("What is the name of the property? ").lower()
            else:
                print(f"{propName} is not currently in the list. So you don't have to remove it.")
                break
        while True:
            sure = input("Are you sure you want to remove the property called {propName}? (y/n) ").lower()
            if sure == "y":
                del self.allProperties[propName]
                print(f"\n{propName} was deleted.\n")
                break
            elif sure =='n':
                break
            else:
                print("Please choose y or n.")
                continue



def roiCash():
    prop = ROI({},{})
    clear()
    while True:
        action = int(input("\n\nWhat do you want to do with the propterty?: \n1)Add property \n2)Find morgage rate \n3)Find income \n4)Add expenses \n5)Cash flow \n6)Investment cost \n7)Find ROI \n8)Fast Facts \n9)Full Facts \n10)Clear \n11)Quit \nType the number from list above: "))
        if action == 1:
            prop.addProperty()
            continue
        if action == 2:
            prop.morgage()
            continue
        if action == 3:
            prop.income()
            continue
        if action == 4:
            prop.expenses()
            continue
        if action == 5:
            prop.cashFlow()
        if action == 6:
            prop.totalInvestment()
        if action == 7:
            prop.findROI()
            continue
        if action == 8:
            prop.fastFacts()
            continue
        if action == 9:
            prop.fullFacts()
            continue      
        if action == 10:
            quit = input("Are you sure you want to clear the screen? No data will be lost. (y/n): ").lower()
            if quit == 'n':
                continue
            if quit =='y':
                clear()
                continue
            else:
                print("That was not acceptable. Sending you to the main menu.")
                continue                         
        if action == 11:
            quit = input("Are you sure you want to quit? All data will be lost. (y/n): ").lower()
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
roiCash()