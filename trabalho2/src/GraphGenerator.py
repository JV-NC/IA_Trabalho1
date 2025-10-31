from matplotlib import pyplot as plt
from typing import Dict

def generate_bar_chart(data: Dict, title: str, xlabel: str, ylabel: str, filename: str, colors: Dict = None) -> None:
    """Generate and save a bar chart from the provided data."""
    plt.figure(figsize=(10, 6))
    bars = plt.bar(data.keys(), data.values(), color=[colors.get(k, 'blue') for k in data.keys()] if colors else 'blue')
    for bar in bars:
        yval = bar.get_height()
        plt.text(bar.get_x() + bar.get_width()/2.0, yval, f'{yval:.2f}', va='bottom')  # va: vertical alignment

    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.savefig(filename)
    plt.close()

"""
def generate_bar_chart(data: Dict, title: str, xlabel: str, ylabel: str, filename: str, colors: Dict = None):
    
    plt.figure(figsize=(10, 6))
    bars = plt.bar(data.keys(), data.values(), color=[colors.get(k, 'blue') for k in data.keys()] if colors else 'blue')
    
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    
    for bar in bars:
        yval = bar.get_height()
        plt.text(bar.get_x() + bar.get_width()/2.0, yval, f'{yval:.2f}', va='bottom')  # va: vertical alignment
    
    plt.savefig(filename)
    plt.close()
"""