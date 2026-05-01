from textnode import TextNode, TextType

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

