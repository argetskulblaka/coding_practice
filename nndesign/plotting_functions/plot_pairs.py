import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def plot_pairs(dataframe, figSize):

    # Make square figure canvas
    plt.figure(figsize=(figSize, figSize))

    # Group dataframe by last column-name
    groupingCol = dataframe.columns[-1]
    groupedData = dataframe.groupby(groupingCol)

    # Get the subplot dimensions
    subplotDimension = len(dataframe.columns) - 1

    # Define subplot, histogram and loop counters
    subplotCounter = 1
    subplotRowCounter = 1

    for i in range(subplotDimension):

        for j in range(subplotDimension):

            # Select subplot
            plt.subplot(subplotDimension, subplotDimension, subplotCounter)

            # Conditional check for diagonal
            if ( i == j ):
                for name, group in groupedData:
                    plt.hist(group[group.columns[i]], label = name)
                plt.legend()

            else:
                for name, group in groupedData:
                    plt.plot(group[group.columns[j]], group[group.columns[i]], marker="+", linestyle="", label=name)
                plt.legend()
            
            # Increment sublot counter
            subplotCounter+=1

