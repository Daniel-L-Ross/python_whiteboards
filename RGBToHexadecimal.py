"""
Write a function that takes in RGB color values and converts it into the hexadecimal color.
The function should take three arguments for the R, G, and B values.
If the R, G, or B values are outside of the 0 to 255 range they should be converted to the closest number in that range
"""

def hex_color_val(num):
    if num > 255 or num < 0:
        return "FF" if num > 255 else "00"
    val = hex(num)[2:].upper()
    return val if len(val) == 2 else ("0" + val)

def rgb_to_hex(red, green, blue):
    hex_color = ""
    hex_color += hex_color_val(red)
    hex_color += hex_color_val(green)
    hex_color += hex_color_val(blue)
    return hex_color


def test_rgb_solution():
    assert rgb_to_hex(255, 255, 255) == 'FFFFFF'
    assert rgb_to_hex(255, 255, 300) == 'FFFFFF'
    assert rgb_to_hex(0, 0, 0) == '000000'
    assert rgb_to_hex(148, 0, 211) == '9400D3'
    assert rgb_to_hex(254,253,252) == "FEFDFC"
    assert rgb_to_hex(220, 67, 368) == "DC43FF"

test_rgb_solution()