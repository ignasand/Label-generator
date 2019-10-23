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
