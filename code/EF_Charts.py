
#%%
# REQUEST GUIDELINES:
    # Rest EFs on a vertical column.
    # Stress EFs on a second vertical to the right of the first column.
    # A line should connect rest and stress values for each of 15 study subjects.
    # Display means and standard deviations adjacent to the two vertical columns.
    # Display means and SD for reference population.
    # Depict Heart rate and systolic blood pressure using the same format.
    # It may ultimately be useful to have all 3 plots side-by-side in a single figure.

# BACKGROUND INFO
# Ejection fraction (EF) is a measure of how well the left ventricle of the heart pumps blood.
    # 55% - 75%
    # Normal EF is 55% or higher.
    # EF below 50% is considered low and may be a sign of heart failure.
# Heart rate (HR) is the number of times your heart beats per minute. 
    # 60 - 100 beats per minute
    # Normal heart rate is between 60 and 100 beats per minute.
    # High heart rate can be a sign of stress, anxiety, or exercise.
# Systolic blood pressure (SBP) is the pressure in your arteries when your heart beats.
    # 90 - 120 mmHg
    # Normal SBP is below 120 mmHg.
    # High SBP can signal high blood pressure; risk factor for heart disease and stroke.
    


#%%
## LIBRARY IMPORTS ##

import pandas as pd
import numpy as np

import matplotlib.pyplot as plt
#import seaborn as sns

import plotly as ply
import plotly.express as px
from plotly.subplots import make_subplots
import plotly.graph_objects as go


## DIRECTORY CONFIGURATION ##

## DATA IMPORT ##

## PRE-PROCESSING ##

## IMAGE IMPORT ##

## DESIGN FORMAT ##

## RANDOM SEED
np.random.seed(42)

# GENERATE DUMMY DATA

# Define interval ranges
rest_ef_mean, rest_ef_std = 50, 5
stress_ef_mean, stress_ef_std = 55, 5
rest_hr_mean, rest_hr_std = 70, 5
stress_hr_mean, stress_hr_std = 80, 10
rest_sbp_mean, rest_sbp_std = 120, 10
stress_sbp_mean, stress_sbp_std = 130, 10

# Generate reference population
population_size = 1000
population_subjects = [i for i in range(population_size)]
rest_efs = np.random.normal(rest_ef_mean, rest_ef_std, population_size)
stress_efs = np.random.normal(stress_ef_mean, stress_ef_std, population_size)
rest_heart_rates = np.random.normal(rest_hr_mean, rest_hr_std, population_size)
stress_heart_rates = np.random.normal(stress_hr_mean, stress_hr_std, population_size)
rest_sbps = np.random.normal(rest_sbp_mean, rest_sbp_std, population_size)
stress_sbps = np.random.normal(stress_sbp_mean, stress_sbp_std, population_size)

# Swap values where rest is higher than stress
#rest_efs, stress_efs = np.where(rest_efs > stress_efs, stress_efs, rest_efs), np.where(rest_efs > stress_efs, rest_efs, stress_efs)
rest_heart_rates, stress_heart_rates = np.where(rest_heart_rates > stress_heart_rates, stress_heart_rates, rest_heart_rates), np.where(rest_heart_rates > stress_heart_rates, rest_heart_rates, stress_heart_rates)
rest_sbps, stress_sbps = np.where(rest_sbps > stress_sbps, stress_sbps, rest_sbps), np.where(rest_sbps > stress_sbps, rest_sbps, stress_sbps)

# DataFrame for 15 study subjects
study_subjects = [i for i in range(1,16,1)]
rest_EFs = np.random.normal(50, 10, 15)
stress_EFs = np.random.normal(55, 10, 15)
rest_heart_rate = np.random.normal(70, 10, 15)
stress_heart_rate = np.random.normal(80, 10, 15)
rest_systolic_BP = np.random.normal(120, 10, 15)
stress_systolic_BP = np.random.normal(130, 10, 15)

# Swap values where rest is higher than stress
#rest_EFs, stress_EFs = np.where(rest_EFs > stress_EFs, stress_EFs, rest_EFs), np.where(rest_EFs > stress_EFs, rest_EFs, stress_EFs)
rest_heart_rate, stress_heart_rate = np.where(rest_heart_rate > stress_heart_rate, stress_heart_rate, rest_heart_rate), np.where(rest_heart_rate > stress_heart_rate, rest_heart_rate, stress_heart_rate)
rest_systolic_BP, stress_systolic_BP = np.where(rest_systolic_BP > stress_systolic_BP, stress_systolic_BP, rest_systolic_BP), np.where(rest_systolic_BP > stress_systolic_BP, rest_systolic_BP, stress_systolic_BP)


# DataFrame for reference population
reference_population_df = pd.DataFrame({
    'Subject': population_subjects,
    'Rest EF': rest_efs,
    'Stress EF': stress_efs,
    'Rest Heart Rate': rest_heart_rates,
    'Stress Heart Rate': stress_heart_rates,
    'Rest Systolic BP': rest_sbps,
    'Stress Systolic BP': stress_sbps,
})

