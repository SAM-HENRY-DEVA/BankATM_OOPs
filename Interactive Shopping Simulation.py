class shop:
    
    shop_name='Sam SuperMarket'
    location ='Tambaram'
    inv={'rice bag':[15,850],'water bottle':[100,20],'chocolate':[30,15],
               'curry masala':[20,30],'snacks':[25,10],'juice':[25,28]}

    #initilizing a customer details with an empty cart
    def __init__(self,cname,ct_no,cus_id):
        self.cname=cname
        self.ct_no=ct_no
        self.cus_id=cus_id
        self.cart={}

    
    #main method--> object object
    def shopping(self):    
        while True:
            print(' ')
            option=int(input('''1 - Products Availability
2 - Customer Details
3 - Add to Cart
4 - Remove Product from Cart
5 - Customer Support
6 - Exit
                                
Enter an optoin : '''))
            
            if option==1:
                print(' ')
                self.inventory()
                
            elif option ==2:
                print(' ')
                self.cust_details()
                
            elif option==3:
                print(' ')
                self.add_prod()
                               
            elif option==4:
                print(' ')
                self.remove_prod()
            
            elif option==5:
                print(' ')
                self.cust_support()
            
            elif option==6:
                print(' ')
                self.thankyou()
                return
            
            else:
                print(' ')
                print('Enter a Valid Option 1 to 6')

    #method--> To showcase the available products in the shop inventory
    def inventory(self):
        print(' ')
        print('--------------------------------')
        print('Prod             |Qty  |Price  ')
        print('--------------------------------')
                
                
        for product, details in shop.inv.items():
            print(f'{product:<15}  | {details[0]:<3} | {details[1]:<5}')

    #method--> To display customer details along with cart history
    def cust_details(self):
        print(' ')
        print('Name        : ',self.cname)
        print('Cust ct.no  : ',self.ct_no)
        print('Customer id : ',self.cus_id)
        self.cart_view()

    #method--> To display cart along with detailed sum of bill
    def cart_view(self):
        if self.cart=={}:
            print('Your Cart is Empty, Please continue shopping !')
        else:
            print('--------------------------------')
            print('Prod              |Qty  |Price  ')
            print('--------------------------------')
            value=0
            for k,l in self.cart.items():
                print(f'{k:<15}   |{l:<3}  |{l*shop.inv[k][1]:<5}')
                value+=l*shop.inv[k][1]
            print(' ')
            print('SubTotal =               ',value )
            print('GST 18%  =               ',value*18/100)
            print(' ')
            print('Total    =               ',value+value*18/100 )
            
                
    #method--> To add available products to cart and and view them with sum amount
    def add_prod(self):

        for i,j in enumerate(shop.inv):
            print(f'{i+1} for {j}')
        print()
        print(f'0 for view cart')
        print(f'101 for main menu')
        print(' ')
        add=int(input('Enter the code to add to cart : '))
        
        if add==0:
            self.cart_view()
            self.add_prod()
            
        elif 1<=add<=len(shop.inv):
            qty=int(input('Enter the quantity : '))
            print(' ')
            pname=list(shop.inv)[add-1]
            if qty<=shop.inv[pname][0]:           
                
                if pname in self.cart:
                    self.cart[pname]+=qty
                else:
                    self.cart[pname]=qty
                shop.inv[pname][0]-=qty
                print('Product added successfully')
            else :
                print(f'Max available quantity ={shop.inv[pname][0]}')
            self.add_prod()

        elif add==101:
            return
        
        else:
            print(' ')
            print('Enter a valid input between 0-6 & 101')
            self.add_prod()

            
    #method--> To remove products from the cart
    def remove_prod(self):
        for i,prod_name in enumerate(self.cart):
            print(f'{i+1} to remove {prod_name}')
        p=int(input('Enter the prod to be removed : '))
        prod_name = list(self.cart.keys())[p - 1]
        print(f'Available quantity = {self.cart[prod_name]}')
        qty=int(input('Enter qty : '))
        if qty<=self.cart[prod_name]:
            self.cart[prod_name]-=qty
            if self.cart[prod_name]==0:
                self.cart.pop(prod_name)
            shop.inv[prod_name][0]+=qty
            print(' ')
            print('Product Removed Succesfully')
        else:
            print(' ')
            print(f'qty in cart is {self.cart[prod_name]}')
            

    #method--> To display the contact info and toll free number
    def cust_support(self):
        print(' ')
        print('Toll Free : 1800 9876543')
        print(' ')
        print('contact our executive : +91 9940245082')
        

    #method--> To end the simulation with a thankyou note
    def thankyou(self):
        print(' ')
        print ('Thankyou for Choosing Sam SuperMarket !!')
        

#Objects created for test running the program    
c1=shop('vijay',6374624480,101)
c2=shop('Dharma',8072789366,102)
c3=shop('Mohan',9876545670,103)
c4=shop('Dhanush',8678904563,104)
c5=shop('vishal',7989809878,105)

c1.shopping()
#c2.shopping()
#c3.shopping()
#c4.shopping()
#c5.shopping()
