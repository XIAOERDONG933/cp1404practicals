"""
Wimbledon
Estimate: 20 minutes
Actual:   32 minutes
"""

FILENAME = "wimbledon.csv"
INDEX_CHAMPION = 2
INDEX_CHAMPION_COUNTRY = 1

def main():
    data = load_data()
    champion_to_count, countries = process_data(data)
    display_information(champion_to_count, countries)

def load_data():
    """Load data from the file"""
    data = []
    with open(FILENAME, "r", encoding="utf-8-sig") as in_file:
        lines = in_file.readlines()[1:]
        for line in lines:
            record = line.strip().split(",")
            data.append(record)
        return data


def process_data(data):
    """Process the data"""
    champion_to_count = {}
    countries = set()
    for record in data:
        champion = record[INDEX_CHAMPION]
        # if champion not in champions_to_count:
        #     champions_to_count[champion] = 1
        # else:
        #     champions_to_count[champion] += 1
        champion_to_count[champion] = champion_to_count.get(champion, 0) + 1
        countries.add(record[INDEX_CHAMPION_COUNTRY])
    return champion_to_count, countries


def display_information(champion_to_count, countries):
    """Display the information"""
    print("Wimbledon Champions: ")
    for champion, count in champion_to_count.items():
        print(f"{champion} {count}")
    print()
    print(f"These {len(countries)} countries have won Wimbledon: ")
    print(", ".join(sorted(countries)))



main()