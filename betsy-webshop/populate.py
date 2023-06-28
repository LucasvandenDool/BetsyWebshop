import models

def populate_test_database():
    
    ### USERS
    models.User.create(name= 'Betsy', street= 'Vuurdoornweg', housenumber= 12, postal= '3012JJ', card= 1234123412341234)
    models.User.create(name= 'Suzan', street= 'Drive', housenumber= 10, postal= '1234AB', card= 4321432143214321)
    models.User.create(name= 'Willy', street= 'Weg', housenumber= 2, postal= '1871TS', card= 5678567856785678)
    models.User.create(name= 'Jasper', street= 'Blinkerd', housenumber= 218, postal= '9999AA', card= 8765876587658765)
    models.User.create(name= 'Yara', street= 'Straat', housenumber= 69, postal= '4321BA', card= 4567456745674567)
    models.User.create(name='Lucas', street= 'Boomgaardhof', housenumber= 37, postal= '1848TT', card= 1234567812345678)
    
    ### Products
    models.Product.create(owner = 1, name= 'Cheese', description = 'Delicious creamy cheese', price = 8.95, amount = 25)
    models.Product.create(owner = 5, name= 'Sweater', description = 'Knitted sweater', price = 29.50, amount = 3)
    models.Product.create(owner = 2, name= 'Limoncello', description = 'Homemade lemon liquor', price = 12.0, amount = 15)
    models.Product.create(owner = 2, name= 'Beer', description = 'Homemade hipster beer', price = 6.50, amount = 48)
    models.Product.create(owner = 3, name= 'Apples', description = 'Fresh healthy apples', price = 1.95, amount = 100)
    models.Product.create(name= 'Pears', description = 'Fresh healthy pears', price = 2.5, amount = 50)


    ### Tags
    models.Tags.create(name = 'delicious')
    models.Tags.create(name = 'knitted')
    models.Tags.create(name = 'homemade')
    models.Tags.create(name = 'lemon')
    models.Tags.create(name = 'liquor')
    models.Tags.create(name = 'hipster')
    models.Tags.create(name = 'food')
    models.Tags.create(name = 'drinks')
    models.Tags.create(name = 'clothes')
    models.Tags.create(name = 'fresh')    
    models.Tags.create(name = 'healthy')    
    models.Tags.create(name = 'furniture')    
    models.Tags.create(name = 'fruit')

    ### Product Tags
    models.Product_tag.create(product= 1, tag = 1)
    models.Product_tag.create(product= 7, tag = 1)
    models.Product_tag.create(product= 2, tag = 2)
    models.Product_tag.create(product= 2, tag = 9)
    models.Product_tag.create(product= 2, tag = 3)
    models.Product_tag.create(product= 3, tag = 3)
    models.Product_tag.create(product= 3, tag = 4)
    models.Product_tag.create(product= 3, tag = 5)
    models.Product_tag.create(product= 4, tag = 3)
    models.Product_tag.create(product= 4, tag = 6)
    models.Product_tag.create(product= 4, tag = 5)
    models.Product_tag.create(product= 3, tag = 8)
    models.Product_tag.create(product= 4, tag = 8)
    models.Product_tag.create(product= 1, tag = 7)
    models.Product_tag.create(product= 5, tag = 10)
    models.Product_tag.create(product= 5, tag = 11)
    models.Product_tag.create(product= 5, tag = 13)
    models.Product_tag.create(product= 5, tag = 7)
    models.Product_tag.create(product= 5, tag = 1)
    models.Product_tag.create(product= 3, tag = 1)
    models.Product_tag.create(product= 4, tag = 1)

    print('Filled database with data.')

    return