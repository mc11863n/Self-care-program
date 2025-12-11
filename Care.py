class Skin:
    def __init__(self,skin = None,oily= None,dry = None, combination = None, sensative = None):
        self.skin = skin
        self.oily = oily
        self.dry = dry
        self.combination = combination
        self.sensative = sensative

    def get_skin(self):
        if self.skin == self.dry:
            return 'dry skin'
        elif self.skin == self.oily:
            return 'oily skin'
        elif self.skin == self.combination:
            return 'combination skin'
        elif self.skin == self.sensative:
            return 'sensative skin'
        else:
            return "No skin type detected"
        
class Acne:
    def __init__(self,name,clogge_pores = None, cytic_acne = None):
        self.name = name
        self.clogge_pores = clogge_pores
        self.cytic_acne = cytic_acne

    def get_acne_check(self):
        if self.name == self.clogge_pores:
            return "clogged pores"
        elif self.name == self.cytic_acne:
            return "cytic acne"
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
        super().__init__(self, skin = '', oily= '', dry= '', combination= '', sensative= '')
        super().__init__(name = '', clogge_pores = '', cytic_acne = '')
        




    


def main():
    user_skin = input("What skin do you have oliy, dry, combination, sensitive? ")
    user_acne = input("Do you have any acne issues (clogge pores dectected or cytic acne dectected)? ")
    skin_type = Skin(skin = user_skin, oily='oily' if user_skin == 'oily' else '', dry='dry' if user_skin == 'dry' else '')
    acne_type = Acne(name = user_acne, clogge_pores= 'clogge pores dectected' if user_acne == 'clogge pores dectected' else None, cytic_acne= 'cytic acne dectected' if user_acne == 'cytic acne dectected' else None)
    print(acne_type.get_acne_check())
    print(skin_type.get_skin())

