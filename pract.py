from PIL import Image
import numpy


def extract_color_code(path):
    image = Image.open(path)
    array = numpy.array(image)
    colors = {}
    top_10_colors = {}
    for row in array:
        for pixel in row:
            color = tuple(int(x) for x in pixel)
            if color in colors:
                colors[color] += 1
            else:
                colors[color] = 1

    for color, count in sorted(list(colors.items()), key=lambda x: x[-1], reverse=True)[:50]:
        # list_top_color_with_namimg = f"color:{color} and count: {count}"
        color_string = f"{color}"
        top_10_colors[color_string] = count
        # top_10_colors[color] = count
    return top_10_colors


# demo of getting path of image
# d = extract_color_code("static/img/rgb.jpg")
#
# for key,value in d.items():
#     print(type(value))
