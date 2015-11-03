import json
import sys
import subprocess

import dateutil.parser
from jinja2 import Environment, PackageLoader

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

if __name__ == '__main__':
    file_data = None

    with open('reporter-export.json') as f:
        file_data = f.read()

    if not file_data:
        print('No data read')
    else:
        reporter_export = json.loads(file_data)
        snapshots = reporter_export['snapshots']
        date_string = sys.argv[1]
        dates = find_by_date(snapshots, date_string)

        with open('entry.md', 'a') as f:
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

        subprocess.call(['sh', 'import.sh', date_string])
