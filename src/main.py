from textnode import TextNode
from htmlnode import HTMLnode, LeafNode
import os
import shutil
from extract_title import extract_title
from generate_page import generate_page
from generate_pages_recursive import generate_page_recursive

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

    if os.path.exists("public"):
        shutil.rmtree("public")
    copy_recursive_content("static", "public")
    generate_page("content/index.md", "template.html", "public/index.html")
    generate_page_recursive("content", "template.html", "public")
main()