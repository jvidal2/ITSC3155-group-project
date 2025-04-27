from . import orders, order_details


def load_routes(app):
    app.include_router(orders.router)
    app.include_router(order_details.router)
    app.include_router(administration.router)
    app.include_router(resources.router)
