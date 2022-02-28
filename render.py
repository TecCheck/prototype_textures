import os;
import subprocess;

# Helper class to keep color and name together
class Color:
    name = ""
    color = ""

    def __init__(self, name, color):
        self.name = name
        self.color = color

def main():
    # CONFIGFIGURATION -----------------------------------------------------------------------
    # Define custom colors here:
    custom_colors = [
        Color("red", "#ef1b76"), Color("green", "#1bd977"), 
        Color("blue", "#04b8f9"), Color("orange", "#ff8205"), 
        Color("pink", "#c32af5"), Color("yellow", "#e8e10e"), 
        Color("navi_blue", "#242846"), Color("dark", "#333335"), 
        Color("light", "#d4d6d9"), Color("beige", "#cb965b")
    ]

    # Original Kenney colors:
    colors = [
        Color("dark", "#333335"), Color("light", "#d4d6d9"), Color("purple", "#9d22fa"), 
        Color("orange", "#ff8c00"), Color("green", "#1bd977"), Color("red", "#ff0038")
    ]

    # Define your output path here
    output_path = "out"

    # Choose between original or custom colors
    custom_colors = False
    # ----------------------------------------------------------------------------------------

    if custom_colors:
        colors = custom_colors

    # Get files in current dir
    files = [f for f in os.listdir('.') if os.path.isfile(f)]

    # Go through all colors
    for color in colors:
        print(color.name)
        path = output_path + os.path.sep + color.name

        if not os.path.exists(path):
            os.makedirs(path)

        for in_file in files:
            if not in_file.startswith("texture"):
                continue

            out_file_path = path + os.path.sep + in_file
            subprocess.call(['inkscape', in_file, '--export-area-page', '--export-type=png', '--export-background', color.color, '--export-filename', out_file_path])

if __name__ == "__main__":
    main()