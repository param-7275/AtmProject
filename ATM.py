import datetime
current  = datetime.datetime.now()
current = current.strftime("%d/%m/%Y - %I:%M:%S")
today = str(current)
with open("person1.txt")as f:
    d = f.read()
    pas1 = int(d)
with open("person11.txt") as f:
    t = f.read()
    amnt1 = int(t)
with open("person2.txt")as f:
    d = f.read()
    pas2 = int(d)
with open("person22.txt") as f:
    t = f.read()
    amnt2 = int(t)
with open("person3.txt")as f:
    d = f.read()
    pas3 = int(d)
with open("person33.txt") as f:
    t = f.read()
    amnt3 = int(t)
with open("person4.txt")as f:
    d = f.read()
    pas4 = int(d)
with open("person44.txt") as f:
    t = f.read()
    amnt4 = int(t)
class employeee:
    def __init__(self,name,balance,password):
        self.name = name
        self.balance = balance
        self.password = password
    def withdrawal(self,amnt):
        if amnt<= self.balance:
            self.balance=self.balance-amnt
        else:
            print("Amount Not sufficient In Acount")     
    def deposit(self,amnt):
        self.balance = self.balance+amnt
def list():
    print("press 1 for WITHDRAWL\npress 2 for deposit\npress 3 for check balance\npress 4 for statement\npress 5 for exit")
