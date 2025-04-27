
import pandas as pd
import plotly.express as px

# load data
df = pd.read_csv("Results_21Mar2022.csv")

# group
df_agg = df.groupby(['diet_group', 'sex'], as_index=False).agg({
    'mean_ghgs': 'mean',
    'mean_watscar': 'mean'
})

# generate treemap
fig = px.treemap(
    df_agg,
    path=['diet_group', 'sex'],
    values='mean_ghgs',
    color='mean_watscar',
    color_continuous_scale='Blues',
    title='Environmental impact analysis of diet groups versus gender',
    labels={'mean_ghgs': 'Greenhouse gas emissions (kg CO2eq)', 'mean_watscar': 'Water scarce (m³)'}
)

# layout
fig.update_layout(margin=dict(t=50, l=25, r=25, b=25))
fig.show()