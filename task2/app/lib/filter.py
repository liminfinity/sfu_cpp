from re import findall, MULTILINE

def filter_figures(figuresStr: str) -> list[str]:
    figures: list[str] = []
    point_regexp = r'Point\((?:[-+]?\d*\.\d+|\d+),\s*(?:[-+]?\d*\.\d+|\d+)\)'
    line_regexp = rf'^Line\({point_regexp},\s*{point_regexp}\)$'
    circle_regexp = rf'^Circle\({point_regexp},\s*(?:\d+)\)$'
    figures.extend(findall(rf'^{point_regexp}$', figuresStr, flags=MULTILINE))
    figures.extend(findall(line_regexp, figuresStr, flags=MULTILINE))
    figures.extend(findall(circle_regexp, figuresStr, flags=MULTILINE))
    return figures