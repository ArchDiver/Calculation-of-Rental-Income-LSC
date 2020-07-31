class ROI():
    def __inti__(self, property, allProperties):
        self.property = property
        self.allProperties = allProperties

    def addPropterty(self):
        propName = input("What do you want to call the property? ")
        while propName in self.allProperties:
            print(f"You already have a property with that name.")
            propName = input("What do you want to call the property? ")
            
        propAddress = input("What is the propterty address? ")
        propAsk = float(input("What is the asking price? $: "))
        propDP = float(input("How much are you going to put as a down payment? $: "))
        propMorgage = propAsk - propDP



        return 



    def income(self, rent, laundry= 0.0, storage= 0.0 , misc= 0.0):
        """
            This method calculates how much income the property GENERATES.
            It accpets four float values:
            rent, laundry, storage, misc
            RENT is the only required value.
        """
        rentalIncome = rent + laundry + storage + misc
        
        print(f"The current income on this proptery is {rentalIncome}")
        return self
