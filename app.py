import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import requests

# API function to get carbon emissions
def get_carbon_emissions(distance, mode):
    url = 'https://www.carboninterface.com/api/v1/estimates'
    headers = {'Authorization': 'Bearer SKrsfaLPFAhVv3yz6e2IIg'}
    payload = {
        'type': 'car',
        'distance_unit': 'kilometers',
        'distance_value': distance
    }

    if mode == 'Car':
        payload['type'] = 'car'
    elif mode == 'Motorcycle':
        payload['type'] = 'motorcycle'
    elif mode == 'Public transportation':
        payload['type'] = 'bus'

    response = requests.post(url, headers=headers, json=payload)
    data = response.json()

    if 'data' in data:
        carbon_emissions = data['data']['attributes']['carbon_kg']
        return carbon_emissions
    else:
        return None

# Set up the app title and description
st.title('GoEco')
st.write('Welcome to our app that helps you calculate your carbon footprint from your daily commute and provides recommendations for more sustainable transportation options.')

# Create input fields for users to enter commute details
st.header('Enter your commute details:')
data = []
transportation_modes = ['Car', 'Motorcycle', 'Public transportation', 'Bicycle', 'Walking']
total_emissions = 0

for mode in transportation_modes:
    st.subheader(f'{mode} Commute Details:')
    distance = st.number_input(f'Distance (in km) for {mode}:', min_value=0.0, max_value=500.0, step=0.1, key=f'{mode}_distance')
    num_days = st.number_input(f'Number of days per week for {mode}:', min_value=1, max_value=7, step=1, key=f'{mode}_days')

    carbon_emissions = get_carbon_emissions(distance, mode)

    if carbon_emissions is not None:
        total_emissions += carbon_emissions
        data.append({'Transportation Mode': mode, 'CO2 Emissions (kg)': carbon_emissions})
    else:
        st.write(f'Error retrieving carbon emissions for {mode}')

# Display the total carbon emissions
df = pd.DataFrame(data)
st.header('Results:')
st.write(f'Your total carbon emissions: {total_emissions:.2f} kg of CO2')

# Create a chart to show CO2 emissions by transportation mode
if not df.empty:
    fig, ax = plt.subplots()
    ax.bar(df['Transportation Mode'], df['CO2 Emissions (kg)'])
    ax.set_xlabel('Transportation Mode')
    ax.set_ylabel('CO2 Emissions (kg)')
    ax.set_title('CO2 Emissions by Transportation Mode')

    # Rotate x-axis labels for better readability
    plt.xticks(rotation=45)

    # Display the chart
    st.pyplot(fig)
else:
    st.write('Carbon emissions data is not available.')

# Provide recommendations for more sustainable transportation options
st.header('Sustainable transportation recommendations:')
if total_emissions > 0:
    st.write('Consider the following more sustainable transportation options:')
    if 'Car' in df['Transportation Mode'].values or 'Motorcycle' in df['Transportation Mode'].values:
        st.write('- Use public transportation or carpooling when possible')
        st.write('- Switch to an electric vehicle')
    else:
        st.write('- Keep up the good work!')
else:
    st.write('Your carbon emissions are negligible. Keep up the good work!')

# Add a footer with the data source and credits
st.write('')
st.write('')
st.write('*Data sources: EPA Greenhouse Gas Equivalencies Calculator and National Public Transportation CO2 Emissions Calculator')
st.write('This app was built by Yash Thapliyal and Laxya Kumar 2023')
