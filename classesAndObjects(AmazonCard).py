class card:
    def __init__(self,curid,imageurl,devicetype,price,rating):
        self.id=curid
        self.imageurl=imageurl
        self.devicetype=devicetype
        self.price=price
        self.rating=rating
        
    def printalldetails(self):
        print("Product -",self.id,":")
        print("imageUrl:",self.imageurl)
        print("deviceType:",self.devicetype)
        print("price:",self.price)
        print("rating:",self.rating)
        print()
mobilephone=card(1,"Dummy-url 1","Mobile",56000,4.5)
mobilephone.printalldetails()


laptop=card(2,"Dummy-url 2","Laptop",94000,4.8)
laptop.printalldetails()


smartwatch=card(3,"Dummy-url 3","Smart-watch",18000,3.5)
smartwatch.printalldetails()
