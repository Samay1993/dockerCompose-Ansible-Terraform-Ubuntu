from flask import Flask, jsonify
import psycopg2

app = Flask(__name__)

# Define connection parameters for the PostgreSQL database
conn_params = {
    "host": "localhost",
    "port": 5432,
    "database": "mydatabase",
    "user": "postgres",
    "password": "password"
}

# Create a connection to the database
conn = psycopg2.connect(**conn_params)

# Define a route to insert data into the database
@app.route('/insert')
def insert_data():
    # Create a cursor object to execute SQL commands
    cur = conn.cursor()

    # Adding variables with SQL commands
    delete_table = '''DROP TABLE IF EXISTS mytable;'''
    create_table = '''CREATE TABLE mytable(name VARCHAR(255),age INT);'''
    insert_details = '''INSERT INTO mytable (name, age) VALUES ('Samay Singh Bisht', 30);'''

    # Dropping table if it already exists
    cur.execute(delete_table)
    # Create Table mytable in mydatabase
    cur.execute(create_table)
    # Insert a record into the database
    cur.execute(insert_details)

    # Commit the transaction
    conn.commit()
    # Close the cursor
    cur.close()
    # Return a success message
    return jsonify({"message": "Data inserted successfully"}), 200
  
# Define a route to fetch data from the database
@app.route('/fetch')
def fetch_data():
    # Create a cursor object to execute SQL commands
    cur = conn.cursor()

    # Creating variable with SQL commands
    select_data = '''SELECT * FROM mytable;'''

    # Fetch all records from the database
    cur.execute(select_data)
    rows = cur.fetchall()

    # Close the cursor
    cur.close()

    # Return the fetched data as a JSON response
    return jsonify({"data": rows}), 200

if __name__ == '__main__':
    app.run(debug=True)



# NOTE: Later add another endpoint /delete with different logics behind