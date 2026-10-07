import os
from generate_page import generate_page

def generate_page_recursive(dir_path_content, template_path, dest_dir_path):
    entries_list = os.listdir(dir_path_content)
    
    for entry in entries_list:
        complete_path = os.path.join(dir_path_content, entry)
        print(complete_path)

        if os.path.isfile(complete_path):
            if complete_path[-3:] == ".md":
                generate_page(complete_path, template_path, os.path.join(dest_dir_path, "index.html") )
                output_path = os.path.join(dest_dir_path, "index.html")

        else:
            destination_path = os.path.join(dest_dir_path, entry)
            os.makedirs(destination_path, exist_ok=True)
            if os.path.exists(destination_path):
                generate_page_recursive(complete_path, template_path, destination_path)

