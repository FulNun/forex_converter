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
            # Get and validate user input
            from_currency = request.form.get('from_currency', '').upper().strip()
            to_currency = request.form.get('to_currency', '').upper().strip()
            amount = request.form.get('amount', '').strip()

            # Validation for empty fields
            if not from_currency or not to_currency or not amount:
                result = "Error: Please fill out all fields."
                return render_template('home.html', result=result)

            # Convert amount to float
            try:
                amount = float(amount)
            except ValueError:
                result = "Error: Please enter a valid number for amount."
                return render_template('home.html', result=result)

            # Debug prints
            print(f"From: {from_currency}, To: {to_currency}, Amount: {amount}")

            # Construct the API URL and make the request
            url = f"{BASE_URL}{from_currency}/{to_currency}"
            print(f"URL: {url}")  # Debug URL
            response = requests.get(url)

            # Handle the response
            if response.status_code == 200:
                data = response.json()
                print(f"Response: {response.text}")  # Debug response

                if 'conversion_rate' in data:
                    result = round(amount * data['conversion_rate'], 2)
                else:
                    result = 'Error: Unable to retrieve the exchange rate.'
            else:
                result = 'Error: Failed to connect to the exchange rate API.'

        except Exception as e:
            print(f"Error: {str(e)}")  # Debug error
            result = f"Error: {str(e)}"

    return render_template('home.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)
