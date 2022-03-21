

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
    T = '<table style="" class="" id ="">\n'
    H = generate_header(headers)
    R = generate_rows(n_rows, n_cols, table_data)
    T += H
    T += R
    T += '\n</table>\n'
    print(T)


def main():
    table_data = lambda n_cols, n_rows: [
        [f'row{row+1}-col{col+1}' for col in range(n_cols)] for row in range(n_rows)]
    td = table_data(3, 2)
    table(['h1', 'h2', 'h3'], 3, 3, td)


if __name__ == '__main__':
    main()
