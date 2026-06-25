import unittest
from textnode import TextNode, TextType
from split_nodes import split_nodes_delimiter, split_nodes_image, split_nodes_link

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
    
    def test_split_image_link_node(self):
        node = TextNode("my test ![alt](https://test.com)after", TextType.TEXT )
        nodes_list = [node]
        
        result = split_nodes_image(nodes_list)

        expected = [
            TextNode("my test ", TextType.TEXT),
            TextNode("alt", TextType.IMAGE, "https://test.com"),
            TextNode("after", TextType.TEXT),
        ]
        self.assertEqual(result, expected)

    def test_split_url_links_node(self):
        node = TextNode("my link [alt](mylink.com) after", TextType.TEXT)

        node_list = [node]
        result = split_nodes_link(node_list)

        expected = [
            TextNode("my link ", TextType.TEXT),
            TextNode("alt", TextType.LINK, "mylink.com"),
            TextNode(" after", TextType.TEXT),
        ]
        self.assertEqual(result, expected)

    def test_url_link_at_start(self):
        node = TextNode("[the link](thelink.com) after link", TextType.TEXT)

        node_list = [node]
        result = split_nodes_link(node_list)

        expected = [
            TextNode("the link", TextType.LINK, "thelink.com"),
            TextNode(" after link", TextType.TEXT)
        ]
        self.assertEqual(result, expected)
    
    def test_multi_link_node(self):
        node = TextNode("[first](firstlink.com) [second](secondlink.com)", TextType.TEXT)
        node_list = [node]

        result = split_nodes_link(node_list)

        expected = [
            TextNode("first", TextType.LINK, "firstlink.com"),
            TextNode(" ", TextType.TEXT),
            TextNode("second", TextType.LINK, "secondlink.com")

        ]
        self.assertEqual(result, expected)