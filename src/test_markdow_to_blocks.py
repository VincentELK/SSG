import unittest
from markdown_to_blocks import markdown_to_blocks
from block_to_blocktype import block_to_block_type, BlockType

class TestMarkdownToBlocks(unittest.TestCase):
    def test_markdown_to_blocks(self):
        md = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
        blocks = markdown_to_blocks(md)

        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",  
            ],)
    
    def test_block_type_code(self):
        block = "```\nsome code\n```"
        self.assertEqual(block_to_block_type(block), BlockType.CODE)
    
    def test_block_type_heading(self):
        block = "### im heading"

        self.assertEqual(block_to_block_type(block), BlockType.HEADING)
    
    def test_block_type_unordered(self):
        block = "- im unordered one\n- im unordered two"

        self.assertEqual(block_to_block_type(block), BlockType.UNORDERED_LIST)