#area of shape

def area_of_shape(shape, **dimensions):
    if shape == "circle":
        return 3.14159 * dimensions["radius"] ** 2
    elif shape == "rectangle":
        return dimensions["length"] * dimensions["width"]
    elif shape == "triangle":
        return 0.5 * dimensions["base"] * dimensions["height"]
    else:
        return "Invalid shape"
print(area_of_shape("circle", radius=5))
print(area_of_shape("rectangle", length=4, width=6))
print(area_of_shape("triangle", base=3, height=7))
