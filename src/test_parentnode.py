import unittest
from htmlnode import ParentNode, LeafNode

class TestHTMLNode(unittest.TestCase):
    def test_to_html_with_child(self):
        child_node = LeafNode("p", "child")
        parent_node = ParentNode("div", [child_node])