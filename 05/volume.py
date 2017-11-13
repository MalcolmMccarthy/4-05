'''
made by malcolm
on nov 2017
in ics3u
calculates volume of a cylinder
'''
import ui

PI = 3.14
#process
def calculate(radius, height):
    
     volume = 2 * PI * radius ** 2 * height
     return volume
    
def calculate_button(sender):
    # input
    radius = int(view['radius_textfield'].text)
    height = int(view['height_textfield'].text)
    answer = calculate(radius, height)
    view['answer_label'].text = "the total volume is: " + str(answer) + "cm**3"

view = ui.load_view()
view.present('sheet')
