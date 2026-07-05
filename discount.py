 def apply_bulk_discount(cart_total, item_count):
       if item_count >= 10:
           return cart_total * 0.9
       return cart_total
