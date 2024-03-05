# Project Explanation

This project involves fetching data from a SQLite database and dynamically updating an HTML table using Flask and AJAX.

## Part 1: Fetching Data from Database

### Overview
This part of the project focuses on fetching data from a SQLite database named `data.db`.

### Code Explanation
1. **SQLite Database Setup**: The `get_data_from_db()` function establishes a connection to the SQLite database file `data.db` and retrieves data from the `items` table.

2. **Data Retrieval**: The function executes a SELECT query to retrieve all rows from the `items` table. It then returns the fetched data.

3. **Flask Routes**: The Flask app defines two routes:
   - `/`: This route renders the `index.html` template.
   - `/get_data`: This route returns JSON containing the fetched data from the database.

## Part 2: Real-time Data Update in HTML Table

### Overview
In this part, the HTML file `index.html` displays the fetched data in a table and updates it dynamically using JavaScript and AJAX.

### Code Explanation
1. **HTML Table**: The HTML file defines a table with a `<thead>` section for column headers and a `<tbody>` section to be populated dynamically with data.

2. **JavaScript**: The JavaScript code fetches data from the Flask server every second using AJAX and updates the table accordingly.
   - The `updateTable()` function populates the table body with the fetched data.
   - The `fetchData()` function sends a GET request to the Flask server's `/get_data` endpoint and updates the table with the received data.
   - Initial data fetching and subsequent updates occur every second using `setInterval()`.

## Conclusion
This project demonstrates how to fetch data from a SQLite database using Flask and dynamically update an HTML table with real-time data using AJAX. By combining server-side and client-side technologies, it provides a responsive and interactive user experience for displaying data.
