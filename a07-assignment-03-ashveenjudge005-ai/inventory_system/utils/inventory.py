class StockItem:
    def __init__(self,id,current_units,unit_price):
        self.id=id
        self.current_units=float(current_units)
        self.unit_price=float(unit_price)

    def get_stock_value(self):
        return round(self.current_units * self.unit_price, 2)
    
    def __str__(self):
        return f"StockItem({self.id})"
    
    def __repr__(self):
        return f"StockItem({self.id})"
    

class Inventory:
    def __init__(self):
        self.stock=[]

    def import_stock(self,csv_file_name):
        import csv
        with open(csv_file_name, "r") as file:
            reader= csv.reader(file)
            next(reader)

            for row in reader:
                stock_id = row[0]
                current_units = float(row[1])
                unit_price = float(row[5])

                item = StockItem(stock_id,current_units,unit_price)
                self.stock.append(item)

        return self.stock
    
    def get_stock_by_id(self, stock_item_id):

        for item in self.stock:
            if item.id == stock_item_id:
                return item
            
        return None
    
    def __str__(self):
        return f"Inventory(stock: {len(self.stock)})"
    def __repr__(self):
        return self.__str__()


    