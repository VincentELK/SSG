import unittest
from htmlnode import HTMLnode
from textnode import TextNode, TextType, text_node_to_html_node

class TestHTMLNode(unittest.TestCase):
     
     def test_tag(self):
          
          node = HTMLnode("p")
          self.assertEqual(node.tag, "p")

    
     def test_node_value(self):
          node = HTMLnode("p", "value")
          
          self.assertEqual(node.value, "value")
          self.assertEqual(node.tag, "p")
          self.assertEqual(node.children, None)
          self.assertEqual(node.props, None)
     
     def test_repr(self):
          node = HTMLnode("p", "some text", None, {"class":"some_text"})

          self.assertEqual(node.__repr__(), "HTMLNode(p, some text, children: None, {'class': 'some_text'})")

    
     def test_props(self):
        node = HTMLnode("div", "Test link", None, {"class": "Test link", "href": "https//somelink.com"} )
        self.assertEqual(node.props_to_html(), ' class="Test link" href="https//somelink.com"') # testing the props_to_html to return the correct format

     def test_text(self):
          node = TextNode("This is a text node", TextType.TEXT)
          html_node = text_node_to_html_node(node)
          self.assertEqual(html_node.tag, None)
          self.assertEqual(html_node.value, "This is a text node")
     
     

