from clickhouse_driver import Client

def create_kafka_materialized_view():
    # Initialize Clickhouse client
    client = Client('clickhouse')
    
    # SQL statements
    create_kafka_table = """
        CREATE TABLE IF NOT EXISTS kafka_table
        (
            id UInt64,
            name String,
            timestamp DateTime
        )
        ENGINE = Kafka
        SETTINGS kafka_broker_list = 'kafka:9092',
                 kafka_topic_list = 'your_topic_name',
                 kafka_group_name = 'clickhouse_consumer_group',
                 kafka_format = 'JSONEachRow'
    """
    
    create_target_table = """
        CREATE TABLE IF NOT EXISTS target_table
        (
            id UInt64,
            name String,
            timestamp DateTime
        )
        ENGINE = MergeTree()
        ORDER BY (timestamp, id)
    """
    
    create_materialized_view = """
        CREATE MATERIALIZED VIEW IF NOT EXISTS kafka_mv
        TO target_table
        AS SELECT id,
                  name,
                  timestamp
        FROM kafka_table
    """
    
    try:
        # Execute the creation statements
        client.execute(create_kafka_table)
        client.execute(create_target_table)
        client.execute(create_materialized_view)
        print("Successfully created Kafka materialized view setup")
        
    except Exception as e:
        print(f"Error creating materialized view: {str(e)}")
        raise
    
if __name__ == "__main__":
    create_kafka_materialized_view()
