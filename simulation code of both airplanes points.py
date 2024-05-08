from qgis.core import QgsProject, QgsPointXY, QgsGeometry
from qgis.PyQt.QtCore import QTimer
def interpolate_point(start_point, end_point, num_steps):
    x_step = (end_point.x() - start_point.x()) / num_steps
    y_step = (end_point.y() - start_point.y()) / num_steps
    intermediate_points = []
    for i in range(1, num_steps + 1):
        x = start_point.x() + i * x_step
        y = start_point.y() + i * y_step
        intermediate_points.append(QgsPointXY(x, y))
    return intermediate_points

# Define starting and ending points
start_point = QgsPointXY(62.3315, 25.1216)   # Starting point coordinates
end_point = QgsPointXY(73.0479, 33.6844)   # Ending point coordinates
num_steps = 100
intermediate_points = interpolate_point(start_point, end_point, num_steps)

# Initialize retindex
retindex = len(intermediate_points) - 2

# Function to update the point geometry and refresh the map canvas
def update_point():
    global current_index, retindex, y  # Declare y as global
    # Check if all intermediate points have been processed
    if retindex > 0:
        if current_index < len(intermediate_points):
            layer = QgsProject.instance().mapLayersByName("Gwadar")[0]
            x, y = intermediate_points[current_index]
            new_point = QgsPointXY(x, y)
            new_geometry = QgsGeometry.fromPointXY(new_point)
            layer.startEditing()
            layer.changeGeometry(0, new_geometry)
            layer.commitChanges()
            iface.mapCanvas().refresh()
            current_index += 1
        # Move "Islamabad" point if y-coordinate condition is met
        if y >= 32.05746800000000007:
            layer2 = QgsProject.instance().mapLayersByName("Islamabad")[0]
          
            # Ensure retindex is within the range
            a, b = intermediate_points[retindex]
            
            neww_point = QgsPointXY(a, b)
            neww_geometry = QgsGeometry.fromPointXY(neww_point)
            layer2.startEditing()
            layer2.changeGeometry(0, neww_geometry)
            layer2.commitChanges()
            iface.mapCanvas().refresh()
            retindex -= 1
            
    else:
        timer.stop()  # Stop the timer when all points have been processed

# Initialize the current index
current_index = 0

# Create a QTimer to control the interval between updates
timer = QTimer()
timer.timeout.connect(update_point)

# Set the interval (milliseconds)
interval = 100  # Adjust this value as needed for smooth animation

# Start the timer
timer.start(interval)

