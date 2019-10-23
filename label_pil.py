from PIL import Image, ImageDraw, ImageFilter, ImageEnhance, ImageFont, ImageDraw


def suggar_num_to_str(suggar):
    if suggar < 18:
        suggar_str = 'sausas'
    elif suggar < 31.5:
        suggar_str = 'pusiau sausas'
    elif suggar < 45:
        suggar_str = 'pusiau saldus'
    else:
        suggar_str = 'saldus'

    return suggar_str


def suggar_num_to_str_en(suggar):
    if suggar < 18:
        suggar_str = 'dry'
    elif suggar < 31.5:
        suggar_str = 'off-dry'
    elif suggar < 45:
        suggar_str = 'semi-sweet'
    else:
        suggar_str = 'sweet'

    return suggar_str


def find_middle(im, text, font):
    draw = ImageDraw.Draw(im)
    w, h = draw.textsize(text, font=font)
    return int(w/2)

def generate_label(title1, title2, number_alcohol, number_years, number_sweetness):
    number_alcohol = "alc. " + str(round(number_alcohol, 1)) + " % by Vol."
    number_sweetness = str(number_sweetness)
    number_years = str(number_years)

    font_size = 20
    font_offset = 20
    font_color = 'rgb(0, 0, 0)'
    font = ImageFont.truetype('fonts/Montserrat-Bold.otf', size=font_size)
    font_regular = ImageFont.truetype('fonts/Montserrat-Regular.otf', size=int(font_size))
    font_italic = ImageFont.truetype('fonts/Montserrat-Italic.otf', size=int(font_size / 1.2))

    img = Image.new(mode="RGB", size=(200, 200), color=(255, 179, 179))
    x, y = img.size

    draw = ImageDraw.Draw(img)
    draw.text((x / 2 - find_middle(img, title1, font), 0), title1, fill=font_color, font=font)
    draw.text((x / 2 - find_middle(img, title2, font_italic), 0 + font_size * 1 + font_offset), title2, fill=font_color, font=font_italic)
    draw.text((x / 2 - find_middle(img, number_alcohol, font_regular), 0 + font_size * 2 + font_offset), number_alcohol, fill=font_color, font=font_regular)
    draw.text((x / 2 - find_middle(img, number_sweetness, font_regular), 0 + font_size * 3 + font_offset), number_sweetness, fill=font_color, font=font_regular)
    draw.text((x / 2 - find_middle(img, number_years, font_regular), 0 + font_size * 4 + font_offset), number_years, fill=font_color, font=font_regular)
    return img
