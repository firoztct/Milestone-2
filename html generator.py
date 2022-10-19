paragraph1 = "This is Paragraph One"
paragraph2 = "This is Paragraph Two"
paragraph3 = "This is Paragraph Three"
paragraph4 = "This is Paragraph Four"

# paragraph1_html = f"<p>{paragraph1}</p>"
# paragraph2_html = f"<p>{paragraph2}</p>"
# paragraph3_html = f"<p>{paragraph3}</p>"
# paragraph4_html = f"<p>{paragraph4}</p>"

def paragraph_html(paragraph):
    all_paragraph_html = f"<p>{paragraph}</p>"
    return all_paragraph_html
print(paragraph_html(paragraph1))
print(paragraph_html(paragraph2))
print(paragraph_html(paragraph3))
print(paragraph_html(paragraph4))


