from config import config
import numpy as np

def convert_input_to_color(input_value):
    if np.issubdtype(type(input_value), int):
        color_mapping = dict(zip(config.COLORS_NUMBERS, config.COLORS))
        return color_mapping.get(input_value)
    elif isinstance(input_value, tuple):
        color_mapping = dict(zip(config.COLORS, config.COLORS_NUMBERS))
        return color_mapping.get(input_value)
    else:
        return None