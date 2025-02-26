COLOR_TO_CODE = {"Aqua": "#00ffff", "Absolute Zero": "#0048ba",
                 "Acid Green": "#b0bf1a", "Amaranth": "#e52b50",
                 "Baby Pink": "#f4c2c2", "Bright Green": "#66ff00",
                 "Cadmium Yellow": "#fff600", "Carolina Blue": "#56a0d3",
                 "Cornsilk1": "#fff8dc", "DodgerBlue1": "#1e90ff"}
COLOR_TO_CODE = {color.lower(): code for color, code in COLOR_TO_CODE.items()}

color = input("Enter a color name: ").lower()
while color != "":
    if color in COLOR_TO_CODE:
        print(COLOR_TO_CODE[color])
    else:
        print("Invalid color name")
    color = input("Enter a color name: ").lower()
