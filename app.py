import streamlit as st
from workload_profiles import workload_profiles

st.set_page_config(page_title="CostAnalyzer-as-a-Service")

st.title("CostAnalyzer-as-a-Service")
st.subheader("Cloud Resource Estimator")
st.write("Select a workload to view its estimated resource usage.")

# dropdown for workload selection
selected_workload = st.selectbox(
    "Choose a workload",
    list(workload_profiles.keys())
)

# Get the selected workload profile
profile = workload_profiles[selected_workload]

# Display the workload profile details
st.markdown("### Workload Description")
st.write(profile["description"])

st.markdown("### Estimated Resource Reqirements")
st.write(f"**vCPUs:** {profile['cpu']}")
st.write(f"**RAM:** {profile['ram_gb']} GB")
st.write(f"**GPU Required:** {'Yes' if profile['gpu'] else 'No'}")
st.write(f"**Estimated Duration:** {profile['duration_min']} minutes")
