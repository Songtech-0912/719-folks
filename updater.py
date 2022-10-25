import sys
from lxml import html
from lxml.etree import tostring

def read(path):
    with open(path, "r") as f:
        return f.read()

def writeb(path, contents):
    with open(path, "wb") as f:
        f.write(contents)

def main():
    if len(sys.argv) < 2:
        print("Invalid arguments. Usage: python updated.py <latest discord code>")
        exit(1)
    s = read("index.html")
    html_contents = html.fromstring(s)
    url_element = html_contents.get_element_by_id("url")
    url_element.text = sys.argv[1]
    output_html = tostring(html_contents, pretty_print=True)
    writeb("index.html", output_html)
    print(f"Updated with newest discord code {sys.argv[1]}")

if __name__ == "__main__":
    main()
