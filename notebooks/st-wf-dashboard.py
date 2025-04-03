
import streamlit as st
import pandas as pd
import numpy as np
import time # <- We'll need this later as well

from wf_script import Population


st.title('Simple Wright-Fisher Simulation of Genetic Drift')

# Create a new Population
# As a reminder these are the default values for population size (N)
# and initial derived allele frequency (f).
#   N=10, f=0.2
p = Population()

# Initialize the chart with the initial allele frequency of the derived
# allele. `line_chart` expects a list, so we must wrap `p.f` in square
# brackets to pass a list
progress_bar = st.sidebar.progress(0)
status_text = st.sidebar.empty()
chart = st.line_chart([p.f])

#Sidebar
N = st.sidebar.number_input('Population Size (N)', min_value=1, value=10)
f = st.sidebar.slider('Initial Derived Allele Frequency (f)', min_value=0.0, max_value=1.0, value=0.2)
ngens = st.sidebar.slider('Number of Generations', min_value=1, max_value =100, value=25)


# Initially we'll run a loop 50 times
for i in range(ngens):
    # Step 1 wf generation
    p.step(ngens=1)
    # Calculate the current derived allele frequency
    freq = np.sum(p.pop)/len(p.pop)
    # Update the chart to add the current allele frequency
    chart.add_rows([freq])
    status_text.text(f"Generation {i + 1}: State - {p.state}")
    progress_bar.progress(i)


    if p.state == "extinct":
       st.write("The allele has gone extinct. Simulation ended.")
       break
    elif p.state == "fixed":
       st.write("The allele is fixed in the population. Simulation stopped.")
       break

    elif p.state != ["fixed", "extinct"]:
    	st.sidebar.info("Simulation completed without fixation or extinction.")

    # sleep for a small amount of time so you can watch the animation
    time.sleep(0.05)



progress_bar.empty()

# Add a button to rerun the simulation
st.button("Rerun")

##