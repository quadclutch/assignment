import csv
import requests
import click
import time

@click.command(context_settings=dict(help_option_names=['-h', '--help']))
@click.option('-i', '--input-file', type=click.Path(exists=True), required=True, help="Input file containing URLs")
def main(input_file):
    """Parses a CSV file of URLs and prints the HTTP status and request time."""
    with open(input_file, 'r') as file:
        reader = csv.reader(file, delimiter='|')
        for row in reader:
            name, url = row
            try:
                start_time = time.time()
                response = requests.get(url, timeout=2)
                end_time = time.time()
                elapsed_time = end_time - start_time
                click.echo(f'"{name}", HTTP {response.status_code}, time {elapsed_time:.1f} seconds')
            except requests.exceptions.RequestException:
                click.echo(f'Skipping {url}')

if __name__ == '__main__':
    main()
