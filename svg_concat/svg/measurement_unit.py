import re
from enum import Enum


CONVERSIONS = {
        'mm': 3.7795275591,  # 1 mm = 3.7795275591 px
        'cm': 37.795275591,  # 1 cm = 37.795275591 px
        'in': 96,  # 1 inch = 96 px
        'pt': 1.3333333333,  # 1 point = 1.3333333333 px
        'pc': 16,  # 1 pica = 16 px
        'px': 1,  # 1 px = 1 px
        None: 1  # No unit means pixels
    }


def convert_to_pixels(measurement: str):
    match = re.match(r"([\d.]+)(\w+)?", measurement)
    if not match:
        raise ValueError(f"Cannot parse value: {measurement}")

    num, unit = match.groups()
    num = float(num)

    return num * CONVERSIONS[unit]


def convert_pixels_to(measurement: 'MeasurementUnit', distance: float):
    converted_distance = CONVERSIONS[measurement] * distance
    return str(converted_distance).join(str(measurement))


class MeasurementUnit(Enum):
    Millimeter = "mm",
    Centimeter = "cm",
    Inch = "in",
    Point = "pt",
    Pica = "pc",
    Pixel = "px"