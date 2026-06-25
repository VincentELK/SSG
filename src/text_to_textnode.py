from textnode import TextNode, TextType, text_node_to_html_node
from split_nodes import split_nodes_delimiter, split_nodes_image, split_nodes_link

def text_to_textnodes(text):
    
    node = TextNode(text, TextType.TEXT)

    splitted_bold = split_nodes_delimiter([node], "**", 
    TextType.BOLD)
    
    splitted_italic = split_nodes_delimiter(splitted_bold, "_", TextType.ITALIC)
    
    splitted_code = split_nodes_delimiter(splitted_italic, "`", TextType.CODE)
    
    splitted_images = split_nodes_image(splitted_code)
    splitted_links = split_nodes_link(splitted_images)
    return splitted_links