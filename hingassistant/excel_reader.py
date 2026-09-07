def get_ingredients(product_sheet,last_row):
    ingredient = {}
    for i in range(last_row):
        if (product_sheet.cell(row=i+3,column=1).value) == "Total Weight":
            break

        if (product_sheet.cell(row=i + 3, column=2).value)==None and (product_sheet.cell(row=i + 3, column=3).value)==None and (product_sheet.cell(row=i + 3, column=4).value)==None:
            continue

        else:
            names = (product_sheet.cell(row=i + 3, column=1).value)
            q1 = (product_sheet.cell(row=i + 3, column=2).value)
            q2 = (product_sheet.cell(row=i + 3, column=3).value)
            q3 = (product_sheet.cell(row=i + 3, column=4).value)
            ingredient[names] = [q1, q2, q3]
    return ingredient

def get_cost(product_sheet,last_row):
    for i in range(last_row):
        if (product_sheet.cell(row=i+3,column=12).value) == "Net Cost":
            product_costing = product_sheet.cell(row=i+3,column=13).value
    return product_costing



