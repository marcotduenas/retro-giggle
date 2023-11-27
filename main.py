from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont


# get_info is a function to retrieve fundamental information to generate some meme. 
#This function will be responsible for getting image width and height and also 
#get information about the captions that will be used.
def get_info_about_the_meme(user_image):
    w, h = user_image.size
    print(w, h)

def generate_meme():
    pass

def main():
    user_template = int(input("Choose a meme template:\n1- Suprised Cat\n2- Smiling dog\n3- Old man\n"))
    template_path = ''


    match user_template:
        case 1:
            template_path = './src/img/tmpl_cat_suprised.jpg'
            choosen_template = Image.open(template_path)
            get_info_about_the_meme(choosen_template)
        case 2:
            template_path= './src/img/tmpl_dog_smile.jpg'
            choosen_template = Image.open(template_path)
            get_info_about_the_meme(choosen_template)
        case 3:
            template_path = './src/img/tmpl_old_man.jpg'
            choosen_template = Image.open(template_path)
            get_info_about_the_meme(choosen_template)

    print(template_path)

if __name__ == "__main__":
    main()

'''
choosen_template = Image.open('./src/img/tmpl_dog_smile.jpg')
img_width, img_height = choosen_template.size
meme_string = "omg it's a cat"
meme_string = meme_string.upper()
meme_string2 = "he is furious"
meme_string2 = meme_string2.upper()
half_w = img_width // 2
meme_bottom_caption_height = img_height - 400 # With some tests, I discovered that this value is good in most images
# artist is the variable used to call the draw method
artist = ImageDraw.Draw(choosen_template)

custom_meme_font = ImageFont.truetype('./src/fonts/impact.ttf', 512)

artist.text((half_w, 300), meme_string, font=custom_meme_font, fill=(255, 255, 255), stroke_width=10, stroke_fill='black', anchor="mm")
artist.text((half_w, meme_bottom_caption_height), meme_string2, font=custom_meme_font, fill=(255, 255, 255), stroke_width=10, stroke_fill='black', anchor="mm")

choosen_template.save('cat_test.png')
'''
