class Skin:
    def __init__(self,skin,oily,dry ):
        self.skin = skin
        self.oily = oily
        self.dry = dry

    def get_skin(self,skin):
        if self.skin is self.oily:
            return self.oily
        else:
            pass
        
        if self.skin is self.dry:
            return self.dry
        else:
            pass
        
class Acne:
    def __init__(self,name,large_pores, small_bumps, zits):
        self.name = name
        self.large_pores = large_pores
        self.small_bumps = small_bumps
        self.zits = zits
    def get_acne_check(self):
        if self.name is self.large_pores:
            return self.large_pores
        else:
            pass

        if self.name is self.small_bumps:
            return self.small_bumps
        else:
            pass

        if self.name is self.zits:
            return self.zits
        else:
            pass
        
    
class SkinCare(Skin):

    def __init__(self,product_name):
        self.productname = product_name
        super().__init__()

    

    
def main(): 
    






if __name__ == '__main__':
    main()

    