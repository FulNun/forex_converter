# Forex Converter

## Project Overview
A Flask-based web application that allows users to convert currencies using real-time exchange rates from an external API. Users can select different currency pairs and get up-to-date conversion rates instantly.

## Features
- **Real-time currency conversion** using an external API.
- **Support for multiple currencies**, allowing conversions between popular and lesser-known currencies.
- **Simple and intuitive user interface** for ease of use.
- **Error handling** for unavailable exchange rates or invalid input.
- **Unit tests** to verify the core functionalities.

## Technologies Used
- **Python** for backend logic.
- **Flask** as the web framework.
- **Requests library** for making API calls.
- **Unittest** for testing functionality.
- **HTML/Jinja2** for templating.

## Prerequisites
- Python 3.7+
- pip (Python package manager)

## Setup and Installation

### 1. Clone the Repository
```bash
git clone https://github.com/Jerrad-Johnson/Forex-Converter
cd forex-converter
```

### 2. Create a Virtual Environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```
Note: Make sure your `requirements.txt` file is up-to-date. You can generate one with:
```bash
pip freeze > requirements.txt
```

### 4. Run the Application
```bash
python app.py
```
Navigate to `http://localhost:5000` in your web browser to access the app.

## Running Tests
To run the unit tests included in the project, use:
```bash
python -m unittest forex_converter_tests.py
```
This will execute the automated tests to verify the core functionalities of the app, such as page responses and currency conversion logic.

## API Used
The application uses the [Exchange Rates API](https://exchangerate.host/) for real-time currency conversion rates.

## Deployment
### Heroku Deployment

1. **Create a `Procfile`**:
   ```
   web: gunicorn app:app
   ```

2. **Create `requirements.txt`** if not done already:
   ```bash
   pip freeze > requirements.txt
   ```

3. **Deploy to Heroku**:
   - Install the Heroku CLI if you haven't already.
   - Log in to Heroku and create a new app:
     ```bash
     heroku create forex-converter-app
     ```
   - Push the repository to Heroku:
     ```bash
     git push heroku main
     ```
   
4. **Set Environment Variables** (if needed): If your API key or other settings need to be configured, use:
   ```bash
   heroku config:set VARIABLE_NAME=value
   ```

## Conceptual Overview
The Forex Converter demonstrates essential web development concepts such as:
- **RESTful API Integration**: The app integrates with the Exchange Rates API to get real-time exchange rates.
- **Form Handling and User Input**: Accepts user inputs through forms and processes them.
- **Error Management**: Handles cases where the API fails or inputs are invalid.
- **Unit Testing**: Implements unit tests to verify functionality, ensuring that critical components work as intended.

## Limitations and Potential Improvements
- **Error Handling**: Expand error handling to include API rate limiting and network issues.
- **Caching**: Implement caching to reduce the number of API calls and improve performance.
- **Frontend Improvements**: Improve the UI for a more user-friendly experience, possibly using a frontend framework like React.
- **Historical Exchange Rates**: Add a feature to view historical rates for selected currency pairs.

## License
MIT License

## Contact
Jerrad Gebhard
- GitHub: [@fulnuns](https://github.com/fulnuns)
