class Bikeshop:
    def __init__(self,total_available_stock,Honda,Pulsar,Avenger,Royal_Enfield):
        self.total_available_stock = total_available_stock
        self.Honda = Honda
        self.Pulsar = Pulsar
        self.Avenger = Avenger
        self.Royal_Enfield = Royal_Enfield

    # available stock function
    def show_stock(self):
        print('The available stock in shop is:',self.total_available_stock)
        print('The available stock in shop is for Honda:', self.Honda)
        print('The available stock in shop is for Pulsar:', self.Pulsar)
        print('The available stock in shop is for Avenger:', self.Avenger)
        print('The available stock in shop is for Royal Enfield:', self.Royal_Enfield)

    #rent function
    def rent_bike(self,quantity,days,price):
        if quantity <= 0:
            print('Please enter value more than zero')
        if quantity > self.total_available_stock:
            print('Please enter the stock less than available stock')
        else:
            print('Total price to pay:',quantity*days*price)
            print('Total bike stock available:',self.total_available_stock - quantity)
            if model == 1:
                print('Total bike stock available for Honda:', self.Honda - quantity)
                print('Total bike stock available for Pulsar:', self.Pulsar )
                print('Total bike stock available for Avenger:', self.Avenger )
                print('Total bike stock available for Royal Enfield:', self.Royal_Enfield )
            elif model == 2:
                print('Total bike stock available for Honda:', self.Honda )
                print('Total bike stock available for Pulsar:', self.Pulsar - quantity)
                print('Total bike stock available for Avenger:', self.Avenger)
                print('Total bike stock available for Royal Enfield:', self.Royal_Enfield)
            elif model == 3:
                print('Total bike stock available for Honda:', self.Honda )
                print('Total bike stock available for Pulsar:', self.Pulsar)
                print('Total bike stock available for Avenger:', self.Avenger - quantity)
                print('Total bike stock available for Royal Enfield:', self.Royal_Enfield)
            else:
                print('Total bike stock available for Honda:', self.Honda)
                print('Total bike stock available for Pulsar:', self.Pulsar)
                print('Total bike stock available for Avenger:', self.Avenger)
                print('Total bike stock available for Royal Enfield:', self.Royal_Enfield - quantity)

while True:
    obj = Bikeshop(100,25,25,25,25)
    uc = int(input('''
    1 Display available stock
    2 Rent the bikes
    3 Exit
    '''))
    if uc == 1:
        obj.show_stock()

    elif uc == 2:
        list = ['1-Honda ₹1000', '2-Pulsar ₹1500', '3-Avenger ₹2000', '4-Royal Enfield ₹3000']
        for i in list:
            print(i)
        model = int(input('Choose bike model:'))
        if model == 1:
            price = 1000
        elif model == 2:
            price = 1500
        elif model == 3:
            price = 2000
        else:
            price = 3000
        n = int(input('Enter the bike Quantity:--'))
        d = int(input('Enter the rent days:--'))
        obj.rent_bike(n,d,price)
    else:
        break
