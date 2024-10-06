import tkinter as tk  # Import tkinter for the GUI components
from tkinter.colorchooser import askcolor  # Import color chooser to change the pen color

# Function to start drawing when the mouse button is pressed
def start_drawing(event):
    global is_drawing, prev_x, prev_y  # Variables to track drawing state and previous coordinates
    is_drawing = True
    prev_x, prev_y = event.x, event.y  # Store initial mouse position

# Function to draw on the canvas when the mouse is dragged
def draw(event):
    global is_drawing, prev_x, prev_y
    if is_drawing:
        current_x, current_y = event.x, event.y  # Get the current mouse position
        # Draw a line from the previous to the current position
        canvas.create_line(prev_x, prev_y, current_x, current_y, fill=drawing_color, width=line_width, capstyle=tk.ROUND, smooth=True)
        prev_x, prev_y = current_x, current_y  # Update previous coordinates

# Function to stop drawing when the mouse button is released
def stop_drawing(event):
    global is_drawing
    is_drawing = False  # Set drawing state to False

# Function to change the pen color using a color chooser dialog
def change_pen_color():
    global drawing_color
    color = askcolor()[1]  # Ask for a color and get its hex value
    if color:
        drawing_color = color  # Update the drawing color

# Function to change the line width based on the slider value
def change_line_width(value):
    global line_width
    line_width = int(value)  # Update the line width

# Initialize the main window
root = tk.Tk()
root.title("Whiteboard App")  # Set the window title

# Create the canvas for drawing
canvas = tk.Canvas(root, bg="white")
canvas.pack(fill="both", expand=True)  # Expand the canvas to fill the window

# Initialize drawing variables
is_drawing = False
drawing_color = "black"  # Default color
line_width = 2  # Default line width

root.geometry("800x600")  # Set window size

# Create a frame for holding control buttons and sliders
controls_frame = tk.Frame(root)
controls_frame.pack(side="top", fill="x")

# Button to change pen color
color_button = tk.Button(controls_frame, text="Change Color", command=change_pen_color)
# Button to clear the canvas
clear_button = tk.Button(controls_frame, text="Clear Canvas", command=lambda: canvas.delete("all"))

color_button.pack(side="left", padx=5, pady=5)
clear_button.pack(side="left", padx=5, pady=5)

# Label and slider to control line width
line_width_label = tk.Label(controls_frame, text="Line Width:")
line_width_label.pack(side="left", padx=5, pady=5)

line_width_slider = tk.Scale(controls_frame, from_=1, to=10, orient="horizontal", command=lambda val: change_line_width(val))
line_width_slider.set(line_width)  # Set default line width on the slider
line_width_slider.pack(side="left", padx=5, pady=5)

# Bind mouse events for drawing
canvas.bind("<Button-1>", start_drawing)  # Start drawing on mouse click
canvas.bind("<B1-Motion>", draw)  # Draw while dragging the mouse
canvas.bind("<ButtonRelease-1>", stop_drawing)  # Stop drawing when the mouse is released

# Add a text widget for taking notes
text_widget_label = tk.Label(controls_frame, text="Notes:")
text_widget_label.pack(side="top", padx=5, pady=5)
text_widget = tk.Text(controls_frame, height=6, width=120)  # Create a text widget for notes
text_widget.pack(side="left", padx=5, pady=5)

# Start the main event loop
root.mainloop()
