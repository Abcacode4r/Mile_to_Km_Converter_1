def add(*args):
    sum=0
    for n in args:
        sum+=n
    return sum
add(2,3,4)

def calculate(n,**kwargs):
   print(kwargs)
   n *= kwargs["multiply"]
   n+=kwargs["add"]

   print(n)

calculate(2,add=3,multiply=5)

class car:
    def __init__(self,**kw):
        self.make=kw["make"]
        self.model=kw["model"]
        self.color=kw["color"]

my_car=car(make="Chevrolet",model="Challenger",color="Red")
print(my_car.color)