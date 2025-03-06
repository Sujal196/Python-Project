#PYTHON BANK_ACCOUNT PROJECT.
class bank_account:
    def __init__(self,balance,acc,name,gender):
        self.balance=balance
        self.acc_no=acc
        self.name=name
        self.gender=gender
    def create_account(self):
        print("\n\t-:we have created your account:-\n")
        print("your name: ",self.name)
        print("your account number: ",self.acc_no)
        print("your current balance: ",self.balance)
    def debit(self,amount):
        if(amount>0 and amount<=self.balance):
            self.balance-=amount
            if(self.gender=='male' or self.gender=='Male' or self.gender=='MALE'):
                print(f"\nMR.{self.name}: RS.{self.balance} is new balance and RS.{amount} has debit")
            else:
                print(f"\nMISS.{self.name}: RS.{self.balance} is new balance and RS.{amount} has debit")
        else:
            print("cannot debited")
    def credit(self,amount):
        if(amount>0):
            self.balance+=amount
            if(self.gender=='male' or self.gender=='Male' or self.gender=='MALE'):
                print(f"\nMR.{self.name}: RS.{self.balance} is new balance and RS.{amount} has credit")
            else:
                print(f"\nMISS.{self.name}: RS.{self.balance} is new balance and RS.{amount} has credit")

        else:
            print("invalid amount,connot credited")
    def get_balance(self):
        return self.balance
print("\t -:WELCOME OF YOU IN OUR BANK MY BANK:-\n")
print("\t-:Enter some details to create your account:-\n")
f=input("Enter your name: ")
l=input("Enter your gender (Male/Female):  ")
#g=int(input("enter your account number in range between 1000 t0 1000000: "))
q=int(input("Enter your balance amount at least 2000: "))
while(q<2000):
    print("\n\tInvalid amount")
    q=int(input("\nEnter your balance amount at least 2000: "))
g=int(input("Enter your account number in range between 1000 t0 1000000: "))
if(g>1000 and g<1000000): 
            f=bank_account(q,g,f,l)
            f.create_account()
            print("\n\t-:choose one: For Credit select 'Credit' and For Debit select 'Debit:-\n")
            method=input("Enter the method: ")
            if(method=='Credit' or method=='credit' or method=='CREDIT' or method=='Debit' or method=='debit' or method=='DEBIT' ):
                    if(method=='Credit' or method=='credit' or method=='CREDIT'):
                        str='yes'
                        while(str=='yes' or str=='Yes'):
                            n=int(input("Enter your amount to credit: "))
                            f.credit(n)
                            print("your current balance : ",f.get_balance())
                            print("\n\t-:Do you want to credit another amount:-")
                            str=input("\nEnter Yes/yes otherwise NO/no: ")
                        print("\n\t-:Do you want to debit some amount,select debit:-\n\t ")
                        method=input("Enter the method: ")
                    if(method=='Debit' or method=='debit' or method=='DEBIT'):
                        str='yes'
                        while(str=='yes' or str=='Yes'):
                            d=int(input("Enter your amount to debit: "))
                            f.debit(d)
                            print("your current balance : ",f.get_balance())
                            print("\n\t-:Do you want to debit another amount:-")
                            str=input("\nEnter Yes/yes otherwise NO/no: ")
                            print("\n")
            else:
                print("\n\tDefault method")
                print("\n\tRestart the process again\n")
                print("\tTHANK YOU")
else:
    print("\n\tInvalid account number")
    print("\nDo you want to enter again account number: ")
    str=input("Enter yes/no: ")
    while(str=='yes' or str=='YES' or str=='Yes'):
         g=int(input("\nEnter your account number in range between 1000 to 1000000: "))
         if(g>1000 and g<1000000): 
            f=bank_account(q,g,f,l)
            f.create_account()
            print("\n\t-:choose one: For Credit select 'Credit' and For Debit select 'Debit':- ")
            method=input("\nEnter the method: ")
            if(method=='Credit' or method=='credit' or method=='CREDIT' or method=='Debit' or method=='debit' or method=='DEBIT' ):
                    if(method=='Credit' or method=='credit' or method=='CREDIT'):
                        str='yes'
                        while(str=='yes' or str=='Yes'):
                            n=int(input("Enter your amount to credit: "))
                            f.credit(n)
                            print("your current balance : ",f.get_balance())
                            print("\n\t-:Do you want to credit another amount:-")
                            str=input("\nEnter Yes/yes otherwise NO/no: ")
                        print("\n\t-:Do you want to debit some amount,select debit:-\n\t ")
                        method=input("Enter the method: ")
                            #print("Do you want to credit another amount:")
                            #str=input("Enter Yes/yes otherwise NO/no: ")
                        #method=input("Do you want to debit some amount,select debit: ")
                    if(method=='Debit' or method=='debit' or method=='DEBIT'):
                        str='yes'
                        while(str=='yes' or str=='Yes'):
                            d=int(input("Enter your amount to debit: "))
                            f.debit(d)
                            print("your current balance : ",f.get_balance())
                            print("\n\t-:Do you want to debit another amount:-")
                            str=input("\nEnter Yes/yes otherwise NO/no: ")
                            print("\n")
                            #print("Do you want to debit another amount:")
                            #str=input("Enter Yes/yes otherwise NO/no: : ")
            else:
                print("\n\tDefault method ")
                print("\n\tRestart the process again\n")
                print("\tTHANK YOU")
                break