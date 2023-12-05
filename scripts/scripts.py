#################
# HERE YOU CAN PUT OTHER SCRIPTS USED IN PAGES. THE IDEA IS TO NOT PUT SCRIPTS/FUNCTIONS ON THE PAGES BECAUSE IS THE VIEW.
#################

"""
This function reads a Markdown file and returns its content as a string.
"""
def read_markdown_file(markdown_file):
    try:
        with open(markdown_file, "r", encoding="utf-8") as file:
            content = file.read()
        return content
    except FileNotFoundError:
        return "Markdown file not found."