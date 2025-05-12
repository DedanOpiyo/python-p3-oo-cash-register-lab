#!/usr/bin/env python3

class CashRegister:
  def __init__(self, discount = 0):
    self.discount = discount
    self.total = 0
    self.items = [] # keep track of items
    self.last_transaction = [] # keep track of last transaction

  def apply_discount(self):
    if self.discount:
        self.total = int(self.total * ((100 - self.discount) / 100))
        print(f"After the discount, the total comes to ${self.total}.")
        # return int(self.total * ((100 - self.discount) / 100)) # discount should return total price with discount other than modifying it. void_last_transaction does not take account of this.
    else:
        print("There is no discount to apply.")

  def add_item(self, title, price, quantity = 1):
    self.last_transaction.append({"title": title, "price": price * quantity, "quantity": quantity})
    
    self.total += price * quantity # update total

    for _ in range(quantity):
      self.items.append(title) # include item per the number specified in quantity

  def list_with_multiples(self):
    return self.items # array of items

  def void_last_transaction(self):
    if self.last_transaction:
      self.total -= self.last_transaction[-1]["price"] 
      
      for _ in range(self.last_transaction[-1]["quantity"]):
        self.items.pop()
      
      self.last_transaction.pop()
    else:
        print("You have no transactions yet. Call add_item to include one.")


# Test
cashRegister = CashRegister(20)
cashRegister.add_item("eggs", 3, 4)
cashRegister.add_item("eggs", 3)
# => 5 eggs. peice 15, after discount, 12
cashRegister.add_item("macbook air", 1000)
print(cashRegister.total)

print(cashRegister.items) # print items
print(f"Last transaction is: {cashRegister.last_transaction}")
print(f"Last item transacted: {cashRegister.last_transaction[-1]}")
print(f"Total before discount: {cashRegister.total}")

print(cashRegister.apply_discount()) # apply discount # prints none, unless we return something. # after void, total will be a -ve
print(cashRegister.total)

print("------------------")
cashRegister.void_last_transaction()
print(cashRegister.total)
print(cashRegister.items)


# Additional Discount Logic(on each item)
# to apply discount on an individual item, you can include a function and call it with...
# price and discount, from add_item. This could mean removing the pre-set discount at initialization. Total is then updated

## Additional logic to voids last transaction
# We would need to track when discount was given(and keep track of that discount) so that we can add it to the current total before 'voiding' the last transaction or...
# before void_last_transaction() voids the last transaction
