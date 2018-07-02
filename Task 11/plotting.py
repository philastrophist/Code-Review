import matplotlib.pyplot as plt
from scipy.stats import ks_2samp
import numpy as np


def plot_distributions(column_name, tables, table_names, colors, ax=None, **hist_kwargs):
    if ax is None:
        fig, ax = plt.subplots()
    bins = hist_kwargs.get('bins', 100)
    for name, table, color in zip(table_names, tables, colors):
        _, bins, _ = ax.hist(table[column_name], bins=bins, color=color, alpha=0.5, label=name, **hist_kwargs)
    plt.legend()
    plt.title(ks_2samp(tables[0][column_name], tables[1][column_name]))
    return ax


def plot_pdf(ax, pdf, cumulative=False,  **kwargs):
    if ax is None:
        fig, ax = plt.subplots()
    else:
        ax = ax.twinx()
    _x = np.linspace(*ax.get_xlim(), num=1000)
    _y = pdf(_x)
    if cumulative:
        _y = np.cumsum()
        _y /= _y.max()
    ax.plot(_x, _y, **kwargs)
    ax.set_ylim(0, 1)
    plt.setp(ax.yaxis.get_ticklabels(), visible=False)
