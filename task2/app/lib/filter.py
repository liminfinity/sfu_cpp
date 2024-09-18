from re import findall, MULTILINE

def filter_figures(figuresStr: str) -> list[str]:
    figures: list[str] = []
    point_regexp = r'^Point\((?:[-+]?\d*\.\d+|\d+),\s*(?:[-+]?\d*\.\d+|\d+)\)$'
    line_regexp = r'^Line\(Point\((?:[-+]?\d*\.\d+|\d+),\s*(?:[-+]?\d*\.\d+|\d+)\),\s*Point\((?:[-+]?\d*\.\d+|\d+),\s*(?:[-+]?\d*\.\d+|\d+)\)\)$'
    circle_regexp = r'^Circle\(Point\((?:[-+]?\d*\.\d+|\d+),\s*(?:[-+]?\d*\.\d+|\d+)\),\s*(?:\d+)\)$'
    figures.extend(findall(point_regexp, figuresStr, flags=MULTILINE))
    figures.extend(findall(line_regexp, figuresStr, flags=MULTILINE))
    figures.extend(findall(circle_regexp, figuresStr, flags=MULTILINE))
    return figures