from enum import Enum

class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING   = "heading"
    CODE      = "code"
    QUOTE     = "quote"
    UNORDERED_LIST = "unordered_list"
    ORDERED_LIST = "ordered_list"

def block_to_block_type(markdown_block):


    count = 0

    for char in markdown_block:
        if char != "#":
            break
        count += 1

    if 1 <= count <= 6 and markdown_block[count] == " ":
        return BlockType.HEADING
    
    if markdown_block[:4] == "```\n" and markdown_block[-4:] == "\n```":
        return BlockType.CODE
    
    lines = markdown_block.split("\n")
    for line in lines:
        if line[0] != ">":
            break
    else: 
        return BlockType.QUOTE
    
    lines_list = markdown_block.split("\n")
    for line in lines_list: 
        if line[:2] != "- ":
            break
    else:
        return BlockType.UNORDERED_LIST
    
    ordered_lines = markdown_block.split("\n")
    

    for i, line in enumerate(ordered_lines):
        if not line[0].isdigit():
            break
        if int(line[0]) != i + 1 or line[1:3] != ". ":
            break
    else:
        return BlockType.ORDERED_LIST

    return BlockType.PARAGRAPH

    
