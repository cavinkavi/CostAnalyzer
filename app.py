import streamlit as st
from workload_profiles import workload_profiles
from instance_profiles import instance_profiles

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
st.markdown("---")

st.markdown("### Recommended Cloud Instances")

# Get resource requirements from profile
required_cpu = profile['cpu']
required_ram = profile['ram_gb']
needs_gpu = profile['gpu']


# Filter matching instances
matching_instances = []
for instance in instance_profiles:
    if (instance['cpu'] >= required_cpu and
        instance['ram_gb'] >= required_ram and
        (needs_gpu == instance['gpu'])
    ):
        matching_instances.append(instance)

# Sort by price
matching_instances.sort(key=lambda x: x['price_per_hour'])

# Display matches
if matching_instances:
    for inst in matching_instances:
        st.write(f"**{inst['provider']} - {inst['name']}**")
        st.write(f"- vCPUs: {inst['cpu']}")
        st.write(f"- RAM: {inst['ram_gb']} GB")
        st.write(f"- GPU: {'Yes' if inst['gpu'] else 'No'}")
        st.write(f"- Price: ${inst['price_per_hour']} /hour")
        st.markdown("---")

else:
    st.warning("No matching instances found for the selected workload.")

