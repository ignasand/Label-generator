from PIL import Image, ImageDraw, ImageFilter, ImageEnhance, ImageFont, ImageDraw, ImageOps


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
        suggar_str = 'dry '
    elif suggar < 31.5:
        suggar_str = 'off-dry '
    elif suggar < 45:
        suggar_str = 'semi-sweet'
    else:
        suggar_str = 'sweet'

    return suggar_str


def find_middle(im, text, font):
    draw = ImageDraw.Draw(im)
    w, h = draw.textsize(text, font=font)
    return int(w/2)


def generate_label(title1, title2, number_alcohol, number_years, number_sweetness, color_var, color_val2):
    number_alcohol = "alc. " + str(round(number_alcohol, 1)) + " % by Vol."
    number_sweetness = str(number_sweetness)
    number_years = str(number_years)

    font_size = 25 * 2
    font_offset = 20
    font_color = color_val2
    # print(font_color)
    # font_color = 'rgb(0, 0, 0)'
    font = ImageFont.truetype('fonts/Montserrat-Bold.otf', size=font_size)
    font_regular = ImageFont.truetype('fonts/Montserrat-Regular.otf', size=int(font_size / 1.2))
    font_italic = ImageFont.truetype('fonts/Montserrat-Italic.otf', size=int(font_size / 1.5))

    # img = Image.new(mode="RGB", size=(int(1240/5-12), int(1754/5-12)), color=(227, 194, 127))

    # img = Image.new(mode="RGB", size=(int(1240 / 5 - 12), int(1754 / 5 - 12)), color=(255, 255, 255))

    img = Image.new(mode="RGB", size=(int(2480 / 5 - 12), int(3508 / 5 - 12)), color=color_var)

    basewidth = 200
    img_temp = Image.open("static/img/bird2.jpg")
    wpercent = (basewidth / float(img_temp.size[0]))
    hsize = int((float(img_temp.size[1]) * float(wpercent)))
    img_temp = img_temp.resize((basewidth, hsize), Image.ANTIALIAS)
    img.paste(img_temp, (0, 0))




    x, y = img.size

    draw = ImageDraw.Draw(img)

    if find_middle(img, title1, font) * 2 < x - 10:
        draw.text((x / 2 - find_middle(img, title1, font), 2 / 6 * y - 1 * font_size), title1, fill=font_color, font=font)
    else:
        w = find_middle(img, title1, font) * 2
        font_temp = ImageFont.truetype('fonts/Montserrat-Bold.otf', size=int(font_size * (x - 10) / w))
        draw.text((x / 2 - find_middle(img, title1, font_temp), 2 / 6 * y - 1 * font_size), title1, fill=font_color,
                  font=font_temp)

    if find_middle(img, title2, font_regular) * 2 < x - 10:
        draw.text((x / 2 - find_middle(img, title2, font_regular), 3 / 6 * y - 0.5 * font_size),
                  title2, fill=font_color, font=font_regular)
    else:
        w = find_middle(img, title2, font_regular) * 2
        font_regular_temp = ImageFont.truetype('fonts/Montserrat-Regular.otf', size=int(((font_size * (x - 10) / w)) / 1.2))
        draw.text((x / 2 - find_middle(img, title2, font_regular_temp), 3 / 6 * y - 0.5 * font_size),
                  title2, fill=font_color, font=font_regular_temp)




    draw.text((x / 2 - find_middle(img, number_years, font_regular), 4 / 6 * y - 0.5 * font_size),
              number_years, fill=font_color, font=font_regular)
    draw.text((x / 2 - find_middle(img, number_sweetness, font_italic), 5 / 6 * y - 0.5 * font_size),
              number_sweetness, fill=font_color, font=font_italic)
    draw.text((x / 2 - find_middle(img, number_alcohol, font_italic), 5 / 6 * y + 0.5 * font_size),
              number_alcohol, fill=font_color, font=font_italic)

    img = ImageOps.expand(img, border=3, fill='black')
    img = ImageOps.expand(img, border=3, fill='white')

    return img
