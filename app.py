from flask import Flask, request, render_template, jsonify
import requests

app = Flask(__name__)

# Base URL for the currency exchange API
BASE_URL = "https://v6.exchangerate-api.com/v6/036e8036d2d44cf5f5164167/latest/"
@app.route('/', methods=['GET', 'POST'])
def home():
    result = None
    if request.method == 'POST':
        try:
            from_currency = request.form['from_currency'].upper()
            to_currency = request.form['to_currency'].upper()
            amount = float(request.form['amount'] or 0)

            response = requests.get(f"{BASE_URL}{from_currency}")
            print(f"API Response: {response.text}")  # Debug line
            data = response.json()
            
            if 'conversion_rates' in data and to_currency in data['conversion_rates']:
                rate = data['conversion_rates'][to_currency]
                result = round(amount * rate, 2)
            else:
                result = 'Error: Currency not found'
                
        except ValueError:
            result = "Error: Please enter a valid amount"
        except Exception as e:
            result = f"Error: {str(e)}"

    return render_template('home.html', result=result)
