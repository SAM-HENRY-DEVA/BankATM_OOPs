class Bank:
    Bname="Indian Bank"
    IFSC="IDIB000C033"
    def __init__(self,Cname,Acc_no,Balance,Phn_no,Pin):
        self.Cname=Cname
        self.Acc_no=Acc_no
        self.Balance=Balance
        self.Phn_no=Phn_no
        self.Pin=Pin


    @classmethod    
    def Bank_Details(cls):
        print('Bank Name : ',cls.Bname)
        print('Bank IFSC : ',cls.IFSC)

    def Cus_Details(self):
        print('Customer Name  : ',self.Cname)
        print('Account Number : ',self.Acc_no)
        print('Acc Balance    : ',self.Balance)
        print('Contact Number : ',self.Phn_no)
        print('Personal id No : ',self.Pin)

    def atm(self):
        print('Enter 1 for Cash Deposit')
        print('Enter 2 for Cash Withdrawal')
        print('Enter 3 for Pin Change')
        print('Enter 4 for Balance Enquiry')
        n=int(input('Enter your option : '))
        if n==1:
            acn=int(input('Please enter your Account Number : '))
            if acn==self.Acc_no:
                dep=int(input('Deposit Amount : Rs. '))
                self.Balance+=dep
                print(f'Amount has been depositted succesfully and your bal: Rs.{self.Balance}')
            else:
                print('Invalid account number')
                return Bank.atm(self)
        
        elif n==2:
            pin=int(input('Enter PIN : '))
            if len(str(pin))==4 and pin==self.Pin:
                wdr=int(input('Enter the amount to withdraw : '))
                if wdr<=self.Balance:
                    self.Balance-=wdr
                    print(f'Succesful, Please collect your cash and your bal: Rs.{self.Balance}')
                else:
                    print(f'Insufficient Fund, Please Retry.')
            else:
                print(f'Invalid PIN')
                return Bank.atm(self)
                
        elif n==3:
            pin=int(input('Please enter your PIN : '))
            if pin==self.Pin:
                print(f'Reset your PIN')
                npin=int(input('Enter new PIN : '))
                cpin=int(input('Confirm your New PIN : '))
                if len(str(npin))==4 and npin!=self.Pin and npin==cpin:
                    self.Pin=npin
                    print(f'PIN changed succesfully')
                else:
                    print(f'Please enter a valid PIN')
            else:
                print(f'Invalid PIN')
                return Bank.atm(self)
                
        elif n==4:
            pin=int(input('Enter your PIN : '))
            if pin==self.Pin:
                print(f'Your Account Balance is Rs. {self.Balance}')
            else:
                print(f'Invalid PIN')
                return Bank.atm(self)

        else:
            print(f'Invallid input, Please select within the option Range')
            
            return Bank.atm(self)                 
        
c1=Bank('Sam Henry',6651702425,25000,9940245082,1797)
c2=Bank('Dharma Seelan',6651802321,138000,8072789366,1234)
c3=Bank('Prashanth',6651707658,45897,9840689554,5678)
c4=Bank('Ashok',6651809834,17654,6379436791,9111)
c5=Bank('Vignesh',6651709876,287543,9841662022,1566)
