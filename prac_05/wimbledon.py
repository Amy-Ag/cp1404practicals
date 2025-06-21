"""
Wimbledon
Estimated: 45 minutes
Actual: minutes
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
            champion_count[record[CHAMPION_INDEX]] += 1
        except KeyError:
            champion_count[record[CHAMPION_INDEX]] = 1
    return champion_count, countries

def display_result(champion_count, countries):
    """Print champions and countries."""
    print("Wimbledon Champions: ")
    for name, count in champion_count.items():
        print(name,count)
    print(f"\nThese {len(countries)} countries have won Wimbledon: ")
    print(" ".join(sorted(countries)))

def get_records(filename):
    """Read the file."""
    records = []
    with open(filename, "r", encoding="utf-8-sig") as in_file:
        in_file.readline()
        for line in in_file:
            records.append(line.strip().split(","))
        return records
main()