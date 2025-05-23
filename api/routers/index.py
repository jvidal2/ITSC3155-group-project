from . import (orders, order_details, administration, resources, payment,
               third_party_delivery_service, reviews, recipes, user, staff,
               menu_item, promotions, order_pickup, order_tracking)


def load_routes(app):
    app.include_router(user.router)
    app.include_router(menu_item.router)
    app.include_router(orders.router)
    app.include_router(order_details.router)
    app.include_router(order_pickup.router)
    app.include_router(order_tracking.router)
    app.include_router(promotions.router)
    app.include_router(payment.router)
    app.include_router(reviews.router)

    app.include_router(administration.router)
    app.include_router(staff.router)
    app.include_router(third_party_delivery_service.router)
    app.include_router(resources.router)
    app.include_router(recipes.router)