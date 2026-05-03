import unittest
from extract_links import extract_markdown_images, extract_markdown_links

class TestExtractLink(unittest.TestCase):
    
    def test_extract_markdown_images(self):
        matches = extract_markdown_images("This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)")
        expected = [("image", "https://i.imgur.com/zjjcJKZ.png")]

        self.assertListEqual(expected, matches)
    
    def test_extract_markdown_images_no_images(self):
        matches = extract_markdown_images("This is plain text with no images")
        self.assertListEqual([], matches)
    
    def test_extract_multiple_image(self):
        matches = extract_markdown_images("im a multiple image markdown link ![image1](https://link.image1.com/image1.png) ![image2](https://link.image2.com/image2.png)")

        expected = [("image1", "https://link.image1.com/image1.png"), ("image2", "https://link.image2.com/image2.png")]
        self.assertListEqual(expected, matches)