class Garage:
    def __init__(self,bikes,cars,trucks):
        self.bikes=bikes
        self.cars=cars
        self.trucks=trucks
def MaxRev(l1):
        if l1 is None:
            return -1
        max_revenue=1
        for i in l1:
            revenue=(100*i.bikes)+(250*i.cars)+(500*i.trucks)
            if revenue>max_revenue:
                max_revenue=revenue
        return max_revenue
    
l1=[Garage(bikes=8,cars=3,trucks=2),Garage(bikes=10,cars=1,trucks=5)]
print(MaxRev(l1))

     