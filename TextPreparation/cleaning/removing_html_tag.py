import re

sample_text = """
<!DOCTYPE html>
<html lang="en">
  <body>
    <p>Hello there! This is line one.</p>
    <p>Here’s line two with a little more text.</p>
    <p>And line three to round it off.</p>
  </body>
</html>
"""

def strip_html(data):
    p = re.compile(r'<.*?>')
    text = p.sub('', data)              # remove HTML tags
    text = re.sub(r'\s+', ' ', text)    # collapse multiple spaces/newlines
    return text.strip()                 # remove leading/trailing spaces

clean_text = strip_html(sample_text)
print(clean_text)
print("########################################\n")




import re

def remove_html_tags(text):
    pattern = re.compile('<.*?>')
    return pattern.sub(r'', text)

text = '''
<p>NLP tokenizes, cleans, and embeds text so we can compare meanings across differently worded questions.</p> <p>Similar questions are clustered together to improve search, reduce duplicates, and boost engagement.</p>
'''

clean_text = remove_html_tags(text)

print(clean_text)