# DataFrame for study subjects
study_subjects_df = pd.DataFrame({
    'Subject': study_subjects,
    'Rest EF': rest_EFs,
    'Stress EF': stress_EFs,
    'Rest Heart Rate': rest_heart_rate,
    'Stress Heart Rate': stress_heart_rate,
    'Rest Systolic BP': rest_systolic_BP,
    'Stress Systolic BP': stress_systolic_BP,
})


# INVESTIGATE DATA
# print(study_subjects_df.info())
# print(reference_population_df.info())

# print(study_subjects_df.describe())
# print(reference_population_df.describe())

# Define a colormap
cmap = px.colors.sequential.dense  # a colormap with color gradient

# Create an empty Figure with 3 horizontal subplots
fig = make_subplots(rows=1, cols=3, subplot_titles=('Ejection Fraction (EF)', 'Heart Rate (HR)', 'Systolic Blood Pressure (SBP)'))

# Define a list of variables and their titles
variables = [('Rest EF', 'Stress EF'), ('Rest Heart Rate', 'Stress Heart Rate'), ('Rest Systolic BP', 'Stress Systolic BP')]

# Iterate over the variables
for idx, (rest_var, stress_var) in enumerate(variables, start=1):

    # Plot the rest and stress data for each subject with lower opacity
    for i in range(len(study_subjects_df)):
        fig.add_trace(go.Scatter(x=[rest_var, stress_var], 
                                 y=study_subjects_df.loc[i, [rest_var, stress_var]], 
                                 mode='lines+markers', 
                                 name=f"Subject {study_subjects_df.loc[i, 'Subject']}",
                                 marker=dict(color=cmap[i%len(cmap)]),
                                 line=dict(width=2, color=cmap[i%len(cmap)]), 
                                 opacity=0.6,
                                 showlegend=(idx==1)), # Show legend only for the first subplot
                                 row=1, col=idx)

    # Calculate and display mean and standard deviation
    rest_mean = study_subjects_df[rest_var].mean()
    rest_std = study_subjects_df[rest_var].std()
    stress_mean = study_subjects_df[stress_var].mean()
    stress_std = study_subjects_df[stress_var].std()

    # Plot means and SDs with thicker lines and different markers
    fig.add_trace(go.Scatter(x=[rest_var, stress_var], 
                             y=[rest_mean, stress_mean], 
                             mode='lines+markers', 
                             name="Mean (Subjects)", 
                             line=dict(dash='dash', color='black', width=4),
                             showlegend=(idx==1)), row=1, col=idx)

    fig.add_trace(go.Scatter(x=[rest_var, stress_var], 
                             y=[rest_mean + rest_std, stress_mean + stress_std], 
                             mode='lines+markers', 
                             name="+1 SD (Subjects)", 
                             line=dict(dash='dash', color='black', width=3),
                             showlegend=(idx==1)), row=1, col=idx)

    fig.add_trace(go.Scatter(x=[rest_var, stress_var], 
                             y=[rest_mean - rest_std, stress_mean - stress_std], 
                             mode='lines+markers', 
                             name="-1 SD (Subjects)", 
                             line=dict(dash='dash', color='black', width=3),
                             showlegend=(idx==1)), row=1, col=idx)

    # Calculate population mean and standard deviation
    rest_pop_mean = reference_population_df[rest_var].mean()
    rest_pop_std = reference_population_df[rest_var].std()
    stress_pop_mean = reference_population_df[stress_var].mean()
    stress_pop_std = reference_population_df[stress_var].std()

    # Plot population means and SDs with thicker lines and different markers
    fig.add_trace(go.Scatter(x=[rest_var, stress_var], 
                             y=[rest_pop_mean, stress_pop_mean], 
                             mode='lines+markers', 
                             name="Mean (Reference)", 
                             line=dict(dash='dash', color='green', width=4),
                             showlegend=(idx==1)), row=1, col=idx)

    fig.add_trace(go.Scatter(x=[rest_var, stress_var], 
                             y=[rest_pop_mean + rest_pop_std, stress_pop_mean + stress_pop_std], 
                             mode='lines+markers', 
                             name="+1 SD (Reference)", 
                             line=dict(dash='dash', color='green', width=3),
                             showlegend=(idx==1)), row=1, col=idx)

    fig.add_trace(go.Scatter(x=[rest_var, stress_var], 
                             y=[rest_pop_mean - rest_pop_std, stress_pop_mean - stress_pop_std], 
                             mode='lines+markers', 
                             name="-1 SD (Reference)", 
                             line=dict(dash='dash', color='green', width=3),
                             showlegend=(idx==1)), row=1, col=idx)

# Update layout for white background and gridlines
fig.update_layout(
    title='Rest vs. Stress', 
    autosize=False,
    width=1400, #2400
    height=700, #800
    plot_bgcolor='white',
    xaxis=dict(
        showgrid=True,
        gridcolor='lightgray',
    ),
    yaxis=dict(
        showgrid=True,
        gridcolor='lightgray',
    ),
    xaxis2=dict(
        showgrid=True,
        gridcolor='lightgray',
    ),
    yaxis2=dict(
        showgrid=True,
        gridcolor='lightgray',
    ),
    xaxis3=dict(
        showgrid=True,
        gridcolor='lightgray',
    ),
    yaxis3=dict(
        showgrid=True,
        gridcolor='lightgray',
    ),
)


