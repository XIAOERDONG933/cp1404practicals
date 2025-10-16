"""
Wimbledon
Estimate: 60 minutes
Actual:   112 minutes
"""
FILENAME = "wimbledon.csv"

def main():
    champions, countries = read_wimbledon_data(FILENAME)
    champion_wins = count_champions(champions)
    display_results(champion_wins, countries)

def read_wimbledon_data(filename):
    """Read and extract champion data from the Wimbledon CSV file."""
    champions = []
    countries = set()

    with open(filename, "r", encoding="utf-8-sig") as in_file:
        in_file.readline()
        for line in in_file:
            parts = line.strip().split(",")
            country = parts[1]
            champion = parts[2]

            champions.append(champion)
            countries.add(country)

    return champions, countries


def count_champions(champions):
    """Count the number of times each player has won Wimbledon."""
    champion_wins = {}
    for champion in champions:
        champion_wins[champion] = champion_wins.get(champion, 0) + 1
    return champion_wins


def display_results(champion_wins, countries):
    """Display the results in the required format."""
    print("Wimbledon Champions:")
    for champion, wins in sorted(champion_wins.items()):
        print(f"{champion} {wins}")

    print("\nThese", len(countries), "countries have won Wimbledon:")
    print(", ".join(sorted(countries)))




main()