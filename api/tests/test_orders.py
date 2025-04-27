from fastapi.testclient import TestClient
from ..controllers import orders as controller
from ..main import app
import pytest
from ..models import orders as model

# # Create a test client for the app
# client = TestClient(app)
#
#
# @pytest.fixture
# def db_session(mocker):
#     return mocker.Mock()
#
#
# def test_create_order(db_session):
#     # Create a sample order
#     order_data = {
#         "customer_name": "John Doe",
#         "description": "Test order"
#     }
#
#     order_object = model.Order(**order_data)
#
#     # Call the create function
#     created_order = controller.create(db_session, order_object)
#
#     # Assertions
#     assert created_order is not None
#     assert created_order.customer_name == "John Doe"
#     assert created_order.description == "Test order"


# Create a test client for the app
client = TestClient(app)

def test_create_order():
    # sample order
    order_data = {
        "customer_name": "John Doe",
        "description": "Test order"
    }
    # send the sample order to the /orders/ endpoint
    response = client.post("/orders/", json=order_data)

    # check if the response was successful
    assert response.status_code == 200

    # check if the data returned matches what we sent
    data = response.json()
    assert data["customer_name"] == "John Doe"
    assert data["description"] == "Test order"

