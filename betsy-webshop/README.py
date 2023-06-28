import models
import populate
from main import *


# Reboot and create new database
models.start_up()

# Fill database with data
populate.populate_test_database()

#search(search)

#list_user_products(user_id)

#list_products_per_tag(tag_id)

#add_product_to_user_catalog(user_id, product_id)

#update_stock(product_id, new_amount)

#purchase_product(product_id, buyer_id, seller_id, amount)

#remove_product(product_id)