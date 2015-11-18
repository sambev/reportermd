import argparse
import os
import json
import subprocess

import dateutil.parser
from jinja2 import Environment, PackageLoader

# set up the jinja environment
env = Environment(loader=PackageLoader('ardy', 'templates'),
                  trim_blocks=True,
                  lstrip_blocks=True)
snapshotmd = env.get_template('snapshot.md')


def parse_reporter_date(value):
    """Parse the date from a reporterApp report.  It can be one of two formats
    1. Stupid Apple date that is seconds from 01.01.2001
    2. ISO date YYYY-MM-DDTHH:MM:SS
    @param {mixed} value - float (case 1), string (case 2)

    @returns datetime
    """
    iphone_date = 978307200

    if type(value) == type(0.0):
        return datetime.fromtimestamp(iphone_date + value).replace(tzinfo=None)
    else:
        return dateutil.parser.parse(value).replace(tzinfo=None)


def find_by_date(snapshots, date_string):
    """
    Find all snapshots for the given date.
    @param {list} snapshots - dicts of snapshots
    @param {string} date_string - YYYY-MM-DD format string

    @returns {list}
    """
    user_date = parse_reporter_date(date_string)
    matching = []

    for snapshot in snapshots:
        snapshot_date = parse_reporter_date(snapshot['date'])
        if snapshot_date.date() == user_date.date():
            matching.append(snapshot)

    return matching


def main():
    '''
    Do the actual work of reading in the reporter export, writing it as md and
    importing it into dayone.
    '''
    parser = argparse.ArgumentParser(description='Import reporter app entries to dayone')
    parser.add_argument('date', type=str, help='Date to import reports from')
    parser.add_argument('--dayone',
                        type=bool,
                        help='Wether or not to import to dayone. (default: False)',
                        default=False)

    args = parser.parse_args()

    # First try to find the reporter-export.json file and read it in. If nothing
    # is found return early
    if not os.path.isfile('reporter-export.json'):
        print('[ERROR] No reporter-export file found. Looked in {0}'.format(
            os.path.dirname(os.path.abspath(__file__))
        ))
        return 1;

    print('Reading reporter-export.json...')

    # Now read in the data
    file_data = None
    with open('reporter-export.json') as f:
        file_data = f.read()

    # Load the data in as json and find the snapshot by date
    reporter_export = json.loads(file_data)
    snapshots = reporter_export['snapshots']
    date_string = args.date
    import_to_dayone = args.dayone
    dates = find_by_date(snapshots, date_string)
    markdown_file_name = 'entry-{0}.md'.format(date_string)

    # open up the markdown file for writing.
    with open(markdown_file_name, 'a') as f:
        print('Writing markdown file...')
        for snapshot in dates:
            location = snapshot.get('location', {}).get('placemark', {})
            weather = snapshot.get('weather', {})
            date = parse_reporter_date(snapshot['date'])

            f.write(snapshotmd.render(**{
                'date': date.date(),
                'time': date.time(),
                'locality': location.get('locality'),
                'postal_code': location.get('postalCode'),
                'state': location.get('administrativeArea'),
                'lat_long': location.get('region'),
                'tempF': weather.get('tempF'),
                'humidity': weather.get('relativeHumidity'),
                'windMPH': weather.get('windMPH'),
                'wind_direction': weather.get('windDirection'),
                'responses': snapshot.get('responses'),
            }))
        print('Markdown file {0} written!'.format(markdown_file_name))

    if import_to_dayone:
        print('Importing into DayOne...')
        subprocess.call(['sh',
                         'import_to_dayone.sh',
                         date_string,
                         markdown_file_name])

if __name__ == '__main__':
    main()
