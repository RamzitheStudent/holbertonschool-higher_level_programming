from flask import Flask, render_template, request
import json
import csv
import os

app = Flask(__name__)

# Helper functions to read JSON and CSV
def read_json(file_path):
    try:
        with open(file_path, 'r') as f:
            data = json.load(f)
        return data, None
    except Exception as e:
        return [], str(e)

def read_csv(file_path):
    try:
        data = []
        with open(file_path, newline='') as f:
            reader = csv.DictReader(f)
            for row in reader:
                # Convert id to int and price to float for consistency
                row['id'] = int(row['id'])
                row['price'] = float(row['price'])
                data.append(row)
        return data, None
    except Exception as e:
        return [], str(e)

@app.route('/products')
def products():
    source = request.args.get('source')
    id_param = request.args.get('id', type=int)

    # Determine file paths
    json_file = os.path.join(os.path.dirname(__file__), 'products.json')
    csv_file = os.path.join(os.path.dirname(__file__), 'products.csv')

    data = []
    error_message = None

    # Read data based on source
    if source == 'json':
        data, read_error = read_json(json_file)
        if read_error:
            error_message = f"Error reading JSON file: {read_error}"
    elif source == 'csv':
        data, read_error = read_csv(csv_file)
        if read_error:
            error_message = f"Error reading CSV file: {read_error}"
    else:
        error_message = "Wrong source"

    # Filter by id if provided
    if data and id_param is not None:
        filtered = [item for item in data if item['id'] == id_param]
        if not filtered:
            error_message = "Product not found"
        data = filtered

    return render_template('product_display.html', products=data, error=error_message)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
