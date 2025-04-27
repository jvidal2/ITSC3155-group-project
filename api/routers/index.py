from . import orders, order_details, administration, resources, sandwiches, payment, third_party_delivery_service, reviews, recipes, user, staff, delivery


def load_routes(app):
    app.include_router(orders.router)
    app.include_router(order_details.router)
    app.include_router(administration.router)
    app.include_router(resources.router)
    app.include_router(sandwiches.router)
    app.include_router(payment.router)
    app.include_router(third_party_delivery_service.router)
    app.include_router(reviews.router)
    app.include_router(recipes.router)
    app.include_router(user.router)
    app.include_router(staff.router)
    app.include_router(delivery.router)


