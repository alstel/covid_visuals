import pandas as pd
import os

# read in data
dir = '.'
filename = 'Global_Mobility_Report.csv'
mobility_wide = pd.read_csv(
    os.path.join(dir, filename)
)

# simplify column names
mobility_wide = mobility_wide.rename(columns={
    'retail_and_recreation_percent_change_from_baseline': 'retail_recreation',
    'grocery_and_pharmacy_percent_change_from_baseline': 'grocery_pharmacy',
    'parks_percent_change_from_baseline': 'parks',
    'transit_stations_percent_change_from_baseline': 'transit_stations',
    'workplaces_percent_change_from_baseline': 'workplaces',
    'residential_percent_change_from_baseline': 'residential'
})

# shift to long format
mobility_long = mobility_wide.melt(id_vars=[
    'country_region',
    'sub_region_1',
    'sub_region_2',
    'metro_area',
    'census_fips_code',
    'date'
    ], 
    value_vars=[
    'retail_recreation',
    'grocery_pharmacy',
    'parks',
    'transit_stations',
    'workplaces',
    'residential'
    ],
    var_name='activity',
    value_name='percent_change'
)

# write to file
mobility_long.to_csv(
	'global_mobility_long.csv',
	index=False
)