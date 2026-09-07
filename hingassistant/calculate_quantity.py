def calculate_quantity(ingredients,scaling_factor):
    step_1 = {}
    step_2 = {}
    step_3 = {}

    for key, value in ingredients.items():
            if value[0] != None:
                step_1[key] = round(value[0] * scaling_factor,2)


            if value[1] != None:
                step_2[key] = round(value[1] * scaling_factor, 2)


            if value[2] != None:
                step_3[key] = round(value[2] * scaling_factor, 2)

    return step_1, step_2, step_3
