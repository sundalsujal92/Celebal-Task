from flask import Flask, request, jsonify
import pyodbc

app = Flask(__name__)

# Replace these values with your actual DB configuration
server = '10.10.3.4'  # DB Tier IP
database = 'ThreeTierDB'
username = 'adminUser'
password = 'strongPass123'
driver= '{ODBC Driver 17 for SQL Server}'


@app.route('/log', methods=['POST'])
def log():
    data = request.get_json()
    message = data.get("message")

    try:
        conn = pyodbc.connect(
            f'DRIVER={driver};SERVER={server};DATABASE={database};UID={username};PWD={password}'
        )
        cursor = conn.cursor()
        cursor.execute("INSERT INTO logs (message) VALUES (?)", message)
        conn.commit()
        return jsonify({"status": "logged"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)