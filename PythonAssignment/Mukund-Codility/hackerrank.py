import sys
def read():
    sys.stdin  = open('./input.txt', 'r')
    sys.stdout = open('./output.txt', 'w')
    
# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.

import os
class Limit:
    limit: int
    @classmethod
    def set_limit(cls, x: int) :
        cls.limit = x

    @classmethod
    def get_limit(cls) :
        return cls.limit

class UserLimitExceeded(Exception):
    @classmethod
    def __init__(self, message):
        self.message = message

class Product:
    @classmethod
    def __init__(self, name):
        self.name = name

    @classmethod
    def __del__(self):
        #print("Deleting Object...")
        return
    


def main():
    max_limit = int(input())
    Limit.set_limit(max_limit)
    products = {}
    
    def new_product(product_name: str) -> str:
        if len(products) < Limit.get_limit():
            product = Product(product_name)
            products[product_name] = product
            return f"{product.name} created"
        else:
            raise UserLimitExceeded(f"Product {product_name} cannot be created")
    
    def del_product(product_name: str) -> str:
        product = products.get(product_name, f"{product_name} not found")
        if isinstance(product, Product):
            del products [product_name]
            return f"{product_name} deleted successfully"
        raise Exception(product)

    def print_product (product_name: str) -> str:
        product = products. get (product_name, f" {product_name} not found")
        if isinstance (product, Product) :
            return f"{product.name} found"
        raise Exception (product)

    def change_limit(limit: int) -> str:
        limit = int(limit)
        Limit.set_limit(limit)
        return f"limit updated to {limit}"
    
    func_map = {
        "new": new_product,
        "del": del_product,
        "print": print_product,
        "limit": change_limit,
    }
    
    num_operations = int(input ())
    
    for i in range (num_operations):
        cmd, arg = input().split()
        try:
            res = func_map[cmd](arg)
            print (res)
        except UserLimitExceeded as ule:
            print (ule)
        except Exception as e:
            print (e)
    
    print("End of Code")



if __name__ == "__main__":
    read()
    main()


