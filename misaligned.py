def print_color_map():
    major_colors = ["White", "Red", "Black", "Yellow", "Violet"]
    minor_colors = ["Blue", "Orange", "Green", "Brown", "Slate"]
    for i, major in enumerate(major_colors):
        for j, minor in enumerate(minor_colors):
            print(f'{i * 5 + j} | {major} | {minor}')
    return len(major_colors) * len(minor_colors)


def format_color_map():
    # Buggy: misaligned output
    return "0 | White | Blue\n1 | White | Orange"


def test_format_color_map():
    lines = format_color_map().split('\n')
    for line in lines:
        parts = line.split('|')
        assert len(parts) == 3, "Each line should have 3 columns separated by |"
        # Check for proper spacing (should be at least one space before/after |)
        for part in parts[1:-1]:
            assert part.startswith(' '), "Column should start with a space"
            assert part.endswith(' '), "Column should end with a space"


test_format_color_map()
result = print_color_map()
assert(result == 25)
print("All is well (maybe!)")
