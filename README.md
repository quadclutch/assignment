# URL Status Checker

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
