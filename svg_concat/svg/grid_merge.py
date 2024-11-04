import math
import more_itertools
from xml.etree import ElementTree as ET

from svg_concat.svg.measurement_unit import convert_to_pixels, MeasurementUnit


class GridMergeJob:
    def __init__(self, svgs_to_merge: list[ET.Element], measurement: MeasurementUnit = MeasurementUnit.Pixel) -> None:
        number_svgs = len(svgs_to_merge)
        rows = math.ceil(math.sqrt(number_svgs))
        self.grid = [tuple(row) for row in more_itertools.divide(rows, svgs_to_merge)]

        self.width, self.height = self._get_dimensions()
        self.measurement = measurement

        self.svg = ET.Element('svg', attrib={
            'xmlns': "http://www.w3.org/2000/svg",
            'width': f"{self.width}{measurement.value}",
            'height': f"{self.height * rows}{measurement.value}",
            'version': "1.1"
        })

        self._generate_svg()

    def _get_dimensions(self) -> tuple[float, float]:
        widest_row_width = 0.0
        tallest_row_height = 0.0

        for row in self.grid:
            row_width = 0.0
            row_height = 0.0
            for column in row:
                row_width += convert_to_pixels(column.attrib["width"])
                row_height += convert_to_pixels(column.attrib["height"])

            if row_width > widest_row_width:
                widest_row_width = row_width

            if row_height > tallest_row_height:
                tallest_row_height = row_height

        return widest_row_width, tallest_row_height

    def _generate_svg(self):
        current_y_offset = 0

        for row in self.grid:
            self._generate_svg_for_row(row, current_y_offset)
            current_y_offset += self.height

    def _generate_svg_for_row(self, row, current_y_offset):
        current_x_offset = 0

        for svg in row:
            width = convert_to_pixels(svg.attrib["width"])
            group = ET.Element('g', attrib={
                "transform": f"translate({current_x_offset}, {current_y_offset})",
            })
            group.extend(svg)

            self.svg.append(group)

            current_x_offset += width + 2


