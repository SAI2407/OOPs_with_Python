import csv

class Item:
   
   # This is a class attribute can be accessed using class or instance

   payable_amount = 0.90 # This fraction of amount should be payed after 10% discount on a single purchase of item

   list_instances = []

   def __init__(self , name : str , price : float , quantity = 0):

          # Checking the validations of received arguments

          assert price >=0 , f"Price {price} is not greater than or equal to zero !"
          assert quantity >= 0 , f"Quantity {quantity} is not greater than or equal to zero !"


          # Assigning attritubes for an instance
             
          self.__name = name
          self.__price =  price
          self.quantity = quantity

          # Appending

          Item.list_instances.append(self)


    # Using decorator @property the method is set to read-only you cant change it
   @property

   def get_name (self):
        return self.__name
   
   @get_name.setter

   def set_name(self , value):
        
        if len(value) > 10:
             raise Exception("The Name is too long !")
        
        else :
             self.__name = value

   @property

   def get_price (self):
        return self.__price
   
   



          
   def calculate_total_price(self):

        return self.__price * self.quantity
   
   def apply_discount(self):
        
        self.__price = self.__price * self.payable_amount
        
        return self.__price
   
   def apply_increment(self, increment):
        
        self.__price = self.__price + self.__price * increment

        return self.__price
        
   # This is a magic method to output instance as we want 

   def __repr__(self):
        
        return f"{self.__class__.__name__}('{self.__name}', '{self.__price}' , '{self.quantity}')"
   
   # Creating a class method to read csv file and create instances.

   @classmethod
   def Instantiate_from_csv(cls):
        
        with open("items.csv" , "r") as f :
             
             # Reading a csv file as dictionary

             reader = csv.DictReader(f)
             items = list(reader)

             # Creating instances

             for item in items:
                  Item(name = item.get("Name"),
                       price = float(item.get("Price")),
                       quantity = int(item.get("Quantity"))
                       )

  
  # Static methods doesnt take class or object as an argument.However class methods take class as first argument

   @staticmethod
   def is_it_integer(num):
        if isinstance(num , float):
             # checking the fractional part of float if it is zero then float is an integer

             return num.is_integer()
        
        elif isinstance(num, int):
            return True
        else:
            return False
        