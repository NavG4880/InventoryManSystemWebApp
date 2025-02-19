from flask import Flask, render_template, request, jsonify
import os
import psycopg2
import boto3
from psycopg2.extras import DictCursor  # ✅ Correct


app = Flask(__name__, static_folder="static", template_folder="templates")

# Function to fetch values from AWS SSM Parameter Store
def get_ssm_parameter(name, with_decryption=True):
    ssm_client = boto3.client("ssm", region_name="ap-southeast-2")  # Change region if needed
    try:
        response = ssm_client.get_parameter(Name=name, WithDecryption=with_decryption)
        return response["Parameter"]["Value"]
    except Exception as e:
        print(f"Error fetching parameter {name}: {e}")
        return None

# Fetch SSM parameters
DB_User = get_ssm_parameter("PartManagementDBUserName")
DB_Pass = get_ssm_parameter("PartManagementDBPass")

# Database connection function
def get_db_connection():
    try:
        conn =psycopg2.connect(
        dbname="awsprojectstack-awsprojectpartmanagdb-ogl3ryhncznf",
        user=DB_User,
        password=DB_Pass,
        host="awsprojectstack-awsprojectpartmanagdb-ogl3ryhncznf.chg844k20aok.ap-southeast-2.rds.amazonaws.com",   
        port="5432"
    )
        return conn
    except Exception as e:
        print(f"Database connection failed: {e}")
        return None


# Home Page
@app.route('/')
def index():
    conn = get_db_connection()
    cur = conn.cursor(cursor_factory=DictCursor)
    # Fetch all parts from DB (no search criteria)
    cur.execute("SELECT id, name, part_number, category, quantity FROM parts")
    parts = cur.fetchall()
    cur.close()
    conn.close()
    return render_template("index.html", parts=parts)
    #return render_template("index.html")

# Add Part Page
@app.route('/addpartpage', endpoint='add_part_page')
def add_part_page():
    return render_template("addpartpage.html")

# View Parts Page
@app.route('/viewpartspage')
def view_parts_page():
    return render_template("viewpartspage.html", parts=[])

# Reports Page
@app.route('/reportspage')
def reports_page():
    return render_template("reportspage.html")

# Settings Page
@app.route('/settings', methods=['GET', 'POST'])
def settings_page():
    return render_template('settingspage.html')

# API to Add Part (POST request from form)
@app.route('/api/add_part', methods=['POST'])
def api_add_part():
    name = request.form.get("name")
    part_number = request.form.get("part_number")
    category = request.form.get("category")
    quantity = request.form.get("quantity")

    if not (name and part_number and category and quantity):
        return jsonify({"error": "All fields are required"}), 400

    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("INSERT INTO parts (name, part_number, category, quantity) VALUES (%s, %s, %s, %s)", 
                (name, part_number, category, quantity))
    conn.commit()
    cur.close()
    conn.close()
    
    return jsonify({"message": "Part added successfully"}), 201

# API to search Parts (Used for displaying parts in View Parts Page)
@app.route('/api/search-parts', methods=['GET'])
def search_parts():
    """Fetch parts from DB. If 'query' param is provided, search for matching parts."""
    query = request.args.get('query', '').strip()  # Get search term from URL params

    conn = get_db_connection()
    if not conn:
        return jsonify({"error": "Database connection failed"}), 500
    
    try:
        cur = conn.cursor(cursor_factory=DictCursor)  # ✅ Use DictCursor correctly

        if query:
            # Search parts by name or part_number using ILIKE (case-insensitive)
            sql_query = "SELECT id, name, part_number, category, quantity FROM parts WHERE name ILIKE %s OR part_number ILIKE %s"
            cur.execute(sql_query, (f"%{query}%", f"%{query}%"))
        else:
            # No query → Fetch all parts
            sql_query = "SELECT id, name, part_number, category, quantity FROM parts"
            cur.execute(sql_query)

        parts = cur.fetchall()
        cur.close()
        conn.close()

        return jsonify([dict(part) for part in parts])  # ✅ Convert result to JSON

    except Exception as e:
        print(f"Error fetching parts: {e}")
        return jsonify({"error": "Failed to fetch parts"}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)
