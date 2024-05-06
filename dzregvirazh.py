import re

def extract_image_links(html_text):
    call = []
    regular = r'(http|https)(://)([0-9a-zA-z.]+)(/)([a-z0-9]+)\.(jpg|png|gif)'
    search = re.finditer(regular, html_text)
    for found in search:
        call.append(found[0])
    return call


sample_html = "<img src='https://example.com/image1.jpg'> <img src='http://example.com/image2.png'> <img src='https://example.com/image3.gif'>"

image_call = extract_image_links(sample_html)
if image_call:
    for image_calls in image_call:
        print(image_calls)
else:
    print('Not found')
