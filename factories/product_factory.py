from factories.connection import get_connection
from models.product import Product

class ProductFactory:
    def list_all_product():
        db = get_connection()
        cursor = db.cursor()
        cursor.execute(
            "SELECT * FROM PRODUCTS"
        )
        rows = cursor.fetchall()
        cursor.close()
        db.close()
        return [Product.from_row(row) for row in rows]

    def get_product(prod_id):
        db = get_connection()
        cursor = db.cursor()
        cursor.execute(
            "SELECT * FORM PRODUCT WHERE ID = %s", (prod_id,)
        )
        row = cursor.fetchone()
        cursor.close()
        db.close()
        return Product.from_row(row) if row else None

    def add_product(name, desc, price, image):
        db = get_connection()
        cursor = db.cursor()
        cursor.execute(
            "INSERT INTO PRODUCTS (PRODUCT_ID, NAME, DESCRIPTION, PRICE, IMAGE_URL) VALUES (%s, %s, %s, %s)", (name, desc, price, image,)
        )
        db.commit()
        id = cursor.fetchone()
        cursor.close()
        db.close()
        return ProductFactory.get_product(id)

    def update_product(name, prod_id):
        db = get_connection()
        cursor = db.cursor()
        cursor.execute(
            "UPDATE PRODUCTS SET NAME = %s WHERE PRODUCT_ID = %s", (name, prod_id,)
        )
        db.commit()
        id = cursor.fetchone()
        cursor.close()
        db.close()
        return ProductFactory.get_product(id)
    
    def update_product_stock(stock, prod_id):
        db = get_connection()
        cursor = db.cursor()
        cursor.execute(
            "UPDATE PRODUCTS SET STOCK = %s WHERE PRODUCT_ID = %s", (stock, prod_id,)
        )
        db.commit()
        cursor.close()
        db.close()

    def remove_product(prod_id):
        db = get_connection()
        cursor = db.cursor()
        cursor.execute(
            "DELETE FROM PRODUCTS WHERE PRODUCT_ID = %s", (prod_id,)
        )
        db.commit()
        cursor.close()
        db.close()


#nbnfjvsu