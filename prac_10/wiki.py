import wikipedia
from wikipedia.exceptions import DisambiguationError, PageError


def main():
    title = input("Enter page title: ").strip()
    while title != "":
        try:
            page = wikipedia.page(title)
            print(page.title)
            print(wikipedia.summary(page.title))
            print(page.url)
        except DisambiguationError:
            print("We need a more specific title. Try one of the following, or a new search:")
            suggestions =  wikipedia.search(title)
            print(suggestions)
        except PageError:
            print(f"Page id \"{title}\" does not match any pages. Try another id!")
        print()
        title = input("Enter page title: ").strip()
    print("Thank you.")


main()