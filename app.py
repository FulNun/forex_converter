from flask import Flask, request, render_template, jsonify
import requests

app = Flask(__name__)

# Base URL for the currency exchange API
BASE_URL = "https://v6.exchangerate-api.com/v6/036e8036d2d44cf5f5164167/pair/"

@app.route('/', methods=['GET', 'POST'])
def home():
    result = None
    if request.method == 'POST':
        try:
            from_currency = request.form['from_currency'].upper()
            to_currency = request.form['to_currency'].upper()
            amount = float(request.form['amount'])
            
            url = f"{BASE_URL}{from_currency}/{to_currency}"
            print(f"URL: {url}")  # Debug URL
            response = requests.get(url)
            print(f"Response: {response.text}")  # Debug response
            data = response.json()
            
            if 'conversion_rate' in data:
                result = round(amount * data['conversion_rate'], 2)
            else:
                result = 'Error: Unable to retrieve the exchange rate.'
                
        except Exception as e:
            print(f"Error: {str(e)}")  # Debug error
            result = f"Error: {str(e)}"

    return render_template('home.html', result=result)
