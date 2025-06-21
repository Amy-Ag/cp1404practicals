"""
Wimbledon
Estimated: 45 minutes
Actual:
"""
FILENAME= "wimbledon.csv"
COUNTRY_INDEX=1
CHAMPION_INDEX=2

def main():
    """Display clean data for Wimbledon champions."""
    records= get_records(FILENAME)
    champion_count, countries= clean_record(records)
    display_result(champion_count, countries)

def clean_record(records):
    """Create dictionary to store champions and countries."""
    champion_count = {}
    countries = set()
    for record in records:
        countries.add(record[COUNTRY_INDEX])
        try:
            champion_count[record[COUNTRY_INDEX]] += 1
        except KeyError:
            champion_count[record[COUNTRY_INDEX]] = 1
    return champion_count, countries
