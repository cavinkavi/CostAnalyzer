import streamlit as st
from aws.aws_matcher import recommend_aws_instances
from workload_profiles import workload_profiles
from azure.azure_matcher import recommend_azure_instances

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
# required_cpu = profile['cpu']
# required_ram = profile['ram_gb']
# needs_gpu = profile['gpu']

# Display Azure instance recommendations
st.markdown("### Azure")
azure_matches = recommend_azure_instances(profile)

if not azure_matches:
    st.info("No matching Azure instances found.")
else:
    for inst in azure_matches:
        st.markdown(f"**Azure - {inst['name']}**")
        st.markdown(f"- vCPUs: {inst['cpu']}")
        st.markdown(f"- RAM: {inst['ram_gb']} GB")
        st.markdown(f"- GPU: {'Yes' if inst['gpu'] else 'No'}")
        st.markdown(f"- Price: ${inst['price']} /hour")
        st.markdown("---")

# Display AWS instance recommendations
st.markdown("### AWS")
st.caption("Showing top 5 AWS matches by price.")
aws_matches = recommend_aws_instances(profile)

if not aws_matches:
    st.info("No matching AWS instances found.")
else:
    for inst in aws_matches:
        st.markdown(f"**AWS - {inst['name']}**")
        st.markdown(f"- vCPUs: {inst['vcpu']}")
        st.markdown(f"- RAM: {inst['ram_gb']} GB")
        st.markdown(f"- GPU: {'Yes' if inst['gpu'] else 'No'}")
        st.markdown(f"- Price: ${inst['price_per_hour']} /hour")
        st.markdown("---")
