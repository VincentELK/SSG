from textnode import TextNode
from htmlnode import HTMLnode, LeafNode
def main():
    # text_node = TextNode("blabla", "bloblo", "https//igrapsnothing.com")
    # print(text_node)
    node = LeafNode("a", "Click test", {"href": "https://somebullcrap.com"})

    print(node.to_html())
main()