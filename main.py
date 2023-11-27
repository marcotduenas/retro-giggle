from PIL import Image, ImageDraw, ImageFont
import random

# get_info is a function to retrieve fundamental information to generate some meme. 
#This function will be responsible for getting image width and height and also 
#get information about the captions that will be used.
def get_info_about_the_meme(user_image):
    img_width, img_height = user_image.size
    generate_meme(img_width, img_height, user_image)

def generate_meme(width, height, image_path):
    top_caption = input("What's the top caption?\n")
    top_caption = top_caption.upper()
    bottom_caption = input("What's the bottom caption\n")
    bottom_caption = bottom_caption.upper()
    text_aligned_to_center = width // 2
    top_caption_height = 300
    botton_caption_height = height - 400
    artist = ImageDraw.Draw(image_path)

    #Defying custom meme font
    custom_meme_font =  ImageFont.truetype('./src/fonts/impact.ttf', 512)

    artist.text((text_aligned_to_center, top_caption_height), top_caption, font = custom_meme_font, fill = (255, 255, 255), stroke_width = 10, stroke_fill = 'black', anchor = 'mm')
    artist.text((text_aligned_to_center, botton_caption_height), bottom_caption, font = custom_meme_font, fill = (255, 255, 255), stroke_width = 10, stroke_fill = 'black', anchor = 'mm')


    file_name = int(random.randint(1111, 9999))
    image_path.save(f'{file_name}.png')
    print(f"Meme created and save into {file_name}.png")
    

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

if __name__ == "__main__":
    main()

