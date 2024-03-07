import pytest
from Product import Product

# Define fixtures
@pytest.fixture
def sample_product_data():
    return {'nome': 'TestProduct', 'prezzo': 100, 'marca': 'TestBrand'}

# Test cases
def test_create_product(sample_product_data):
    created_product = Product.create(sample_product_data)
    assert isinstance(created_product, dict)
    assert 'id' in created_product
    assert isinstance(created_product['id'], int)

def test_find_product():
    # Assuming product with id=1 exists in the database
    found_product = Product.find(1)
    assert found_product is not None
    assert isinstance(found_product, tuple)# Assuming it returns a tuple

def test_fetch_all_products():
    all_products = Product.fetchAll()
    assert isinstance(all_products, list)
    for product in all_products:
        assert isinstance(product, tuple)# Assuming it returns a list of tuples

def test_update_product(sample_product_data):
    # Create a product to update
    created_product = Product.create(sample_product_data)
    created_product['prezzo'] = 200  # Update the price
    Product.update(created_product)
    
    # Retrieve the updated product
    updated_product = Product.find(created_product['id'])
    assert updated_product is not None
    assert isinstance(updated_product, list)
    assert updated_product['prezzo'] == 200  # Assuming price is at index 2

def test_delete_product(sample_product_data):
    # Create a product to delete
    created_product = Product.create(sample_product_data)
    
    # Delete the product
    Product.delete(created_product)
    
    # Try to find the deleted product
    deleted_product = Product.find(created_product['id'])
    assert deleted_product is None
