# Uses Heath Nutrition and Population statistics,
# stored in the file HNP_Data.csv.gz,
# assumed to be located in the working directory.
# Prompts the user for an Indicator Name. If it exists and is associated with
# a numerical value for some countries or categories, for some the years 1960-2015,
# then finds out the maximum value, and outputs:
# - that value;
# - the years when that value was reached, from oldest to more recents years;
# - for each such year, the countries or categories for which that value was reached,
#   listed in lexicographic order.
# 
# Written by *** and Eric Martin for COMP9021


import sys
import os
import csv
import gzip
from collections import defaultdict


filename = 'HNP_Data.csv.gz'
if not os.path.exists(filename):
    print(f'There is no file named {filename} in the working directory, giving up...')
    sys.exit()

# indicator_of_interest = input('Enter an Indicator Name: ')
indicator_of_interest = 'Age at first marriage, female'
first_year = 1960
number_of_years = 56
max_value = None
countries_for_max_value_per_year = defaultdict(list)

with gzip.open(filename) as csvfile:
    file = csv.DictReader(line.decode('utf8').replace('\0', '') for line in csvfile)
    # file = csv.DictReader(csvfile)
    pass
    # REPLACE pass above WITH YOUR CODE
    count = 0
    country_name_field = None
    for name in file.fieldnames:
        if 'Country Name' in name:
            country_name_field = name
    value_list = []
    row_list = []
    for row in file:
        if indicator_of_interest in row['Indicator Name']:
            for i in range(number_of_years):
                if row.get(str(first_year + i)):
                    value_list.append(row.get(str(first_year + i)))

            row_list.append(row)

    if value_list:
        max_value = value_list[0]
        for item in value_list[1:]:
            if float(max_value) < float(item):
                max_value = item

    for row in row_list:
        if indicator_of_interest in row['Indicator Name']:
            for i in range(number_of_years):
                if row.get(str(first_year + i)) == max_value:
                    countries_for_max_value_per_year[str(first_year + i)].append(row[country_name_field])

if max_value is None:
    print('Sorry, either the indicator of interest does not exist or it has no data.')
else:
    print('The maximum value is:', max_value)
    print('It was reached in these years, for these countries or categories:')
    print('\n'.join(f'    {year}: {countries_for_max_value_per_year[year]}'
                                  for year in sorted(countries_for_max_value_per_year)
                   )
         )
