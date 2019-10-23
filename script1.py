from label_pil import suggar_num_to_str_en, generate_label

title1 = "Wine title"
title2 = "Grape wine"
number_alcohol = 11.05
number_years = 2019
number_sweetness = 44

image = generate_label(title1, title2, number_alcohol, number_years, number_sweetness)

image.show()