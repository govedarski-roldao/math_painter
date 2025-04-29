from canvas import Canvas, color_map
from shapes import Rectangle, Square
import os

canvas_width = int(input("Enter Canvas width: "))
canvas_height = int(input("Enter Canvas height: "))
canvas_color = input("Enter canvas color: ")

while canvas_color not in color_map:
    canvas_color = input("Please introduce a valid color: ").lower()

format_not_accepted = True
while format_not_accepted:
    image_format = input("Please introduce the output format of your image:")
    if image_format.lower() in ("jpeg", "png", "raw", "tiff"):
        format_not_accepted = False
    else:
        print("\n" * 100)
        print("Please Introduce a valid format")

canvas = Canvas(height=canvas_height, width=canvas_width, color=canvas_color, format="jpg")

while True:
    shape_type = input("What do you like to draw? (Square or Rectangle?) Enter quit to quit. ").capitalize()
    if shape_type in ("Square", "Rectangle"):
        try:
            init_pos_x = int(input(f"Enter the x of the {shape_type.lower()}: "))
            init_pos_y = int(input(f"Enter the y of the {shape_type.lower()}: "))
        except ValueError:
            print("Coordinates must be integers. Try again.")
            continue

        object_color = input(f"Choose a color for your {shape_type.lower()}: ").lower()
        while object_color not in color_map:
            object_color = input("Please introduce a valid color: ").lower()

        if shape_type == "Rectangle":
            rec_height = int(input("Please introduce the height of the Rectangle: "))
            rec_width = int(input("Please introduce the width of the Rectangle: "))
            object = Rectangle(init_pos_x, init_pos_y, rec_width, rec_height, object_color)
        else:
            square_size = int(input("Please, introduce the size of the square side: "))
            object = Square(init_pos_x, init_pos_y, square_size, object_color)
        object.draw(canvas)
    elif shape_type == "Quit":
        canvas.make()
        break
    else:
        print("\n" * 100)
        print("Please introduce a valid shape (Square or Rectangle).")

# r1 = Rectangle(x=10, y=20, color="orange", width=10, height=2)
# r1.draw(canvas)
# s1 = Square(5, 7, 20, "blue")
# s1.draw(canvas)
# canvas.make()
