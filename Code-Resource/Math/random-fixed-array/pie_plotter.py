import matplotlib.pyplot as plt
from matplotlib import figure


def pie_chart(data, plot_name):
    # generate the labels from the data
    _labels = [f'id-{idx+1}' for idx in range(len(data))]
    fig = figure.Figure()
    ax = fig.subplots()

    # create the plot
    ax.pie(data,labels=_labels)

    ax.legend(title="Pie chart")
    fig.tight_layout()
    fig.savefig(f'{plot_name}.pdf', dpi=300, bbox_inches='tight')


def main():
    data = [x for x in range(10)]
    pie_chart(data, 'plot')


if __name__ == '__main__':
    main()
