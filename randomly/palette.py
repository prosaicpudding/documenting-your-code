import matplotlib.pyplot as plt
from matplotlib.figure import Figure
import requests

def plot_palette(model: str) -> Figure:
    """
        Gives us a matplot lib figure from colormind.io
        parameters: 
            Model (str): which model to use, see http://colormind.io/api/ for options

        returns: 
            Figure: The firgure returned by the api
    """
    if model not in {"default", "ui"}:
        raise ValueError(f"{model} is not supported.")

    data = f'{{"model": "{model}"}}'

    # Documentation on the colormind api http://colormind.io/api-access/
    response = requests.post("http://colormind.io/api/", data=data)
    palette = response.json()

    fig, axs = plt.subplots(figsize=(10, 2), nrows=1, ncols=5)

    for idx, color in enumerate(palette["result"]):
        # converts bits to 0-1 scalar
        color_decimal = [val / 256 for val in color]
        axs[idx].set_facecolor(color_decimal)

        axs[idx].set_title(color)
        axs[idx].set_xticks([])
        axs[idx].set_yticks([])

    return fig
