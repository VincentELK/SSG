from markdown_to_blocks import markdown_to_blocks
from block_to_blocktype import block_to_block_type, BlockType
from htmlnode import HTMLnode
from htmlnode import ParentNode, LeafNode
def get_heading_level(block):
    lvl = 0
    for char in block:
        if char == "#":
            lvl += 1
        else:
            break
    return lvl

def markdown_to_html_node(markdown):
    markdown_block = markdown_to_blocks(markdown)
    children = []
    for block in markdown_block:
        block_type = block_to_block_type(block)
        
        if block_type == BlockType.HEADING:
            level = get_heading_level(block)
            node = LeafNode(f"h{level}", f"{block[level + 1:]}" )
            print(node.to_html())
        elif block_type == BlockType.PARAGRAPH:

            node = LeafNode("p", block)

        elif block_type == BlockType.CODE:
            node = ParentNode("pre", [LeafNode("code", block[4:-3])])
        elif block_type == BlockType.QUOTE:
            lines = block.split("\n")
            stripped_lines = []
            for line in lines:
                stripped_lines.append(line[2:])
            joined_text = " ".join(stripped_lines)
            node = LeafNode("blockquote", joined_text)
            print("joined text :", joined_text)
        elif block_type == BlockType.UNORDERED_LIST:
            lines = block.split("\n")
            lines_list = []
            for line in lines:

                leaf = LeafNode("li", line[2:])
                lines_list.append(leaf)
            node = ParentNode("ul",lines_list)
        elif block_type == BlockType.ORDERED_LIST:
            lines = block.split("\n")
            lines_list = []
            for line in lines:
                parts = line.split(". ", 1)
                leaf = LeafNode("li", parts[1])
                lines_list.append(leaf)
            node = ParentNode("ol", lines_list)
        children.append(node)
    parent = ParentNode("div", children)
    
    return parent

md = "1. item one\n2. item two\n3. item three"
node = markdown_to_html_node(md)
print(node.to_html())