from pathlib import Path
from google.cloud import vision

p = Path(__file__).parent / 'load-sign.jpg'

client = vision.ImageAnnotatorClient()

with p.open('rb') as image_file:
    content = image_file.read()

image = vision.types.Image(content=content)

response = client.text_detection(image=image)

for text in response.text_annotations:
    print(text.description)