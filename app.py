from flask import Flask, request
from datetime import datetime
import csv

app = Flask(__name__)

@app.route('/')
def track():

    # Get IP Address
    ip_address = request.remote_addr

    # Get current time
    timestamp = datetime.now()

    # Get browser / device info
    user_agent = request.headers.get('User-Agent')

    # Save data into logs.csv (auto created if not exists)
    with open('logs.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([timestamp, ip_address, user_agent])

    return "QR Scan Recorded Successfully"

if __name__ == '__main__':
    print("Server starting...")
    app.run(debug=True)