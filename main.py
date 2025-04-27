import pandas as pd
import plotly.express as px

# Load data
df = pd.read_csv("Results_21Mar2022.csv")

# Aggregate by diet group, sex, and age group
df_agg = df.groupby(['diet_group', 'sex', 'age_group'], as_index=False).agg({
    'mean_ghgs': 'mean',
    'mean_watscar': 'mean'
})

# Generate treemap
fig = px.treemap(
    df_agg,
    path=['diet_group', 'sex', 'age_group'],
    values='mean_ghgs',
    color='mean_watscar',
    color_continuous_scale='Blues',
    title='Environmental Impact by Diet Group, Sex, and Age',
    labels={
        'mean_ghgs': 'Greenhouse Gas Emissions (kg CO2eq)',
        'mean_watscar': 'Water Scarcity Impact (m³)',
        'diet_group': 'Diet Group',
        'sex': 'Sex',
        'age_group': 'Age Group'
    }
)

# layout
fig.update_layout(
    margin=dict(t=50, l=25, r=25, b=25),
    coloraxis_colorbar=dict(title="Water Scarcity (m³)")
)

fig.show()
