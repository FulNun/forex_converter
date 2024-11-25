# Conceptual Questions

### 1. What is Flask and why do we use it?
Flask is a lightweight web framework for Python that allows developers to build web applications quickly and easily. It is designed with simplicity and flexibility in mind, providing the necessary tools and features to create web applications while avoiding unnecessary complexity. Flask is often used because it provides a minimalist structure, allowing developers to have greater control over their application's components and scaling as needed. Flask's extensibility allows for adding libraries and plugins, making it very versatile.

### 2. What is an API and why do we use it in this project?
An API (Application Programming Interface) is a set of rules and protocols that allows different software applications to communicate with each other. In this project, we use the currency exchange API to retrieve live exchange rates. This saves us the effort of manually updating exchange rates, allowing us to easily access up-to-date currency conversion information, ensuring our currency converter app provides accurate and reliable results.

### 3. What is the purpose of using `requests` library in the project?
The `requests` library in Python is used to send HTTP requests to interact with web APIs. In this project, it is used to make GET requests to the currency exchange API, allowing us to fetch real-time exchange rates. This makes our application dynamic by pulling the latest rates instead of relying on hardcoded or outdated data.

### 4. What is the difference between GET and POST requests?
- **GET Request**: A GET request is used to retrieve data from a server. It typically sends data through the URL, and it is used when no sensitive information is being transmitted.
- **POST Request**: A POST request is used to send data to a server to create or update resources. In our project, we use a POST request to submit the form data (the currencies and amount to be converted) to the server.

In our currency converter, GET is used to render the homepage and POST is used when users submit the conversion form.

### 5. How does the currency conversion process work in the application?
The currency conversion process works by:
1. Taking the user's input for the base currency, target currency, and amount.
2. Sending a request to the currency exchange API using the `requests` library.
3. Receiving the exchange rate data from the API response.
4. Calculating the converted amount by multiplying the provided amount by the exchange rate.
5. Displaying the result back to the user on the HTML page.

### 6. How do we handle errors when the exchange rate is unavailable?
In the application, error handling is done by checking if the response from the API contains the `rates` key and if the target currency is available in that response. If the requested exchange rate is not found, we return an error message indicating that the exchange rate is unavailable. This prevents the application from crashing and provides a user-friendly error message.

### 7. What are unit tests, and why are they important?
Unit tests are automated tests written to verify the behavior of small, individual units of code (e.g., functions or routes). In this project, unit tests are used to verify that the web application and currency conversion logic work as expected. They are important because they help catch bugs early in the development process, improve code quality, ensure reliability, and make future modifications safer by preventing regressions.

### 8. How does the `unittest` library help in testing our application?
The `unittest` library is a built-in Python testing framework that provides tools for writing and running tests. In this project, `unittest` helps us write tests to check if the Flask application routes are functioning correctly and if the currency conversion process works as expected. It provides useful features like assertions to validate outcomes and setup methods to initialize test conditions, making it easier to automate testing and ensure code reliability.
