import imdlib as imd
import matplotlib.pyplot as plt

variable = 'rain'
start_year = 2020
end_year = 2023
file_format = 'yearwise'
file_path = 'data'
output_file_name = 'data/rain/output_'

def convert_to_csv(variable, start_year, end_year, file_format, file_path, output_file_name):
    for i in range(start_year, end_year):
        data = imd.open_data(variable, i, i + 1, file_format, file_path)
        xarray_data = data.get_xarray()
        xarray_data = xarray_data.where(xarray_data != -999.)
        xarray_data[variable].mean('time').plot()
        plt.savefig(output_file_name + str(i) + '.png')
        plt.clf()
        data.to_csv(output_file_name + str(i) + '.csv')

if __name__ == '__main__':
    convert_to_csv(variable, start_year, end_year, file_format, file_path, output_file_name)

