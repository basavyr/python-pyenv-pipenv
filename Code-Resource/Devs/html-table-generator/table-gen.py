

from cgitb import reset


def generate_header(headers):
    res_string = f'<tr>\n'
    for header in headers:
        res_string += f'<th>{header}</th>\n'
    res_string += f'</tr>\n'

    return res_string


def generate_rows(n_rows, n_cols):
    res_string = ''
    for row in range(n_rows - 1):
        item = '<tr>\n'
        for col in range(n_cols):
            item += '<td></td>\n'
        item += '</tr>'
        res_string += item

    return res_string


def table(headers, n_rows, n_cols):
    T = '<table style="" class="" id ="">\n'
    H = generate_header(headers)
    R = generate_rows(n_rows, n_cols)
    T += H
    T += R
    T += '\n</table>\n'
    print(T)


def main():
    table(['h1', 'h2', 'h3'], 3, 3)


if __name__ == '__main__':
    main()
