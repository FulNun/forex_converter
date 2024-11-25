from flask import Flask, request, render_template, jsonify
import requests

app = Flask(__name__)

# Base URL for the currency exchange API
BASE_URL = "https://api.exchangerate.host/latest"

@app.route('/', methods=['GET', 'POST'])
def home():
    result = None
    if request.method == 'POST':
        try:
            from_currency = request.form['from_currency'].upper()
            to_currency = request.form['to_currency'].upper()
            amount = float(request.form['amount'])

            response = requests.get(BASE_URL, params={'base': from_currency, 'symbols': to_currency})
            print(f"API Response: {response.text}")  # Add this line
            data = response.json()

            if 'rates' in data and to_currency in data['rates']:
                rate = data['rates'][to_currency]
                result = amount * rate
            else:
                result = 'Error: Unable to retrieve the exchange rate.'
        except Exception as e:
            print(f"Error: {str(e)}")  # Add this line
            result = f"Error: {str(e)}"

    return render_template('home.html', result=result)
