import unittest
from textnode import TextNode, TextType
from split_nodes import split_nodes_delimiter

class TestSplitNodes(unittest.TestCase):
    def test_multiple_delimiter(self):
        node = TextNode("i'm a `multiple` délimiter `test`", TextType.TEXT)
        result = split_nodes_delimiter([node], "`", TextType.CODE)
        
        expected = [
            TextNode("i'm a ", TextType.TEXT),
            TextNode("multiple", TextType.CODE),
            TextNode(" délimiter ", TextType.TEXT),
            TextNode("test", TextType.CODE),
        ]
        self.assertEqual(result, expected)
    
    def test_unclosed_delimiter(self):
        node = TextNode("i'm **unclosed delimiter string", TextType.TEXT)
        with self.assertRaises(Exception):
            split_nodes_delimiter([node],"**", TextType.TEXT)
    