from xml.etree import ElementTree as ET

from svg_concat.svg.grid_merge import GridMergeJob
from svg_concat.svg.measurement_unit import convert_to_pixels


def merge_svgs(output_file='merged.svg', *svg_files):
    svgs = [ET.parse(svg_file).getroot() for svg_file in svg_files]

    grid_merge_job = GridMergeJob(svgs)

    _write_merged_svg(output_file, grid_merge_job.svg)


def _write_merged_svg(output_file, merged_svg):
    # Write the merged SVG to a file
    with open(output_file, 'w') as f:
        ET.ElementTree(merged_svg).write(f, encoding='unicode', xml_declaration=True)


def line_merge_svgs(output_file='merged.svg', side_by_side=True, *svg_files):
    svgs = [ET.parse(svg_file).getroot() for svg_file in svg_files]

    # Calculate the total width and height
    widths = [convert_to_pixels(svg.attrib['width']) for svg in svgs]
    heights = [convert_to_pixels(svg.attrib['height']) for svg in svgs]

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

    _write_merged_svg(output_file, merged_svg)