fig.show()

#%%
# # Plot the rest and stress EF for each subject with lower opacity
# for i in range(len(study_subjects_df)):
#     fig.add_trace(go.Scatter(x=['Rest EF', 'Stress EF'], 
#                              y=study_subjects_df.loc[i, ['Rest EF', 'Stress EF']], 
#                              mode='lines+markers', 
#                              name=f"Subject {study_subjects_df.loc[i, 'Subject']}",
#                              marker=dict(color=cmap[i%len(cmap)]),
#                              line=dict(width=2, color=cmap[i%len(cmap)]), 
#                              opacity=0.6))

# # Calculate and display mean and standard deviation
# rest_ef_mean = study_subjects_df['Rest EF'].mean()
# rest_ef_std = study_subjects_df['Rest EF'].std()
# stress_ef_mean = study_subjects_df['Stress EF'].mean()
# stress_ef_std = study_subjects_df['Stress EF'].std()

# # Plot means and SDs with thicker lines and different markers
# fig.add_trace(go.Scatter(x=['Rest EF', 'Stress EF'], 
#                          y=[rest_ef_mean, stress_ef_mean], 
#                          mode='lines+markers', 
#                          name="Mean (Subjects)", 
#                          line=dict(dash='dash', color='green', width=4)))

# fig.add_trace(go.Scatter(x=['Rest EF', 'Stress EF'], 
#                          y=[rest_ef_mean + rest_ef_std, stress_ef_mean + stress_ef_std], 
#                          mode='lines+markers', 
#                          name="+1 SD (Subjects)", 
#                          line=dict(dash='dash', color='green', width=3)))

# fig.add_trace(go.Scatter(x=['Rest EF', 'Stress EF'], 
#                          y=[rest_ef_mean - rest_ef_std, stress_ef_mean - stress_ef_std], 
#                          mode='lines+markers', 
#                          name="-1 SD (Subjects)", 
#                          line=dict(dash='dash', color='green', width=3)))

# # Calculate population mean and standard deviation
# rest_ef_pop_mean = reference_population_df['Rest EF'].mean()
# rest_ef_pop_std = reference_population_df['Rest EF'].std()
# stress_ef_pop_mean = reference_population_df['Stress EF'].mean()
# stress_ef_pop_std = reference_population_df['Stress EF'].std()

# # Plot population means and SDs with thicker lines and different markers
# fig.add_trace(go.Scatter(x=['Rest EF', 'Stress EF'], 
#                          y=[rest_ef_pop_mean, stress_ef_pop_mean], 
#                          mode='lines+markers', 
#                          name="Mean (Reference)", 
#                          line=dict(dash='dash', color='black', width=4)))

# fig.add_trace(go.Scatter(x=['Rest EF', 'Stress EF'], 
#                          y=[rest_ef_pop_mean + rest_ef_pop_std, stress_ef_pop_mean + stress_ef_pop_std], 
#                          mode='lines+markers', 
#                          name="+1 SD (Reference)", 
#                          line=dict(dash='dash', color='black', width=3)))

# fig.add_trace(go.Scatter(x=['Rest EF', 'Stress EF'], 
#                          y=[rest_ef_pop_mean - rest_ef_pop_std, stress_ef_pop_mean - stress_ef_pop_std], 
#                          mode='lines+markers', 
#                          name="-1 SD (Reference)", 
#                          line=dict(dash='dash', color='black', width=3)))

# # Update layout for white background and gridlines
# fig.update_layout(
#     title='Ejection Fraction (EF) Rest vs. Stress', 
#     yaxis_title='EF Value', 
#     autosize=False,
#     width=1200,
#     height=600,
#     plot_bgcolor='white',
#     xaxis=dict(
#         showgrid=True,
#         gridcolor='lightgray',
#     ),
#     yaxis=dict(
#         showgrid=True,
#         gridcolor='lightgray',
#     ),
# )

# fig.show()



#%%

## FORMAT / STYLE ##

## VISUALIATION LABELS ##

## COLOR SCALES ##

# Tropic = px.colors.diverging.Tropic
# Blackbody = px.colors.sequential.Blackbody
# BlueRed = px.colors.sequential.Bluered

# Sunsetdark = px.colors.sequential.Sunsetdark
# Sunset = px.colors.sequential.Sunset
# Temps = px.colors.diverging.Temps
# Tealrose = px.colors.diverging.Tealrose

# Ice = px.colors.sequential.ice
# Ice_r = px.colors.sequential.ice_r
# Dense = px.colors.sequential.dense
# Deep = px.colors.sequential.deep
# PuOr = px.colors.diverging.PuOr
# Speed = px.colors.sequential.speed
# IceFire = px.colors.diverging.
# YlOrRd = px.colors.sequential.YlOrRd
# Mint = px.colors.sequential.Mint
# Electric = px.colors.sequential.Electric

# pd.options.display.float_format = '${:,.2f}'.format
# pd.set_option('display.max_colwidth', 200)