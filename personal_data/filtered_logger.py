import re

def filter_datum(fields, redaction, message, separator):
    regex = re.compile(f'({re.escape(separator)}|^)({"|".join(map(re.escape, fields))}){re.escape(separator)}')
    return re.sub(regex, lambda match: f'{match.group(1)}{redaction}{match.group(3)}', message)