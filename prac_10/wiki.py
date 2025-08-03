import wikipedia

def main():
    """Find wikipedia page for certain word."""
    title= input("Enter page title or search phrase: ").strip()
    while title != "":
        try:
            page = wikipedia.page(title, auto_suggest=False)
            print(page.title)
            print(page.content)
            print(page.url)
        except wikipedia.exceptions.DisambiguationError as e:
            print("DisambiguationError: ", e.options[:5])
        except wikipedia.exceptions.PageError:
            print("Page not found.")
        title = input("\nEnter page title or search phrase: ").strip()
    print("Thank you.")

main()