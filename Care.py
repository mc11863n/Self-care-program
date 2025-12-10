class Skin:
    def __init__(self,skin_type = None,oily= None,dry = None ):
        self.skin = skin_type
        self.oily = oily
        self.dry = dry

    def get_skin(self):
        if self.skin == 'dry':
            return 'dry skin'
        elif self.skin == 'oily':
            return 'oily skin'
        else:
            return "No skin type detected"
        
class Acne:
    def __init__(self,name,large_pores = None, small_bumps = None, zits = None):
        self.name = name
        self.large_pores = large_pores
        self.small_bumps = small_bumps
        self.zits = zits

    def get_acne_check(self):
        if self.name == self.large_pores:
            return "Large pores detected"
        elif  self.name == self.small_bumps:
            return "Small bumps detected"
        elif self.name == self.zits:
            return "Zits detected"
        else:
            return "No acne issues"


class Budget:
    def __init__(self,price_of_product, max_budget, min_budeget, budget):
        self.price_of_product = price_of_product
        self.max_budget = max_budget
        self.min_budget = min_budeget
        self.budget = budget
    
    def get_price(self):
        return self.price_of_product
    
    def subtracting_price_budget(self):
        return self.budget - self.price_of_product
    
    def get_budget(self):
        if self.budget > self.max_budget:
            return "You have exeded your budget"
        elif self.budget < self.min_budget:
            return "You still have ${self.budget} left"
        else:
            return "Your budget is at its limit"
        
    def __str__():
        return

class SkinCare(Skin,Acne):
    def __init__(self,product_name):
        self.productname = product_name
        Skin.__init__(self, skin_type = '', oily= '', dry= '')
        Acne().__init__(name = '', large_pores = '', small_bumps = '', zits = '')
        




def main():
    user_skin = input("What skin do you have (oily or dry)? ")
    user_acne = input("Do you have large pores, small bumps, or zits? (Enter type) ")
    skin = Skin(skin = user_skin, oily='oily' if user_skin == 'oily' else '', dry='dry' if user_skin == 'dry' else '')
    acne = Acne(name = user_acne, large_pores= 'largepores dectected' if user_acne == 'large pores dectected' else None, small_bumps= ' Small bumps dectected'if user_acne == 'small bumps detected' else None, zits= 'zits dectected' if user_acne == 'zits dectected' else None)
    print(skin.get_skin())
    print(acne.get_acne_check())



if __name__ == "__main__":
    main()

     