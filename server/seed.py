#!/usr/bin/env python3

from app import app
from models import db, Customer, Review, Item

with app.app_context():
    db.session.query(Customer).delete()
    db.session.query(Review).delete()
    db.session.query(Item).delete()

    customer1 = Customer(name='Tal Yuri')
    customer2 = Customer(name='Raha Rosario')
    customer3 = Customer(name='Luca Mahan')

    item1 = Item(name='Laptop Backpack', price=49.99)
    item2 = Item(name='Insulated Coffee Mug', price=9.99)
    item3 = Item(name='6 Foot HDMI Cable', price=12.99)

    review1 = Review(comment="zipper broke the first week", customer=customer1, item=item1)
    review2 = Review(comment="love this backpack!", customer=customer2, item=item1)
    review3 = Review(comment="coffee stays hot for hours!", customer=customer1, item=item2)
    review4 = Review(comment="best coffee mug ever!", customer=customer3, item=item2)
    review5 = Review(comment="cable too short", customer=customer3, item=item3)

    db.session.add_all([customer1, customer2, customer3, item1, item2, item3])
    db.session.add_all([review1, review2, review3, review4, review5])
    db.session.commit()
