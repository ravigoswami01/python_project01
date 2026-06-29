class Persion:
    def __init__(self , fast_name, Last_name ,age):
        self.fast_name = fast_name;
        self.last_name = Last_name;
        self.age = age;



P1 = Persion("ravi" , "Kumar", 22)

print(P1.fast_name ,)


class Laptop:
    def __init__(self , brand_name , model_name , price):
        self.brand_name=brand_name;
        self.model_name = model_name;
        self.price = price


Ravi =Laptop("dell" , "353562 R3" , "68000") 


print(Ravi.brand_name,Ravi.model_name,Ravi.price)