def main():
    name= input("Enter your name")
    print(f"Hello, {name}! Welcome to the Skin Care Recommendation Program.")

    UserInput= input("Enter your skin type (oily, dry, combination, sensitive, cystic acne, clogged pores): ").strip().lower() #use lowercase letters only
    if UserInput == "oily":
        print(f"Hi {name}, you have oily skin. Recommended products: foaming cleanser, oil-free moisturizer, clay mask.") #why is name not showing up?
        print("Suggested routine: Cleanse twice daily, exfoliate 2-3 times a week, use toner, moisturize.")
        print("link to reccommended product: https://www.laroche-posay.us/our-products/face/face-wash/toleriane-purifying-foaming-face-wash-tolerianepurifyingfoamingfacialwash.html?gclsrc=aw.ds&gad_source=1&gad_campaignid=58622437&gbraid=0AAAAAD80ULe0X_gR4to1puJTuu6PfQUH_&gclid=CjwKCAiA0eTJBhBaEiwA-Pa-hUOZPPXoLzXhvRjxETdnTweolDbpdqbWMb7tt1C010M0zfEd3bixHhoC4jMQAvD_BwE")

    elif UserInput == "dry":
        print(f"Hi {name}, you have dry skin. Recommended products: hydrating cleanser, rich moisturizer, hydrating mask.")
        print("Suggested routine: Cleanse once daily, exfoliate once a week, use hydrating toner, moisturize.")
        print("link to reccommended product: https://www.laroche-posay.us/our-products/face/dry-skin-routine-set-dryskincareset.html?GeoRedirectOff&gclsrc=aw.ds&gad_source=1&gad_campaignid=18158821601&gbraid=0AAAAAD80ULdfhbKwUnOP8nSd22Z2PwkR5&gclid=CjwKCAiA0eTJBhBaEiwA-Pa-hUJHySB8TauuoV9PiGIwBN-9zcnU64p2iXa1v1-E_vyScsh6C_8akBoC4CMQAvD_BwE")

    elif UserInput == "combination":
        print(f"Hi {name}, you have combination skin. Recommended products: gentle cleanser, lightweight moisturizer, balancing mask.")
        print("Suggested routine: Cleanse twice daily, exfoliate 2 times a week, use toner, moisturize.")
        print("link to reccommended product: https://www.laroche-posay.us/offers/exclusive-value-sets/toleriane-purifying-foaming-cleanser-toleriane-double-repair-face-moisturizer-tolerianepurcleanseranddrmset.html?GeoRedirectOff&gclsrc=aw.ds&gad_source=1&gad_campaignid=18158821601&gbraid=0AAAAAD80ULdfhbKwUnOP8nSd22Z2PwkR5&gclid=CjwKCAiA0eTJBhBaEiwA-Pa-hUet64KNj_wp4XdnuDlPM5hq1jDrqXyFx9kQdAAlPc8uuBwYHiNt0xoCk4MQAvD_BwE")
    
    elif UserInput == "sensitive":
        print(f"Hi {name}, you have sensitive skin. Recommended products: gentle cleanser, soothing moisturizer, calming mask.")
        print("Suggested routine: Cleanse once daily, exfoliate once a week, use calming toner, moisturize.")
        print("link to reccommended product: https://www.cerave.com/skincare/cleansers/air-foam-foaming-facial-cleanser")

    elif UserInput == "cystic acne":
        print(f"Hi {name}, you have cystic acne. Recommended products: medicated cleanser, oil-free moisturizer, acne treatment mask.")
        print("Suggested routine: Cleanse twice daily, exfoliate 2 times a week, use acne-fighting toner, moisturize.")
        print("link to reccommended over the counter product: https://www.cvs.com/shop/panoxyl-foaming-wash-maximum-strength-deep-cleaning-with-10-benzoyl-peroxide-5-5-oz-prodid-1150093?skuId=412505&cgaa=QWxsb3dHb29nbGVUb0FjY2Vzc0NWU1BhZ2Vz&cid=ps_bea_ski_pla&gclsrc=aw.ds&gad_source=1&gad_campaignid=21158449916&gclid=CjwKCAiA0eTJBhBaEiwA-Pa-hT9SeqdaOvRWBk7UfZwVCD28xS8C12IkjjUUX0bM5NXNQvKImflWFRoCqxIQAvD_BwE")
        print("we also reccomend speaking to a dermatologist for prescription treatments.")

    elif UserInput == "clogged pores":
        print(f"Hi {name}, you have clogged pores. Recommended products: exfoliating cleanser, lightweight moisturizer, pore-clearing mask.")
        print("Suggested routine: Cleanse twice daily, exfoliate 3 times a week, use toner, moisturize.")
        print("link to reccommended product: https://www.ulta.com/p/zero-pore-pad-pimprod2053434?sku=2645351&cmpid=PS_Non!google!Product_Listing_Ads&cagpspn=pla&CATCI=&CAAGID=&CAWELAID=330000200003341746&gad_source=1&gad_campaignid=22865742698&gbraid=0AAAAAD9rLH60qN2anF_1AMCt-OqPFvMu_&gclid=CjwKCAiA0eTJBhBaEiwA-Pa-hdHhrTs9S6vOa1CQBqagpv65VG3EdzBq3NUFR6hkbcdG-q9N5Be3kBoCGyIQAvD_BwE")

    elif UserInput not in ["oily", "dry", "combination", "sensitive", "cystic acne", "clogged pores"]:
        print("Invalid input. Please enter a valid skin type: oily, dry, combination, sensitive, cystic acne, or clogged pores and make sure you are using only lower case letters.")

    #product dictionary with prices     #IS THIS LOOPS?
    product_dict = {
        "oily": [
            "Foaming Cleanser: $15.00",
            "Oil-Free Moisturizer: $20.00",
            "Clay Mask: $18.00",
        ],
        "dry": [
            "Hydrating Cleanser: $16.00",
            "Rich Moisturizer: $22.00",
            "Hydrating Mask: $19.00",
        ],
        "combination": [
            "Gentle Cleanser: $14.00",
            "Lightweight Moisturizer: $21.00",
            "Balancing Mask: $17.00",
        ],
        "sensitive": [
            "Gentle Cleanser: $13.00",
            "Soothing Moisturizer: $23.00",
            "Calming Mask: $20.00",
        ],
        "cystic acne": [
            "Medicated Cleanser: $18.00",
            "Oil-Free Moisturizer: $20.00",
            "Acne Treatment Mask: $22.00",
        ],
        "clogged pores": [
            "Exfoliating Cleanser: $17.00",
            "Lightweight Moisturizer: $21.00",
            "Pore-Clearing Mask: $19.00",
        ],
    }
    if UserInput in product_dict:
        print("\nRecommended Products and Prices:")
        for product in product_dict[UserInput]:
            print(f"- {product}")

    budget= float(input("Enter your budget for skin care products in American dollars: $" ))
    if budget < 20:
         print("With a budget under $20, we recommend focusing on essential products like a gentle cleanser and moisturizer.") #IS THIS MATHMATICAL OPERATIONS?
    elif budget >= 20 and budget < 50:
         print("With a budget between $20 and $50, you can consider adding an exfoliator or a mask to your routine.")
    elif budget >= 50:
         print("With a budget over $50, you have the flexibility to explore premium products and complete your skincare routine.")
    elif budget <= 0:
         print("Please enter a valid budget amount greater than $0.")





if __name__ == "__main__":
    main()

     