import unittest
from text_to_textnode import text_to_textnodes
from textnode import TextNode, TextType

class TestInLineMarkdown(unittest.TestCase):
    def test_splitting_text(self):
        node = """ This is **text** with an _italic_ word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)""" 

        result = text_to_textnodes(node)

        expected = [
    TextNode(" This is ", TextType.TEXT),
    TextNode("text", TextType.BOLD),
    TextNode(" with an ", TextType.TEXT),
    TextNode("italic", TextType.ITALIC),
    TextNode(" word and a ", TextType.TEXT),
    TextNode("code block", TextType.CODE),
    TextNode(" and an ", TextType.TEXT),
    TextNode("obi wan image", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"),
    TextNode(" and a ", TextType.TEXT),
    TextNode("link", TextType.LINK, "https://boot.dev"),
    ]
        self.assertEqual(result, expected)
    
    def text_plain_text_node(self):
        node = "Just a plain text"
        result = text_to_textnodes(node)

        expected = [TextNode("just a plain text", TextType.TEXT)]

        self.assertEqual(result, expected)