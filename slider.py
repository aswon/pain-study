import math

class Slider(object):
    """Creates a slider object.

    The slider works by calculating the distance between two marker objects.
    The smaller the distance, the smaller the resulting output. To create a
    slider increasing from left to right, for example, set one marker on the
    left, and have the participant hold the marker in his hand. As the marker
    is moved to the right, the distance will increase, and thus the slider
    value will also increase.

    Usage:

    # Create a slider half a meter long, with output from [0, 10]
    slider = Slider(0, 10, 0.5, marker_1, marker_2)

    # Get the current slider value
    value = slider.get_value()
    """

    def __init_(self, min_v, max_v, width, marker_1, marker_2):
        """Initializes the slider.

        Args:
            min_v: Minimum value of the slider (e.g. 0)
            max_v: Maximum value of the slider (e.g. 10)
            width: The width of the slider, in meters.
            marker_1, marker_2: Marker Node3D objects.
        """
        self.width = width
        self.marker_1 = marker_1
        self.marker_2 = marker_2

    def get_value(self):
        """Get the current slider value."""
        # Get the position of the two markers
        position_1 = self.marker_1.getPosition()
        position_2 = self.marker_2.getPosition()

        # Calculate the distance between the markers
        v = [i - j for i, j in zip(position_1, position_2)]
        d = math.sqrt(sum(i * i for i in v))

        # Interpolate the value between min_v and max_v
        s = d / width
        return min_v + s * (max_v - min_v)

