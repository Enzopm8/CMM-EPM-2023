#------------------------------------------------------------------------------
#                                   MAIN CODE
import matplotlib.pyplot as plt
import numpy as np

def create_plot(x, y, plot_type='scatter', title='', xlabel='', ylabel='', legend=None, save_path=None,
                units=('',''), grid=False, axis_linewidth=1, subplot=None, style='seaborn', zoom=None, **kwargs):
    try:
        # Input validation
        if len(x) != len(y):
            raise ValueError("Input data (x, y) must have the same length.")

        # Set plot style
        plt.style.use(style)

        # Create a new figure with subplots if specified
        if subplot:
            if isinstance(subplot, tuple) and len(subplot) == 2:
                plt.subplots(subplot[0], subplot[1])
            else:
                raise ValueError("Invalid subplot parameters. Use a tuple (rows, columns).")

        # Plot based on the specified plot type
        if plot_type == 'scatter':
            plt.scatter(x, y, label=legend, **kwargs)
        elif plot_type == 'line':
            plt.plot(x, y, label=legend, **kwargs)
        else:
            raise ValueError(f"Invalid plot_type: {plot_type}")

        # Set plot title and labels
        plt.title(title)
        plt.xlabel(f"{xlabel} ({units[0]})")
        plt.ylabel(f"{ylabel} ({units[1]})")

        # Add legend if provided
        if legend:
            if isinstance(legend, list):
                plt.legend(legend)
            else:
                plt.legend()

        # Customize grid and axes
        plt.grid(grid)
        plt.gca().spines['left'].set_linewidth(axis_linewidth)
        plt.gca().spines['bottom'].set_linewidth(axis_linewidth)
        plt.gca().spines['right'].set_linewidth(axis_linewidth)
        plt.gca().spines['top'].set_linewidth(axis_linewidth)

        # Zoom in if specified
        if zoom:
            plt.xlim(zoom[0])
            plt.ylim(zoom[1])

        # Save the plot if save_path is provided
        if save_path:
            plt.savefig(save_path)

        # Show the plot
        plt.show()

    except Exception as e:
        print(f"Error: {str(e)}")

#------------------------------------------------------------------------------
#                               DATA TO SPECIFY
# Example using data arrays
x_data = [1, 2, 3, 4, 5]
y_data = [2, 4, 1, 7, 3]



#  Example using function and filled arrays
def example_function(x):
    return np.sin(x)

# Generate x values within a specified range and a specified n of points
x_values = np.linspace(0, 2 * np.pi, 100)

# Generate y values by applying the function to x values
y_values = example_function(x_values)


#------------------------------------------------------------------------------
#                                   CALLING THE FUNCTION

# Create a plot for the function
create_plot(x_values, y_values, plot_type='line', title='Example Function Plot', xlabel='X-axis', ylabel='Y-axis',
            legend=['Function'], units=('rad', ''), grid=True, axis_linewidth=2, style='ggplot', color='blue')

# Create a scatter plot with enhanced customization options
create_plot(x_data, y_data, plot_type='scatter', title='Sample Scatter Plot', xlabel='X-axis', ylabel='Y-axis',
            legend=['Data Points'], units=('m', 'm/s'), grid=True, axis_linewidth=2, style='ggplot', s=100, color='red')

# Save the plot to a file, replace the save path with a 'text.png' 
create_plot(x_data, y_data, plot_type='scatter', title='Sample Scatter Plot', xlabel='X-axis', ylabel='Y-axis',
            legend=['Data Points'], units=('m', 'm/s'), grid=True, axis_linewidth=2, style='ggplot', s=100, color='red',
            save_path= False)

# Create a plot for the function with zoom
create_plot(x_values, y_values, plot_type='line', title='Example Function Plot with Zoom', xlabel='X-axis', ylabel='Y-axis',
            legend=['Function'], units=('rad', ''), grid=True, axis_linewidth=2, style='ggplot', color='blue',
            zoom=((1, 5), (-0.5, 0.5)))
