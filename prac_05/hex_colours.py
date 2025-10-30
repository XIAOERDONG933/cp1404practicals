COLOR_TO_HEX = {"AbsoluteZero": "#0048ba", "AcidGreen": "#b0bf1a", "AliceBlue": "#f0f8ff", "Amaranth": "#e52b50",
                "Aqua": "#00ffff", "Aureolin": "#fdee00", "Beaver": "#9f8170", "BlueViolet": "#8a2be2",
                "BrightGreen": "#66ff00", "Bronze": "#cd7f32"}

color_name = input("Please enter color name: ").strip()

while color_name:
    try:
        print(f"{color_name} has hex code {COLOR_TO_HEX[color_name]}")
    except KeyError:
        print("Invalid color name")
    color_name = input("Please enter name: ").strip()