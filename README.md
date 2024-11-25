# Forex Converter

## Project Overview
A Flask-based web application that allows users to convert currencies using real-time exchange rates from an external API.

## Features
- Real-time currency conversion
- Support for multiple currencies
- Simple and intuitive user interface
- Error handling for unavailable exchange rates

## Technologies Used
- Python
- Flask
- Requests library
- Unittest for testing
- HTML/Jinja2 templating

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
pip install flask requests
```

### 4. Run the Application
```bash
python app.py
```
Navigate to `http://localhost:5000` in your web browser.

## Running Tests
```bash
python -m unittest forex_converter_tests.py
```

## API Used
The application uses the [Exchange Rates API](https://exchangerate.host/) for real-time currency conversion rates.

## Deployment
### Heroku Deployment
1. Create a `Procfile`:
```
web: gunicorn app:app
```

2. Create `requirements.txt`:
```bash
pip freeze > requirements.txt
```

3. Install Heroku CLI and deploy:
```bash
heroku create forex-converter-app
git push heroku main
```

## Conceptual Overview
The application demonstrates key web development concepts including:
- RESTful API integration
- Form handling
- Error management
- Unit testing

## Limitations and Potential Improvements
- Add more comprehensive error handling
- Implement caching for exchange rates
- Create a more robust frontend
- Add support for historical exchange rates

## License
MIT License

## Contact
Jerrad Gebhard
GitHub: @fulnuns
