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
