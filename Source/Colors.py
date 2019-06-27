import requests
from PIL import Image, ImageDraw

base_link = "https://api.noopschallenge.com/hexbot?count="


def get_colors(number_of_colors):
    if number_of_colors < 1:
        return "Your number of colors was invalid!"
    response = requests.get(base_link + str(int(number_of_colors)))
    data = response.json()
    data = data["colors"]
    if number_of_colors == 1:
        return data[0].get("value")
    else:
        list_of_hex = []
        for x in data:
            list_of_hex.append(x.get("value"))
        return list_of_hex


class ColorGrid:
    def __init__(self, x_count, y_count):
        self.x_count = x_count
        self.y_count = y_count
        self.hex_codes = []
        if x_count * y_count > 1000:
            for x in range(x_count):
                list_of_colors = get_colors(y_count)
                self.hex_codes.append(list_of_colors)
        else:
            list_of_colors = get_colors(x_count * y_count)
            self.hex_codes = [[list_of_colors[(x*y_count)+y] for y in range(y_count)] for x in range(x_count)]

    def draw_image(self, x_size, y_size):
        image = Image.new("RGB", (x_size, y_size), 'black')
        draw = ImageDraw.Draw(image)
        x_side_length, y_side_length = (x_size // self.x_count, y_size // self.y_count)
        for x in range(self.x_count):
            for y in range(self.y_count):
                draw.rectangle((x * x_side_length, y * y_side_length, (x+1) * x_side_length, (y+1) * y_side_length),
                               self.hex_codes[x][y])
        return image


# image_X, image_Y = (1000, 1000)
# grid = ColorGrid(100, 100)
# image = grid.draw_image(image_X, image_Y)
# image.show()
# image.save("../Images/Random_Success.png", "PNG")
