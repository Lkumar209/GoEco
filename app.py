import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

def calculate_car_emissions(distance, num_days):
    # Average CO2 emissions per km for a car
    CO2_PER_KM = 0.1808
    # Average distance driven per day for a car
    AVG_DISTANCE_PER_DAY = 40.0

    # Calculate the total distance driven
    total_distance = distance * num_days

    # Calculate the carbon emissions
    carbon_emissions = (total_distance / AVG_DISTANCE_PER_DAY) * CO2_PER_KM

    return carbon_emissions


def calculate_motorcycle_emissions(distance, num_days):
    # Average CO2 emissions per km for a motorcycle
    CO2_PER_KM = 0.129

    # Calculate the total distance driven
    total_distance = distance * num_days

    # Calculate the carbon emissions
    carbon_emissions = total_distance * CO2_PER_KM

    return carbon_emissions


def calculate_public_trans_emissions(distance, num_days):
    # Average CO2 emissions per km for public transportation
    CO2_PER_KM = 0.09

    # Calculate the total distance traveled
    total_distance = distance * num_days

    # Calculate the carbon emissions
    carbon_emissions = total_distance * CO2_PER_KM

    return carbon_emissions



# Set up the app title and description
st.title(':green[GoEco]')
st.write('Welcome to our app that helps you calculate your carbon footprint from your daily commute and provides recommendations for more sustainable transportation options.')

# Create input fields for users to enter commute details
st.header(':green[Enter your commute details:]')
data = []
transportation_modes = ['Car', 'Motorcycle', 'Public transportation']
total_emissions = 0

for mode in transportation_modes:
    st.subheader(f'{mode} Commute Details:')
    distance = st.number_input(f'Distance (in km) for {mode}:', min_value=0.0, max_value=500.0, step=0.1, key=f'{mode}_distance')
    num_days = st.number_input(f'Number of days per week for {mode}:', min_value=1, max_value=7, step=1, key=f'{mode}_days')

    if mode == 'Car':
        carbon_emissions = calculate_car_emissions(distance, num_days)
    elif mode == 'Motorcycle':
        carbon_emissions = calculate_motorcycle_emissions(distance, num_days)
    elif mode == 'Public transportation':
        carbon_emissions = calculate_public_trans_emissions(distance, num_days)
   

    total_emissions += carbon_emissions
    data.append({'Transportation Mode': mode, 'CO2 Emissions (kg)': carbon_emissions})

# Display the total carbon emissions
df = pd.DataFrame(data)
st.header('Results:')

if total_emissions > 10:
    st.title(f'Net :red[carbon] :red[emissions]: :red[{total_emissions:.2f}] kg of CO2')
else:
    st.title(f'Net :green[carbon] :green[emissions]: :green[{total_emissions:.2f}] kg of CO2')




# Find the maximum emissions value
max_emissions = max(data, key=lambda x: x['CO2 Emissions (kg)'])['CO2 Emissions (kg)']

# Create a chart to show CO2 emissions by transportation mode
fig, ax = plt.subplots()
ax.bar(df['Transportation Mode'], df['CO2 Emissions (kg)'])
ax.set_xlabel('Transportation Mode')
ax.set_ylabel('CO2 Emissions (kg)')
ax.set_title('CO2 Emissions by Transportation Mode')

# Rotate x-axis labels for better readability
plt.xticks(rotation=45)

# Set y-axis limits to include the maximum emissions value
ax.set_ylim(0, max_emissions * 1.2)  # Adjust the multiplier (1.2) as needed for spacing

# Display the chart
st.pyplot(fig)


 
st.header('Sustainable transportation recommendations:')
if total_emissions > 0:
    st.write('Consider the following more sustainable transportation options:')
    if 'Car' in total_emissions or 'Motorcycle' in total_emissions:
        st.write('- Use public transportation or carpooling when possible')
        st.write('- Switch to an electric vehicle')
    else:
        st.write('- Keep up the good work!')
else:
    st.write('Your carbon emissions are negligible. Keep up the good work!')

# Add a footer with the data source and credits
st.write('')

st.write('This app was built by Yash Thapliyal and Laxya Kumar 2023')

 
