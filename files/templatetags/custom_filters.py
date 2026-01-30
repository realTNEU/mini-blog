from django import template

register = template.Library()

@register.filter
def file_icon(file_type):
    """Return Font Awesome icon class for file type"""
    icons = {
        'excel': 'fa-file-excel',
        'csv': 'fa-table',
        'pdf': 'fa-file-pdf',
        'image': 'fa-image',
        'other': 'fa-file',
    }
    return icons.get(file_type, 'fa-file')


@register.filter(name="divideby")
def divideby(value, arg):
    """
    Divide a numeric value by arg.

    Used in templates as: {{ value|divideby:200 }}
    Returns 0 if inputs are invalid or divisor is 0.
    """
    try:
        numerator = float(value)
        denominator = float(arg)
        if denominator == 0:
            return 0
        result = numerator / denominator
        return int(result) if result >= 0 else int(result)
    except (TypeError, ValueError):
        return 0
