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

