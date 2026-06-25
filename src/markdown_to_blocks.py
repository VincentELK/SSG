from enum import Enum

def markdown_to_blocks(markdown):
    markdown_blocks = markdown.split("\n\n")

    striped_blocks = []
    for block in markdown_blocks:
        
        stripped = block.strip()
        if stripped != "":    
            striped_blocks.append(stripped)
        
    return striped_blocks

