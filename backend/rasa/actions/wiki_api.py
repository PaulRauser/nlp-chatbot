import wikipediaapi

wiki = wikipediaapi.Wikipedia('en')

def fetch_wikipedia_summary(title) -> str:
    page = wiki.page(title)

    if page.exists():
        return page.summary
    else:
        return f"I can't find any more details for '{title}'"


