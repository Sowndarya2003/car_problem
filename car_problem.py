'''create a class car_show_room in which
1)create a function name car_company which will allow user to select a car_company of of the displayed companies.If the user enters in any
  random company he/she should be asked to re-enter.
2)According to the car company selected the user should be redirected to selecting the car models of that company of of the given list.
  If any random order enter again re-enter.
3)after selecting the model the user should be redirected to selecting the varient(petrol/diesel)
4)According to the car company model and variant a price should be calculated to which  agst and cgst are added to make it the total price.
NOTE:sgst and cgst are common for all the cars'''

class car_company:
    def __init__(self):
        self.agst=4500
        self.cgst=9000
        self.insurance=120000    
    def company(self):
        while True:
            print("1.BMW")
            print("2.Benze")
            self.ch=input("Enter the choice:")
            if(self.ch==1):
                print("you are selected car:",self.ch)
                self.model()
                break
            elif(self.ch==2):
                print("you are selected car",self.ch)
                self.model()
                break
            else:
                print("re-enter")
                break          
    def model(self):
        while True:
            print("3.Model1")
            print("4.Model2")
            self.m=input("enter your choice:")
            if(self.m==3):
                self.cost(self.m)
                break
            elif(self.m==4):
                self.cost(self.m)
                break
            else:
                print(" invalid..Re-enter")
                break
    def cost(self,m):
        if(m==1):
            self.cost=142000
        elif(m==2):
            self.cost=200000
        elif(m==3):
            self.cost=154000
        else:
            self.cost=180000
        total_cost=self.cost+self.agst+self.cgst+self.insurance
        print(total_cost)
o=car_company()
o.company()
