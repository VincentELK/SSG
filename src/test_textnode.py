import unittest
from textnode import TextNode, TextType

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD_TEXT)
        node2 = TextNode("This is a text node", TextType.BOLD_TEXT)
        self.assertEqual(node, node2)

    def test_no_eq(self):
        node = TextNode("This is a text node", TextType.BOLD_TEXT )
        node2 = TextNode("This is another different text", TextType.PLAIN_TEXT)
        self.assertNotEqual(node, node2)

    def test_url(self):
        node = TextNode("None URL", TextType.LINK)

        self.assertIsNone(node.url, "URL is None")
    
    def test_text_type_not_equal(self):
        node = TextNode("Some Text", TextType.CODE_TEXT)
        node2 = TextNode("Some Text", TextType.PLAIN_TEXT)
        self.assertNotEqual(node, node2)

    
if __name__ == "__main__":
    unittest.main()