p1=employeee("sandeep",amnt1,pas1)
p2=employeee("sumit",amnt2,pas2)
p3=employeee("vivek",amnt3,pas3)
p4=employeee("rajesh",amnt4,pas4)
while True:
    for i in range(2,-1,-1):
        try:
            Q = int(input("ENTER YOUR 4 DIGIT PIN : "))
            while True:
                if Q==pas1:
                    print(f"hello {p1.name} welcome PNB Atm!\n")
                    list()
                    h = int(input("choose one option:"))
                    if h==1:
                        p = int(input("enter withdrawal amount: "))
                        p1.withdrawal(p)
                        with open("person11.txt","w")as f:
                            f.write(str(p1.balance))
                        with open("sandeep.txt","a")as f:
                            f.write(str(p) + " rupees withdrawal\t"+ str(today)+"\n")
                            f.write(str(p1.balance) + " rupees is available balance \n")
                            print("YOUR AMOUNT WITHDRAL SUCCESSFULLY !\nTOTAL AMOUNT:", p1.balance)
                    elif h==2:
                        p = int(input("Enter Deposit Amount: "))
                        p1.deposit(p)
                        with open("person11.txt","w") as f:
                            f.write(str(p1.balance))
                        with open("sandeep.txt","a")as f:
                            f.write(str(p) + " rupees deposit\t"+ str(today)+"\n")
                            f.write(str(p1.balance) + " rupees is available balance \n")
                            print("YOUR AMOUNT DEPOSIT SUCCESSFULLY !\nTOTAL AMOUNT:", p1.balance)
                    elif h==3:
                        with open("sandeep.txt")as f:
                            s=f.readlines()[-1]
                            print(s)
                    elif h==4:
                        with open("sandeep.txt")as f:
                            stmnt = f.read()
                            print(stmnt)
                    elif h==5:
                        print("Thanks For Using PNB Atm:")
                        break
                    else:
                         print("Choose Given Option")
                elif Q==pas2:
                    print(f"hello {p2.name} welcome PNB Atm!\n")
                    list()
                    h = int(input("choose one option:"))
                    if h==1:
                        p = int(input("enter withdrawal amount: "))
                        p2.withdrawal(p)
                        with open("person22.txt","w") as f:
                            f.write(str(p2.balance))
                        with open("sumit.txt","a")as f:
                            f.write(str(p) + " rupees withdrawal\t")
                            f.write(today)
                            f.write("\n")
                            f.write(str(p2.balance) + " rupees is available balance \n")
                            print("YOUR AMOUNT WITHDRAL SUCCESSFULLY !\nTOTAL AMOUNT:", p2.balance)
                    elif h==2:
                        p = int(input("Enter Deposit Amount: "))
                        p2.deposit(p)
                        with open("person22.txt","w") as f:
                            f.write(str(p2.balance))
                        with open("sumit.txt","a")as f:
                            f.write(str(p) + " rupees deposit\t")
                            f.write(today)
                            f.write("\n")
                            f.write(str(p2.balance) + " rupees is available balance \n")
                            print("YOUR AMOUNT DEPOSIT SUCCESSFULLY !\nTOTAL AMOUNT:", p2.balance)
                    elif h==3:
                        with open("sumit.txt")as f:
                            s=f.readlines()[-1]
                            print(s)
                    elif h==4:
                        with open("sandeep.txt")as f:
                            stmnt = f.read()
                            print(stmnt)
                    elif h==5:
                        print("Thanks For Using PNB Atm:")
                        break
                    else:
                        print("Choose Given Option")
                        
                elif Q==pas3:
                    print(f"hello {p3.name} welcome PNB Atm!\n")
                    list()
                    h = int(input("choose one option:"))
                    if h==1:
                        p = int(input("enter withdrawal amount: "))
                        p3.withdrawal(p)
                        with open("person33.txt","w") as f:
                            f.write(str(p3.balance))
                        with open("vivek.txt","a")as f:
                            f.write(str(p) + " rupees withdrawal\t")
                            f.write(today)
                            f.write("\n")
                            f.write(str(p3.balance) + " rupees is available balance")
                            print("YOUR AMOUNT WITHDRAL SUCCESSFULLY !\nTOTAL AMOUNT:", p3.balance)
                    elif h==2:
                        p = int(input("Enter Deposit Amount: "))
                        p3.deposit(p)
                        with open("person33.txt","w") as f:
                            f.write(str(p3.balance))
                        with open("vivek.txt","a")as f:
                            f.write(str(p) + " rupees deposit\t")
                            f.write(today)
                            f.write(str(p3.balance) + " rupees is available balance \n")
                            print("YOUR AMOUNT DEPOSIT SUCCESSFULLY !\nTOTAL AMOUNT:", p3.balance) 
                    elif h==3:
                        with open("vivek.txt")as f:
                            s=f.readlines()[-1]
                            print(s)
                    elif h==4:
                        with open("vivek.txt")as f:
                            stmnt = f.read()
                            print(stmnt)
                    elif h==5:
                        print("Thanks For Using PNB Atm:")
                        break
                    else:
                        print("Choose Given Option")
                elif Q==pas4:
                    print(f"hello {p4.name} welcome PNB Atm!\n")
                    list()
                    h = int(input("choose one option:"))
                    if h==1:
                        p = int(input("enter withdrawal amount: "))
                        p4.withdrawal(p)
                        with open("person44.txt","w")as f:
                            f.write(str(p4.balance))
                        with open("rajesh.txt","a")as f:
                            f.write(str(p) + " rupees withdrawal\t")
                            f.write(today)
                            f.write("\n")
                            f.write(str(p4.balance) + " rupees is available balance \n")
                            print("YOUR AMOUNT WITHDRAL SUCCESSFULLY !\nTOTAL AMOUNT:", p4.balance)
                    elif h==2:
                        p = int(input("Enter Deposit Amount: "))
                        p4.deposit(p)
                        with open("person44.txt","w") as f:
                            f.write(str(p4.balance))
                        with open("rajesh.txt","a")as f:
                            f.write(str(p) + " rupees deposit\t")
                            f.write(today)
                            f.write("\n")
                            f.write(str(p4.balance) + " rupees is available balance \n")
                            print("YOUR AMOUNT DEPOSIT SUCCESSFULLY !\nTOTAL AMOUNT:", p4.balance)
                    elif h==3:
                        with open("rajesh.txt")as f:
                            s=f.readlines()[-1]
                            print(s)
                    elif h==4:
                        with open("rajesh.txt")as f:
                            stmnt = f.read()
                            print(stmnt)
                    elif h==5:
                        print("Thanks For Using PNB Atm:")
                        break
                    else:
                        print("Choose Given Option")
                else:
                    print("Please Enter Correct Password")
                    print("You have " +str(i)+ " attempt left:\n")
                    break       
                    if i == 0:
                        print("Your Card Blocked!\nPlease Try After 24 Hours:")     
                        break
        except:
            print("Character Not Allowed, Enter Correct Key :")
