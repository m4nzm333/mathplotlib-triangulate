
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import TextBox

def trilaterate (p1, p2, p3, r1, r2, r3):
    x1, y1 = p1
    x2, y2 = p2
    x3, y3 = p3

    A = 2 * (x2 - x1)
    B = 2 * (y2 - y1)
    C = r1**2 - r2**2 - x1**2 + x2**2 - y1**2 + y2**2
    D = 2 * (x3 - x2)
    E = 2 * (y3 - y2)
    F = r2**2 - r3**2 - x2**2 + x3**2 - y2**2 + y3**2

    x = (C*E - F*B) / (E*A - B*D)
    y = (C*D - A*F) / (B*D - A*E)

    return x, y


# Initial point coordinates

initial_point_x0, initial_point_y0 = 1, 1
initial_point_x1, initial_point_y1 = 4, 1
initial_point_x2, initial_point_y2 = 2.5,4

# Circle properties
initial_circle_radius = 2
circle_color = 'green'
circle_alpha = 0.3

# Set up the figure and axis
fig, ax = plt.subplots()
#ax.set_xlim(0, 100)
#ax.set_ylim(0, 100)

# Plot the initial circle
circle0 = plt.Circle((initial_point_x0, initial_point_y0), initial_circle_radius, color=circle_color, alpha=circle_alpha)
circle1 = plt.Circle((initial_point_x1, initial_point_y1), initial_circle_radius, color=circle_color, alpha=circle_alpha)
circle2 = plt.Circle((initial_point_x2, initial_point_y2), initial_circle_radius, color=circle_color, alpha=circle_alpha)
ax.add_patch(circle0)
ax.add_patch(circle1)
ax.add_patch(circle2)


# Plot the initial point
point0, = ax.plot(initial_point_x0, initial_point_y0, 'yo', markersize=5)
point1, = ax.plot(initial_point_x1, initial_point_y1, 'yo', markersize=5)
point2, = ax.plot(initial_point_x2, initial_point_y2, 'yo', markersize=5)

initial_fpoint = trilaterate((initial_point_x0,initial_point_y0), (initial_point_x1,initial_point_y1), (initial_point_x2,initial_point_y2),initial_circle_radius,initial_circle_radius,initial_circle_radius)

Object, = ax.plot(initial_fpoint[0], initial_fpoint[1],'ro',markersize=5)
# Plot r line and value

line0, = plt.plot([initial_point_x0, initial_point_x0 + initial_circle_radius], [initial_point_y0, initial_point_y0],'r:')
line1, = plt.plot([initial_point_x1, initial_point_x1 + initial_circle_radius], [initial_point_y1, initial_point_y1],'r:')
line2, = plt.plot([initial_point_x2, initial_point_x2 + initial_circle_radius], [initial_point_y2, initial_point_y2],'r:')

# Display the initial radius value
radius0_text = ax.text(initial_point_x0 + initial_circle_radius / 2, initial_point_y0 , 
                        f"r₁: {initial_circle_radius:.1f}",ha='center',va='top', fontsize=7, color='black')
radius1_text = ax.text(initial_point_x1 + initial_circle_radius / 2, initial_point_y1,
                      f"r₂: {initial_circle_radius:.1f}",ha='center',va='top', fontsize=7, color='black')
radius2_text = ax.text(initial_point_x2 + initial_circle_radius / 2, initial_point_y2,
                      f"r₃: {initial_circle_radius:.1f}",ha='center',va='top', fontsize=7, color='black')
Station0_text = ax.text(initial_point_x0, initial_point_y0,
                      "Station 1",ha='right',va='bottom', fontsize=9, color='red')
Station1_text = ax.text(initial_point_x1, initial_point_y1,
                      "Station 2",ha='right',va='bottom', fontsize=9, color='red')

Station2_text = ax.text(initial_point_x2, initial_point_y2,
                      "Station 3",ha='right',va='bottom', fontsize=9, color='red')
Object_text = ax.text(initial_fpoint[0], initial_fpoint[1], "Object Position",ha='left',va='bottom',fontsize=9,color='black')

# Text box positions
text_x0_ax = plt.axes([0.15, 0.1, 0.15, 0.03], facecolor='lightgoldenrodyellow')
text_y0_ax = plt.axes([0.15, 0.06, 0.15, 0.03], facecolor='lightgoldenrodyellow')
text_radius0_ax = plt.axes([0.15, 0.02, 0.15, 0.03], facecolor='lightgoldenrodyellow')
text_x1_ax = plt.axes([0.35, 0.1, 0.15, 0.03], facecolor='lightgoldenrodyellow')
text_y1_ax = plt.axes([0.35, 0.06, 0.15, 0.03], facecolor='lightgoldenrodyellow')
text_radius1_ax = plt.axes([0.35, 0.02, 0.15, 

0.03], facecolor='lightgoldenrodyellow')
text_x2_ax = plt.axes([0.55, 0.1, 0.15, 0.03], facecolor='lightgoldenrodyellow')
text_y2_ax = plt.axes([0.55, 0.06, 0.15, 0.03], facecolor='lightgoldenrodyellow')
text_radius2_ax = plt.axes([0.55, 0.02, 0.15, 0.03], facecolor='lightgoldenrodyellow')

