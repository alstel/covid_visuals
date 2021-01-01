import pandas as pd
import os

"""
Good for use in building facet charts.
File size will increase over wide format.
"""

# read in data
dir = '.'
filename = 'Global_Mobility_Report.zip'
mobility = pd.read_csv(
    os.path.join(dir, filename),
	compression='zip',
    low_memory=False
)

# start with subsets
country_region_code = ['US']
    
for code in country_region_code:    
    
    # create subset
    mobility = mobility.loc[
        mobility.country_region_code == code
    ]

    # simplify column names
    mobility = mobility.rename(columns={
        'retail_and_recreation_percent_change_from_baseline': 'retail_recreation',
        'grocery_and_pharmacy_percent_change_from_baseline': 'grocery_pharmacy',
        'parks_percent_change_from_baseline': 'parks',
        'transit_stations_percent_change_from_baseline': 'transit_stations',
        'workplaces_percent_change_from_baseline': 'workplaces',
        'residential_percent_change_from_baseline': 'residential'
    })

    # shift to long format
    mobility_long = mobility.melt(
        id_vars=[
            'country_region_code',
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
        f'{code}_mobility_long.zip',
        compression='zip',
        index=False
    )