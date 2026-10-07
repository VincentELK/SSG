
def extract_title(markdown):
    lines = markdown.split("\n")

    for line in lines:
        if line.startswith("# "):
            line_stripped = line.strip()
            clean_word = line_stripped[2:]
            
            return clean_word
    raise Exception("no H1 found")