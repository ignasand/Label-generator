from PIL import Image, ImageDraw, ImageFilter, ImageEnhance, ImageFont


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


def generate_label(title1, title2, number_alcohol, number_years, number_sweetness):
    font_size = 20
    font_color = 'rgb(0, 0, 0)'
    font = ImageFont.truetype('fonts/Montserrat-Bold.otf', size=font_size)
    font_regular = ImageFont.truetype('fonts/Montserrat-Regular.otf', size=int(font_size))
    font_italic = ImageFont.truetype('fonts/Montserrat-Italic.otf', size=int(font_size / 1.2))

    img = Image.new(mode="RGB", size=(200, 323), color=(255, 179, 179))
    x, y = img.size

    draw = ImageDraw.Draw(img)
    draw.text((0, 0), title1, fill=font_color, font=font)
    draw.text((0, 0 + font_size * 1), title2, fill=font_color, font=font_italic)
    draw.text((0, 0 + font_size * 2), "alc. " + str(round(number_alcohol, 1)) +" % by Vol.", fill=font_color, font=font_regular)
    draw.text((0, 0 + font_size * 3), str(number_sweetness), fill=font_color, font=font_regular)
    draw.text((0, 0 + font_size * 4), str(number_years), fill=font_color, font=font_regular)
    return img
