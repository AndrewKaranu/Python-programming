# Object Oriented Programming
# A programming paradigm that involves objects and classes
# Class-> template/blueprint for creating object
# Object-> a real world entity or is an instance of a class


# Constructor-> A special method that executes first when an object has been created(instanciation)

class MyRouter:
    """This class describes the characteristics of a router""" #-> Tripple qoutes to define the class
    def __init__(self, routername, model, serialNo, ios): 
        # The class attributes/properties (one the left)
        self.routername = routername
        self.model = model
        self.serialNo = serialNo
        self.ios = ios
    
    #->The self parameter is a reference to the current instance of the class, and is used to access variables that belong to the class.

    # Class method
    # def print_router(self, manu_date):
    #     """This method displays the router information"""
    #     print(f"The name of the router is: {router1.routername}")
    #     print(f"The router model is: {router1.model}")
    #     print(f"The serial no of the router is: {router1.serialNo}")
    #     print(f"The ios version is: {router1.ios}")
    #     print(f"The model and date combined is: {router1.model}{manu_date}")
                
    def print_router(self, manu_date):
        """This method displays the router information"""
        print("The name of the router is: ", self.routername)
        print("The router model is: ", self.model)
        print("The serial no of the router is: ", self.serialNo)
        print("The ios version is: ", self.ios)
        print("The model and date combined is:", self.model + manu_date)
        
        
# Creating an object
# router1 = MyRouter("r1", "2600", "123456", "12.4")
# print(router1)
# print(router1.routername)
# print(router1.serialNo)
# print(router1.model)
# print(router1.ios)
# router1.print_router("78926")

# router2 = MyRouter("r2", "3600","101010","12.3")
# print(router2)
# print(router2.routername)
# print(router2.serialNo)
# print(router2.model)
# print(router2.ios)
# router2.print_router("78926")

# Inheritance-> Acquiring the properties of another class
# Child class/subclass-> Inherits
# Parent class/super class-> Inherits from

# Create a child class
class MyNewRouter(MyRouter): #->To create a child class you put the parent class namein the parenthesis
    """This is a child class inherititng from MyRouter Class"""
    def __init__(self, routername, model, serialNo, ios, portsNo):
        MyRouter.__init__(self, routername, model, serialNo, ios) #->You can also start with super().
        self.portsNo = portsNo
        
    # Our child class method
    # def print_new_router(self, string):
    #     print(string + self.model)
    def __str__(self):
        return f"{self.routername} has ({self.portsNo} ports)"

# Create child object-
MyNewRouter1 = MyNewRouter("newr1", "1800", "678909", "12.2", "10")
# print(MyNewRouter1)
# print(MyNewRouter1.routername)
# print(MyNewRouter1.serialNo)
# print(MyNewRouter1.model)
# print(MyNewRouter1.ios)
# MyNewRouter1.print_new_router("78926")
print(MyNewRouter1)
