__winc_id__ = "d7b474e9b3a54d23bca54879a4f1855b"
__human_name__ = "Betsy Webshop"

from datetime import datetime
import models


##### SEARCH
def search(search):
    search = search.lower()
    query = models.Product.select().where(models.Product.name.contains(search) | models.Product.description.contains(search))

    if query:
        print('Search related results:\n')
        
        for product in query:
            print(f'Product: {product.name}\nDescription: {product.description}\n')

    else:
        print('No products found.')


##### USER PRODUCTS
def list_user_products(user_id):
    query = models.Product.select().where(models.Product.owner == user_id)

    if query:
        user = models.User.get_by_id(user_id)
        print(f'{user.name} holds these items:')
        
        for product in query:
            print(f'{product.storage} X {product.name}')
    
    else:
        print('No results. This user has no items or the given ID was not correct')


##### PRODUCTS PER TAG
def list_products_per_tag(tag_id):
    query = models.Product.select().join(models.Product_tag).join(models.Tags).where(models.Tags.id == tag_id)
    
    if query:
        tag = models.Tags.get_by_id(tag_id)
        
        for product in query:
            print(f'{tag.name} matches with {product.name}')
    
    
    else:
        tag = models.Tags.get_by_id(tag_id)
        print(f'The tag "{tag.name}" does not match any products')


##### PRODUCT TO USER
def add_product_to_user_catalog(user_id, product_id):
    user = models.User.get_by_id(user_id)
    product = models.Product.get_by_id(product_id)
    product.owner = user
    product.save()
    print(f'The user {user.name} now holds {product.amount} times {product.name}.')
    

##### UPDATE STOCK
def update_stock(product_id, new_amount):
    product = models.Product.get_by_id(product_id)
    product.amount = new_amount
    product.save()
    print(f"Product amount has been updated. {product.name}'s new amount is {product.amount}.")
    

##### PURCHASE PRODUCT
def purchase_product(product_id, buyer_id, seller_id, amount):
    product = models.Product.get_by_id(product_id)
    buyer = models.User.get_by_id(buyer_id)
    seller = models.User.get_by_id(seller_id)
    
    
    if buyer.name == seller.name:
        print('You can not purchase your own items.')
    
    if amount > product.amount:
        print(f'Not enough {product.name} in stock to fullfil the purchase.')

    total = round(product.price * amount, 2)
    new_amount = product.amount - amount
    date = datetime.today()
    date = date.strftime("%d/%m/%Y, %H:%M:%S")

    print(f'Purchase completed!\n{buyer.name} is now the owner of {amount} {product.name}.')
    print(f'{seller.name} made ${total}!\n')
    
    transaction = models.Transaction.create(
        product = product.name, 
        buyer = buyer.name, 
        seller = seller.name, 
        amount = amount, 
        price = product.price, 
        total = total, 
        date = date)
        
    update_stock(product_id, new_amount)
    print(transaction.date)
    


##### REMOVE PRODUCT
def remove_product(product_id):
    product = models.Product.get_by_id(product_id)
    print(f'{product.name} has been removed from the database.')
    product.delete_instance()
    