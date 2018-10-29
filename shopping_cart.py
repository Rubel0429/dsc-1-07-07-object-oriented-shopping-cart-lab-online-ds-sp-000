class ShoppingCart:
    
    prices = []
    
    def __init__(self, employee_discount = None):
        self._items = []
        self._total = 0
        self._prices = []
        self._discount = employee_discount
    
    def total(self):
        return self._total
    def set_total(self, amount):
        self._total += amount
    
    def employee_discount(self):
        return employee_discount
    
    def item_names(self):
        return self._items
    
    def add_item(self, item, price, quantity=None):
        if quantity == None:
            self.set_total(price)
            self._items.append(item)
            self._prices.append(price)
            return self.total()
        else:
            self.set_total(price*quantity)
            self._items += quantity * [item]
            self._prices += quantity * [price]
            return self.total()
        
    def mean_item_price(self):
        return self._total/(len(self._items))
    
    def median_item_price(self):
        x = sorted(self._prices)
        if len(self._prices)%2 == 1:
            y = int((len(self._prices)/2)-0.5)
            return self._prices[y]
        else:
            z1 = int(len(self._prices)/2)
            z2 = int((len(self._prices)/2)-1)
            return (self._prices[z1]+self._prices[z2])/2
    def apply_discount(self):
        if self._discount == None:
            return "Sorry, there is no discount to apply to your cart :("
        else:
            return self._total*((100-self._discount)/100)
    def void_last_item(self):
        if len(self._items) == 0:
            return "There are no items in your cart!"
        else:
            self._prices.pop()
            self._total = sum(self._prices)