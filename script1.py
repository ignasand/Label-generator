from label_pil import suggar_num_to_str_en, generate_label

title1 = "iki 25"
title2 = "very good Grape wine"
number_alcohol = 11.05
number_years = 2019
number_sweetness = 10
number_sweetness = suggar_num_to_str_en(number_sweetness)

image = generate_label(title1, title2, number_alcohol, number_years, number_sweetness)

image.show()