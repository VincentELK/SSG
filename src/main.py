from textnode import TextNode
from htmlnode import HTMLnode, LeafNode
import os
import shutil
from extract_title import extract_title
from generate_page import generate_page
from generate_pages_recursive import generate_page_recursive
import sys
basepath = ""
if len(sys.argv) > 1:
    basepath = sys.argv[1]
else:
    basepath = "/"
print(basepath)
def copy_recursive_content(source, dest):

    contents = os.listdir(source)
    if not os.path.exists(dest):
        os.mkdir(dest)
    for item in contents:
        full_path = os.path.join(source, item)
        dest_path = os.path.join(dest, item)

        if os.path.isfile(full_path):
            shutil.copy(full_path, dest_path)
        else:
            copy_recursive_content (full_path, dest_path)

def main():

    if os.path.exists("docs"):
        shutil.rmtree("docs")
    copy_recursive_content("static", "docs")
    generate_page("content/index.md", "template.html", "docs/index.html", basepath)
    generate_page_recursive("content", "template.html", "docs", basepath)
main()