
This command line tool parses a CSV file of URLs and displays the HTTP status code and the time taken for the request.

## Features
- Parses a CSV file with a pipe (`|`) separator.
- Fetches the HTTP status code and request time for each URL.
- Outputs the results in a user-friendly format.
- Skips URLs that are not reachable within 2 seconds.

## Requirements
- Python 3.x
- `click` library
- `requests` library

## Installation

1. **Clone the repository or download the script:**
   ```sh
   git clone https://github.com/quadclutch/assignment.git
   ```

2. **Navigate to the directory:**
   ```sh
   cd <directory>
   ```

3. **Install the required Python packages:**
   ```sh
   pip install click requests
   ```

## Usage

1. **Prepare the CSV file:**

   The input file should be a CSV file with a pipe (`|`) separator. Each line should contain a name and a URL.

   Example `urls.csv`:
   ```csv
   Neti|http://www.neti.ee
   Google|http://www.google.com
   ```

2. **Run the script:**
   ```sh
   python assignment.py -i urls.csv
   ```

   Output:
   ```
   "Neti", HTTP 200, time 0.5 seconds
   "Google", HTTP 200, time 0.6 seconds
   ```

3. **Display the help message:**
   ```sh
   python assignment.py -h
   ```
