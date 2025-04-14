from . import orders, order_details, recipes, sandwiches, resources, payment, menu_item, user, reviews
from . import payments
from ..dependencies.database import engine


def index():
    orders.Base.metadata.create_all(engine)
    order_details.Base.metadata.create_all(engine)
    recipes.Base.metadata.create_all(engine)
    sandwiches.Base.metadata.create_all(engine)
    resources.Base.metadata.create_all(engine)
    payment.Base.metadata.create_all(engine)
    menu_item.Base.metadata.create_all(engine)
    administration.Base.metadata.create_all(engine)
    delivery.Base.metadata.create_all(engine)
    third_party_delivery_service.Base.metadata.create_all(engine)
    user.Base.metadata.create_all(engine)
    reviews.Base.metadata.create_all(engine)
