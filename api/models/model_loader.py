from . import (order_pickup, orders, order_details, recipes, resources, payment, menu_item,
               administration, third_party_delivery_service, user,
               reviews, payment, staff)

from ..dependencies.database import engine


def index():
    orders.Base.metadata.create_all(bind=engine, checkfirst=True)
    order_details.Base.metadata.create_all(bind=engine, checkfirst=True)
    recipes.Base.metadata.create_all(bind=engine, checkfirst=True)
    resources.Base.metadata.create_all(bind=engine, checkfirst=True)
    payment.Base.metadata.create_all(bind=engine, checkfirst=True)
    menu_item.Base.metadata.create_all(bind=engine, checkfirst=True)
    administration.Base.metadata.create_all(bind=engine, checkfirst=True)
    order_pickup.Base.metadata.create_all(bind=engine, checkfirst=True)
    third_party_delivery_service.Base.metadata.create_all(bind=engine, checkfirst=True)
    user.Base.metadata.create_all(bind=engine, checkfirst=True)
    reviews.Base.metadata.create_all(bind=engine, checkfirst=True)
    staff.Base.metadata.create_all(bind=engine, checkfirst=True)
    order_pickup.Base.metadata.create_all(bind=engine, checkfirst=True)