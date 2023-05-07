import streamlit as st

def calculate_car_emissions(distance, num_days):
    # Average CO2 emissions per km for a car
    CO2_PER_KM = 0.1808
    # Average distance driven per day for a car
    AVG_DISTANCE_PER_DAY = 40.0

    # Calculate the total distance driven per week
    total_distance = distance * num_days

    # Calculate the carbon emissions for the total distance driven per week
    carbon_emissions = (total_distance / AVG_DISTANCE_PER_DAY) * CO2_PER_KM

    return carbon_emissions


def calculate_motorcycle_emissions(distance, num_days):
    # Average CO2 emissions per km for a motorcycle
    CO2_PER_KM = 0.129

    # Calculate the total distance driven per week
    total_distance = distance * num_days

    # Calculate the carbon emissions for the total distance driven per week
    carbon_emissions = total_distance * CO2_PER_KM

    return carbon_emissions


def calculate_public_trans_emissions(distance, num_days):
    # Average CO2 emissions per km for public transportation
    CO2_PER_KM = 0.09

    # Calculate the total distance traveled per week
    total_distance = distance * num_days

    # Calculate the carbon emissions for the total distance traveled per week
    carbon_emissions = total_distance * CO2_PER_KM

    return carbon_emissions


def calculate_bicycle_emissions(distance, num_days):
    # Carbon emissions for a bicycle are negligible
    return 0.0


def calculate_walking_emissions(distance, num_days):
    # Carbon emissions for walking are negligible
    return 0.0


# Set up the app title and description
st.title('GoEco')
st.write('Welcome to our app that helps you calculate your carbon footprint from your daily commute and provides recommendations for more sustainable transportation options.')

# Create input fields for user to enter commute details
st.header('Enter your commute details:')
distance = st.number_input('Distance (in km):', min_value=0.0, max_value=500.0, step=0.1)
num_days = st.number_input('Number of days per week:', min_value=1, max_value=7, step=1)
vehicle_type = st.selectbox('Vehicle type:', ['Car', 'Motorcycle', 'Public transportation', 'Bicycle', 'Walking'])

# Calculate the carbon footprint based on user input
if vehicle_type == 'Car':
    carbon_emissions = calculate_car_emissions(distance, num_days)
elif vehicle_type == 'Motorcycle':
    carbon_emissions = calculate_motorcycle_emissions(distance, num_days)
elif vehicle_type == 'Public transportation':
    carbon_emissions = calculate_public_trans_emissions(distance, num_days)
elif vehicle_type == 'Bicycle':
    carbon_emissions = calculate_bicycle_emissions(distance, num_days)
else:
    carbon_emissions = calculate_walking_emissions(distance, num_days)

# Display the carbon footprint to the user
st.header('Results:')
st.write(f'Your daily commute generates {carbon_emissions:.2f} kg of CO2 emissions.')

# Provide recommendations for more sustainable transportation options
st.header('Sustainable transportation recommendations:')
if carbon_emissions > 0:
    st.write('Consider the following more sustainable transportation options:')
    if vehicle_type == 'Car' or vehicle_type == 'Motorcycle':
        st.write('- Use public transportation or carpooling when possible')
        st.write('- Switch to an electric vehicle')
    else:
        st.write('- Keep up the good work!')

# Add a footer with the data source and credits
st.write('')
st.write('')
st.write('*Data sources: EPA Greenhouse Gas Equivalencies Calculator and National Public Transportation CO2 Emissions Calculator')
st.write('This app was built by Yash Thapliyal 2023')
