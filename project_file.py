# Create class store to keep tracks of products.
class Product:
    def __init__(self,code,name,price):
        self.code = code
        self.name = name
        self.price = price
        
class Store: 
    def __init__(self):
        self.p_list = []
        
    def adding_products(self):
        p1 = Product(1,"Soap",30)
        self.p_list.append(p1)
        p2 = Product(2,"Bag",700)
        self.p_list.append(p2)
        p3 = Product(3,"Juice",100)
        self.p_list.append(p3)
        p4 = Product(4,"Dignity",2)
        self.p_list.append(p4)
        
    def display_list(self):
        print("Products in the store are")
        for p in self.p_list:
            print("Code = ",p.code,"Name = ",p.name)
            
    def purchase(self):
        code = int(input("Enter product code: "))
        quantity = int(input("Enter quantity of products: "))
        
        for p in self.p_list:
            if p.code == code:
                total_price = p.price*quantity
                print("Product:", p.name,"Quantity:", quantity,"Total_price:", total_price)        
        
st = Store()

st.adding_products()

st.display_list()

st.purchase()