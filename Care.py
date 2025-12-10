class Skin:
    def __init__(self,skin_type = None,oily= None,dry = None ):
        self.skin_type = skin_type
        self.oily = oily
        self.dry = dry

    def get_skin(self,skin_type):
        return self.skin_type
        
class Acne:
    def __init__(self,name,large_pores = None, small_bumps = None, zits = None):
        self.name = name
        self.large_pores = large_pores
        self.small_bumps = small_bumps
        self.zits = zits
    def get_acne_check(self):
        return self.name
        
    
class SkinCare(Skin):

    def __init__(self,product_name):
        super().__init__(None,None,None)
        self.productname = product_name




def main():
    return



if __name__ == '__main__':
    main()

    