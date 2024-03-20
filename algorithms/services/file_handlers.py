import re


def get_string_from_file(file):
    try:
        data = (file.read()).decode()
        return data
    except Exception:
        return 'incorrect file format, send txt file with separated numbers like: 12 3 4'


def get_num_from_file(file):
    data = (file.read()).decode()
    num = re.findall('\d', data)
    return int(num[0])
