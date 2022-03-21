

from cgitb import reset


def generate_header(headers):
    res_string = f'<tr>\n'
    for header in headers:
        res_string += f'<th>{header}</th>\n'
    res_string += f'</tr>\n'

    return res_string


def generate_rows(n_rows, n_cols, table_data):
    res_string = ''
    for row in range(n_rows - 1):
        item = '<tr>\n'
        for col in range(n_cols):
            item += f'<td>{table_data[row][col]}</td>\n'
        item += '</tr>'
        res_string += item

    return res_string


def table(headers, n_rows, n_cols, table_data):
    style = "<style> table, th, td { border:1px solid black; } </style>\n"
    T = style + '<table style="" class="table-style" id ="">\n'
    H = generate_header(headers)
    R = generate_rows(n_rows, n_cols, table_data)
    T += H
    T += R
    T += '\n</table>\n'
    return T


def main():
    table_data = lambda n_cols, n_rows: [
        [f'row{row+1}-col{col+1}' for col in range(n_cols)] for row in range(n_rows)]
    html_table = table(['h1', 'h2', 'h3'], 3, 3, table_data(3, 2))
    with open('tables.html', 'w+') as writer:
        writer.write(html_table)


if __name__ == '__main__':
    main()
