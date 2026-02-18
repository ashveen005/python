from datetime import datetime
import csv
from .inventory import Inventory, StockItem
class Order:
    def __init__(self,date_string, stock_item_id, quantity):
        self.Order_date = datetime.strptime(date_string, "%m/%d/%Y").date()
        self.stock_item_id = str(stock_item_id)
        self.quantity: float = float(quantity)

    def __str__ (self):
        return f"Order(stock item id: {self.stock_item_id}, date: {self.Order_date})"
    def __repr__(self):
        return self.__str__()
    
class OrdersList:
    def __init__(self, inventory: Inventory):
        self.inventory = inventory
        self.orders = []

    def import_orders(self, csv_file):
        with open(csv_file, "r") as file:
            reader = csv.reader(file)
            next(reader)     
            for row in reader:
                date_string = row[0]
                stock_item_id = row[1]
                quantity = float(row[2])   

                order = Order(date_string, stock_item_id, quantity)
                self.orders.append(order)

            return self.orders
        
    def get_number_of_orders_by_sku(self, stock_item_id):
        count = 0
        for order in self.orders:
            if order.stock_item_id == stock_item_id:
                count += 1
        return count 
    
    def get_orders_price_by_sku(self, stock_item_id):
        total_price = 0.0
        stock_item = self.inventory.get.stock_by_id(stock_item_id)
        if stock_item:
            unit_price = stock_item.unit_price
            for order in self.orders:
                if order.stock_item_id == stock_item_id:
                    total_price += order.quantity * stock_item.unit_price
        return round(total_price, 2)
        
    def __str__(self):
        return f"OrdersList(orders: {len(self.Orders)})"
    
    def __repr__(self):
        return self.__str__()

       