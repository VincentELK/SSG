from textnode import TextNode, TextType
from extract_links import extract_markdown_images, extract_markdown_links

def split_nodes_delimiter(old_nodes: list, delimiter, text_type)-> list: 
    new_nodes = []
    for node in old_nodes:
        
        if not node.text_type == TextType.TEXT:
            new_nodes.append(node)
            continue
        delimiter_count = node.text.count(delimiter)

        if delimiter_count % 2 != 0:
            raise Exception(f"""No closing delimiter < {delimiter}> found""" )
        
        splitted_node = node.text.split(delimiter)

        for i in range(len(splitted_node)):
            if splitted_node[i] == "": 
                continue
            elif i % 2 == 0:
                text_string = splitted_node[i]
                new_nodes.append(TextNode(text_string, TextType.TEXT))
            
            else:
                formated_string = splitted_node[i]
                new_nodes.append(TextNode(formated_string, text_type))
            
    
    return new_nodes

def split_nodes_image(old_nodes):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
        else:
            remaining_text = node.text
            images  = extract_markdown_images(remaining_text)
            if not images: 
                new_nodes.append(node)
            
            else:

                for image_alt, image_url in images:
                    sections = remaining_text.split(f"![{image_alt}]({image_url})", 1)
                    before = sections[0]
                    after = sections[1]

                    if before:
                        new_nodes.append(TextNode(before, TextType.TEXT))

                    new_nodes.append(TextNode(image_alt, TextType.IMAGE, image_url))

                    remaining_text = after

                if remaining_text:
                    new_nodes.append(TextNode(remaining_text, TextType.TEXT))
    return new_nodes
    

def split_nodes_link(old_nodes):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue
        
        remaining_text = node.text
        links = extract_markdown_links(remaining_text)
        if not links:
                new_nodes.append(node)
                continue
        for alt, link in links:
            

            sections = remaining_text.split(f"[{alt}]({link})", 1)
            before = sections[0]
            after = sections[1]

            if before:
                new_nodes.append(TextNode(before, TextType.TEXT))
            new_nodes.append(TextNode(alt, TextType.LINK, link))
            remaining_text = after
        if remaining_text:
            new_nodes.append(TextNode(remaining_text, TextType.TEXT))

    return new_nodes     



