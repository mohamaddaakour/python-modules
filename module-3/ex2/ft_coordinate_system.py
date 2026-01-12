import sys
import math

def distance_3d(p1, p2):
    x1, y1, z1 = p1
    x2, y2, z2 = p2
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2 + (z2 - z1) ** 2)

def parse_coordinates(coord_str):
    parts = coord_str.split(",")
    return tuple(int(part) for part in parts)

def main():
    print("=== Game Coordinate System ===")

    origin = (0, 0, 0)
    position = (10, 20, 5)

    print(f"Position created: {position}")
    dist = distance_3d(origin, position)
    print(f"Distance between {origin} and {position}: {round(dist, 2)}")

    coord_string = "3,4,0"
    print(f'Parsing coordinates: "{coord_string}"')
    try:
        parsed_position = parse_coordinates(coord_string)
        print(f"Parsed position: {parsed_position}")
        dist = distance_3d(origin, parsed_position)
        print(f"Distance between {origin} and {parsed_position}: {dist}")
    except Exception as e:
        print(f"Error parsing coordinates: {e}")

    invalid_string = "abc,def,ghi"
    print(f'Parsing invalid coordinates: "{invalid_string}"')
    try:
        parse_coordinates(invalid_string)
    except Exception as e:
        print(f"Error parsing coordinates: {e}")
        print(f"Error details - Type: {type(e).__name__}, Args: {e.args}")

    print("Unpacking demonstration:")
    x, y, z = parsed_position
    print(f"Player at x={x}, y={y}, z={z}")
    print(f"Coordinates: X={x}, Y={y}, Z={z}")

if __name__ == "__main__":
    main()
