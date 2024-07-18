from item import Item

# Creating a Phone class to have some special attributes for the phone

class Phone(Item):
      
      def __init__(self , name : str , price : float , quantity =0 , network : str = "4g" ):
           
           assert network == "5g" or network == "4g" , f"The {network} is invalid"
           
           super().__init__(name , price , quantity)
           self.network = network
             