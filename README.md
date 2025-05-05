### Restaurant Ordering System

This is the Final Project for ITSC3155, a backend API for managing a sandwich making system. It handles menu items, recipes, resources, orders, payments, promotions, users, reviews, staff, delivery, and more using FastAPI and SQLAlchemy with a MySQL database.

### Features
##### CRUD operations for:
* Menu Items
* Recipes linking menu items to resources
* Resources inventory
* Orders and order details
* User accounts and administration
* Reviews and ratings
* Promotions and discounts
* Staff and delivery management

Search and filter menu items by name or exclude ingredients. Clear relationships using SQLAlchemy with foreign key integrity. Modular structure with routers, controllers, models, and schemas. Swagger documentation available at /docs. Error handling with descriptive API responses.

### Technologies Used
* `Python 3.11+`
* `FastAPI`
* `SQLAlchemy`
* `MySQL`
* `Pydantic`


### Setup Instructions
#### Clone the repository
	
git clone https://github.com/jvidal2/ITSC3155-group-project
cd FinalProject


#### Create a virtual environment

python -m venv .venv
source .venv/bin/activate      (Linux/macOS)
.venv\Scripts\activate            (Windows)


#### Install dependencies

pip install -r requirements.txt


Set up MySQL database
Create the sandwich_maker_api database
Let SQLAlchemy create the tables
Run the FastAPI server

uvicorn api.main:app –reload


### Access API docs
Open http://127.0.0.1:8000/docs to explore and test the endpoints

### Contributors
* Jazmin Vidal
* Alice Chen
* Dijonay Dawson
* Sara Eriksousi
* Trinity Thao