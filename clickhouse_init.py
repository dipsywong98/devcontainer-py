from clickhouse_driver import Client
from datetime import datetime

def create_clickhouse_table():
    # Initialize the ClickHouse client
    client = Client(
        host='clickhouse',
        port=9000,
        user='default',
        password='',
        database='default'
    )
    
    try:
        # Create a sample table
        create_table_query = """
            CREATE TABLE IF NOT EXISTS sample_table (
                id UInt32,
                name String,
                timestamp DateTime,
                value Float64
            )
            ENGINE = MergeTree()
            ORDER BY (id, timestamp)
        """
        
        client.execute(create_table_query)
        print("Table created successfully!")
        
        # Updated sample data using datetime objects
        sample_data = [
            (1, 'Item 1', datetime(2024, 3, 20, 10, 0, 0), 123.45),
            (2, 'Item 2', datetime(2024, 3, 20, 10, 1, 0), 567.89)
        ]
        
        client.execute(
            'INSERT INTO sample_table (id, name, timestamp, value) VALUES',
            sample_data
        )
        print("Sample data inserted successfully!")
        
    except Exception as e:
        print(f"An error occurred: {e}")
    
    finally:
        client.disconnect()

if __name__ == "__main__":
    create_clickhouse_table()
