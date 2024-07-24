import pandas as pd
from database import create_connection, execute_query

def load_data(filepath):
    return pd.read_csv(filepath)

def insert_data(connection, df):
    cursor = connection.cursor()
    for _, row in df.iterrows():
        query = """
        INSERT INTO laptops (id, brand, model, price)
        VALUES (%s, %s, %s, %s)
        """
        cursor.execute(query, (row['id'], row['brand'], row['model'], row['price']))
    connection.commit()
    print("Data inserted successfully")

def get_high_value_laptops(connection, price_threshold=1000):
    query = "SELECT * FROM laptops WHERE price > %s"
    cursor = connection.cursor(dictionary=True)
    cursor.execute(query, (price_threshold,))
    return cursor.fetchall()

def main():
    connection = create_connection()

    # Load data from CSV
    df = load_data('data/sample_data.csv')

    # Insert data into the database
    insert_data(connection, df)

    # Get high value laptops
    high_value_laptops = get_high_value_laptops(connection)
    for laptop in high_value_laptops:
        print(laptop)

if __name__ == "__main__":
    main()
