from label_pil_2 import suggar_num_to_str_en, generate_label, suggar_num_to_str

title1 = "STARLING"
title2 = "Vyšnių vynas"
number_alcohol = 10.4
number_years = 2019
number_sweetness = 50
number_sweetness = suggar_num_to_str(number_sweetness)
color_var = 'rgb(255,255,255)'
color_var2 = 'rgb(0,0,0)'

image = generate_label(title1, title2, number_alcohol, number_years, number_sweetness, color_var, color_var2)

image.show()
image.save('label.png')