# Create the text boxes for X, Y coordinates, and the radius
text_x0 = TextBox(text_x0_ax, 'X₁', initial="{:.1f}".format(initial_point_x0))
text_y0 = TextBox(text_y0_ax, 'Y₁', initial="{:.1f}".format(initial_point_y0))
text_radius0 = TextBox(text_radius0_ax, 'r₁', initial="{:.1f}".format(initial_circle_radius))
text_x1 = TextBox(text_x1_ax, 'X₂', initial="{:.1f}".format(initial_point_x1))
text_y1 = TextBox(text_y1_ax, 'Y₂', initial="{:.1f}".format(initial_point_y1))
text_radius1 = TextBox(text_radius1_ax, 'r₂', initial="{:.1f}".format(initial_circle_radius))

text_x2 = TextBox(text_x2_ax, 'X₃', initial="{:.1f}".format(initial_point_x2))
text_y2 = TextBox(text_y2_ax, 'Y₃', initial="{:.1f}".format(initial_point_y2))
text_radius2 = TextBox(text_radius2_ax, 'r₃', initial="{:.1f}".format(initial_circle_radius))

# point_x0 = float(text_x0.text)
# point_y0 = float(text_y0.text)
# radius0 = float(text_radius0.text)
# point_x1 = float(text_x1.text)
# point_y1 = float(text_y1.text)
# radius1 = float(text_radius1.text)
# point_x2 = float(text_x2.text)
# point_y2 = float(text_y2.text)
# radius2 = float(text_radius2.text)



def update(val):
    print(type(val))
    """Update the circle, point, line, and radius text based on the text box values"""
    try:

        point_x0 = float(text_x0.text)
        point_y0 = float(text_y0.text)
        radius0 = float(text_radius0.text)
        point_x1 = float(text_x1.text)
        point_y1 = float(text_y1.text)
        radius1 = float(text_radius1.text)
        point_x2 = float(text_x2.text)
        point_y2 = float(text_y2.text)
        radius2 = float(text_radius2.text)


        point0.set_data(point_x0, point_y0)
        circle0.set_center((point_x0, point_y0))
        circle0.set_radius(radius0)
        point1.set_data(point_x1, point_y1)
        circle1.set_center((point_x1, point_y1))
        circle1.set_radius(radius1)
        point2.set_data(point_x2, point_y2)
        circle2.set_center((point_x2, point_y2))
        circle2.set_radius(radius2)


        line0.set_data([point_x0, point_x0 + radius0], [point_y0, point_y0])
        radius0_text.set_text(f"r1: {radius0:.2f}")
        radius0_text.set_position((point_x0 + radius0 / 2, point_y0 - 5))
        line1.set_data([point_x1, point_x1 + radius1], [point_y1, point_y1])

        radius1_text.set_text(f"r2: {radius1:.2f}")
        radius1_text.set_position((point_x1 + radius1 / 2, point_y1 - 5))
        line2.set_data([point_x2, point_x2 + radius2], [point_y2, point_y2])
        radius2_text.set_text(f"r3: {radius2:.2f}")
        radius2_text.set_position((point_x2 + radius2 / 2, point_y2 - 5))

        p0 = (point_x0,point_y0)
        p1 = (point_x1,point_y1)
        p2 = (point_x2,point_y2)

        fig.canvas.draw_idle()
    except ValueError:
        pass

# Onclick
def onclick(event):
    global ix, iy
    ix, iy = event.xdata, event.ydata
    print (f'x = {ix}, y = {iy}')

    # Update marker
    Object.set_xdata([ix])
    Object.set_ydata([iy])
    # Object, = ax.plot(ix, iy,'ro',markersize=5)
    Object_text.set_position((ix + 0.02 , iy + 0.02))

    return
cid = fig.canvas.mpl_connect('button_press_event', onclick)

# Connect the text boxes to the update 
text_x0.on_submit(update)
text_y0.on_submit(update)
text_radius0.on_submit(update)

text_x1.on_submit(update)
text_y1.on_submit(update)
text_radius1.on_submit(update)

text_x2.on_submit(update)
text_y2.on_submit(update)
text_radius2.on_submit(update)


plt.show()
