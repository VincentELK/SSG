from markdown_to_html import markdown_to_html_node
from extract_title import extract_title
import os
def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    

    with open(from_path, "r") as f:
        source_content = f.read()
    
    with open(template_path, "r") as f:

        template_content = f.read()

    html_string= markdown_to_html_node(source_content).to_html()

    title = extract_title(source_content)

    final_html = template_content.replace("{{ Title }}", title)
    
    final_html = final_html.replace("{{ Content }}", html_string)


    dest_dir = os.path.dirname(dest_path)
    os.makedirs(dest_dir, exist_ok=True)

    with open(dest_path, "w") as f:
        f.write(final_html)
