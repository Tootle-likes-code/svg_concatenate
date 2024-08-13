import svgwrite
from xml.etree import ElementTree as ET
import re


def parse_unit(value):
    """Parse a value with units like '91.302299mm' into pixels."""
    match = re.match(r"([\d\.]+)(\w+)?", value)
    if not match:
        raise ValueError(f"Cannot parse value: {value}")

    num, unit = match.groups()
    num = float(num)

    # Conversion factors to pixels
    conversions = {
        'mm': 3.7795275591,  # 1 mm = 3.7795275591 px
        'cm': 37.795275591,  # 1 cm = 37.795275591 px
        'in': 96,  # 1 inch = 96 px
        'pt': 1.3333333333,  # 1 point = 1.3333333333 px
        'pc': 16,  # 1 pica = 16 px
        'px': 1,  # 1 px = 1 px
        None: 1  # No unit means pixels
    }

    return num * conversions.get(unit, 1)


def merge_svgs(output_file='merged.svg', side_by_side=True, *svg_files):
    svgs = [ET.parse(svg_file).getroot() for svg_file in svg_files]

    # Calculate the total width and height
    widths = [parse_unit(svg.attrib['width']) for svg in svgs]
    heights = [parse_unit(svg.attrib['height']) for svg in svgs]

    if side_by_side:
        total_width = sum(widths)
        total_height = max(heights)
    else:
        total_width = max(widths)
        total_height = sum(heights)

    # Create a new root SVG element
    merged_svg = ET.Element('svg', attrib={
        'xmlns': "http://www.w3.org/2000/svg",
        'width': f"{total_width}px",
        'height': f"{total_height}px",
        'version': "1.1"
    })

    current_x = 0
    current_y = 0

    for svg, width, height in zip(svgs, widths, heights):
        # Adjust the position of each SVG by setting a new `transform` attribute
        group = ET.Element('g', attrib={
            'transform': f"translate({current_x},{current_y})"
        })
        group.extend(svg)  # Add all elements from the original SVG to the group

        # Append the group to the merged SVG
        merged_svg.append(group)

        # Update the position for the next SVG
        if side_by_side:
            current_x += width
        else:
            current_y += height

    # Write the merged SVG to a file
    with open(output_file, 'w') as f:
        ET.ElementTree(merged_svg).write(f, encoding='unicode', xml_declaration=True)

