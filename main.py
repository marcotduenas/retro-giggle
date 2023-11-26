from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

choosen_template = Image.open('./src/img/tmpl_cat_suprised.jpg')
meme_string = "omg it's a cat"
meme_string = meme_string.upper()

# artist is the variable used to call the draw method
artist = ImageDraw.Draw(choosen_template)

custom_meme_font = ImageFont.truetype('./src/fonts/impact.ttf', 512)

artist.text((28, 36), meme_string, font=custom_meme_font, fill=(255, 0, 0))

choosen_template.save('cat_test.png')
