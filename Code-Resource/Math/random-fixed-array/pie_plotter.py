import matplotlib.pyplot as plt
from matplotlib import figure


def pie_chart(data):
    fig = figure.Figure()
    ax = fig.subplots()
    ax.pie(data)
    fig.tight_layout()
    fig.savefig('plot.pdf', dpi=300, bbox_inches='tight')


def main():
    data = [x for x in range(10)]
    pie_chart(data)


if __name__ == '__main__':
    main()
