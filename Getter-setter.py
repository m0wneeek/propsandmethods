#Properties should have getter and setter methods
#Code should include proof of testing. Class instances should be created and each method and property should be shown to work as expected

#If the product weighs less than or equal to 1000 grams, the cost is 5
#If the product weighs more than 1000 grams, but less than 5000 grams, the cost is 8
#If the product weighs 5000 grams or more, the cost is 10
#The polymorphic method of the Book child class should determine the shipping cost, which has a flat rate of 3 for paperbacks and 4 for hardbacks.

##I spent a lot of time doing the wrong thing with the method and price/weight properties because I misunderstood that price and shipping costs were separate things.

class Product:

    """A class describing a product
    
    Properties:
        _item_name: str. product name
        _description: str. product description
        _price: int, product price
        _weight_in_grams: int, between 0<w<5000, weight of the book in grams
        
    methods:
        calculate_shipping(): calculates the shipping based on a given algorithm
        getter and setter methods"""
        
        #i forgot that i needed to include the property names inside of the initialisation brackets. I looked back on the sugar example to see this
        
    def __init__(self, item_name, description, price, weight_in_grams):
        """initialises the properties"""
        self._item_name = item_name
        self._description = description
        self._price = price
        self._weight_in_grams = weight_in_grams
        
    @property
    def item_name(self):
        """item name getter"""
        return self._item_name
    
    @item_name.setter
    def item_name(self, new_value):
        self._item_name = new_value
        
    @property
    def description(self):
        """description getter"""
        return self._description
        
    @description.setter
    def description(self, new_value):
        self._description = new_value
        
    @property
    def price(self):
        """price getter"""
        return self._price 
        
    @price.setter
    def price(self, new_value):
        self._price = new_value
        
    @property
    def weight_in_grams(self):
        """weight in grams getter"""
        return self._weight_in_grams
    
    @weight_in_grams.setter
    def weight_in_grams(self, new_value):
        self._weight_in_grams = new_value
        """
        weight in grams setter method

        Args:
            new_value: int specifying the weight
        Returns:
            new weight
        Raises:
            None
        """
        
##i originally got confused and tried to create the method in here, using if isinstance etc within this setter. I had the if, elif, else for each step of the method but in the wrong place.
            
    def calculate_shipping(self):
        """ calculates the shipping. printing each item for extra pizzazz
        
        Args: Weight 
        
        Returns: shipping cost
        """
        print("calculating shipping")
        
        """if the weight is less than or equal to 1000, the shipping cost returns 5. 
        
        else if the weight is below 5000, the shipping cost returns as 8. 
        
        else, the shipping cost returns 10.
        """
        
        if self._weight_in_grams <=1000:
            return 5 
        elif self._weight_in_grams < 5000:
            return 8
        else:
            return 10

my_product = Product()
my_product._calculate_shipping()
        

class Book(Product):
    
    """One child class for a book product

    New Properties:
        _ISBN: str, international standard book number
        _is_paperback: Boolean, paperback or hardback
    
    New Methods: 
        polymorphic calculate_shipping(). flat rate for paperbacks vs hardbacks
        getter and setter methods"""
        
    def __init__(self, item_name, description, price, weight_in_grams, ISBN, is_paperback):
        """ Initialises the properties """
        super().__init__(item_name, description, price, weight_in_grams)
        self._ISBN = ISBN
        self._is_paperback = is_paperback
        #self._is_papeback = is_paperback so that if this is checked as True, the boolean is True. if it is false it is recognised as a hardback
    """creating getter and setter methods for both new properties"""
    
    @property
    def ISBN(self):
        return self._ISBN
        
    @ISBN.setter
    def ISBN(self, new_value):
        self._ISBN = new_value
        
    @property
    def is_paperback(self):
        return self._is_paperback
        
    @is_paperback.setter
    def is_paperback(self, new_value):
        self._is_paperback = new_value
    
    """creating polymorphic method by calling the parent method but changing the actual method itself"""
    
    def calculate_shipping(self):
        """method has a flat rate of 3 for paperbacks and 4 for hardbacks"""
        if self._is_paperback:
            return 3
        else:
            return 4
            
my_book = Book("Children of Time", "A really good sci-fi book about spiders and space", 20, 300, "1447273303", False)
my_book1 = Book("Children of Memory", "A great sequel", 25, 400, "1529087198", True)

print("Shipping Cost for this book is:", my_book.calculate_shipping(), "pounds")

print("Shipping Cost for this book is:", my_book1.calculate_shipping(), "pounds")
    
