import wikipedia

def main():
    title= input("Enter page title or search phrase: ").strip()
    while title != "":
        try:
            page = wikipedia.page(title, auto_suggest=False)
            print("Title:", page.title)
            print("URL: ", page.url)
            print("Summary: ", page.content)
        except wikipedia.exceptions.DisambiguationError as e:
            print("DisambiguationError: ", e.options[:5])
        except wikipedia.exceptions.PageError:
            print("Page not found.")
        title = input("\nEnter page title or search phrase: ").strip()


main()