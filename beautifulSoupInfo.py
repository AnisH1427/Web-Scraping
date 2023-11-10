import bs4

def display_info():
    print("Beautiful Soup is a Python library for web scraping.")
    print("It allows you to parse HTML and XML documents.")
    print("You can install Beautiful Soup using pip: pip install beautifulsoup4")
    print("To use Beautiful Soup, you first need to import the library: import bs4")
    print()
    print("Some of the key functions in Beautiful Soup are:")
    print("- BeautifulSoup: creates a BeautifulSoup object from an HTML/XML document")
    print("- find: finds the first tag with the specified name and attributes")
    print("- find_all: finds all tags with the specified name and attributes")
    print("- select: finds tags that match a CSS selector")
    print("- get_text: extracts the text content of a tag")
    print("- attrs: returns a dictionary of the tag's attributes")
    print("- contents: returns a list of the tag's children")
    print("- parent: returns the parent of the tag")
    print("- previous_sibling: returns the previous sibling of the tag")
    print("- next_sibling: returns the next sibling of the tag")
    print()
    print("Let's take a closer look at each of these functions:")
    print()
    print("1. BeautifulSoup")
    print("The BeautifulSoup function is used to create a BeautifulSoup object from an HTML/XML document. This object represents the document as a nested data structure. You can then navigate and search this structure using the other functions in Beautiful Soup.")
    print()
    print("2. find")
    print("The find function is used to find the first tag in the document with the specified name and attributes. The function takes two arguments: the name of the tag and a dictionary of attributes to search for. If the tag is not found, the function returns None.")
    print()
    print("3. find_all")
    print("The find_all function is used to find all tags in the document with the specified name and attributes. The function takes the same arguments as the find function. If no tags are found, the function returns an empty list.")
    print()
    print("4. select")
    print("The select function is used to find tags in the document that match a CSS selector. The function takes a single argument: the CSS selector to search for. The function returns a list of tags that match the selector.")
    print()
    print("5. get_text")
    print("The get_text function is used to extract the text content of a tag. The function takes no arguments and returns a string.")
    print()
    print("6. attrs")
    print("The attrs function is used to return a dictionary of the tag's attributes. The function takes no arguments.")
    print()
    print("7. contents")
    print("The contents function is used to return a list of the tag's children. The function takes no arguments.")
    print()
    print("8. parent")
    print("The parent function is used to return the parent of the tag. If the tag has no parent, the function returns None.")
    print()
    print("9. previous_sibling")
    print("The previous_sibling function is used to return the previous sibling of the tag. If the tag has no previous sibling, the function returns None.")
    print()
    print("10. next_sibling")
    print("The next_sibling function is used to return the next sibling of the tag. If the tag has no next sibling, the function returns None.")
    
if __name__ == "__main__":
    display_info()
