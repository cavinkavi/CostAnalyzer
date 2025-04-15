import streamlit as st
from aws.aws_matcher import recommend_aws_instances
from workload_profiles import workload_profiles
from azure.azure_matcher import recommend_azure_instances
from openai_api import analyze_workload

st.set_page_config(page_title="CostAnalyzer-as-a-Service")

st.title("CostAnalyzer-as-a-Service")
st.subheader("Cloud Resource Estimator")

# Input mode toggle
mode = st.radio("Choose input method:", ["Describe with AI", "Predefined Workload"], horizontal=True)

profile = None

if mode == "Describe with AI":
    st.markdown("### Describe your custom workload")
    description = st.text_area("Describe your workload (e.g., 'a daily ML job on image data')")

    if st.button("Analyze with AI"):
        with st.spinner("Thinking..."):
            try:
                ai_result = analyze_workload(description)
                profile = ai_result

                st.success("Suggested Requirements:")
                st.write(f"**vCPUs:** {profile['cpu']}")
                st.write(f"**RAM:** {profile['ram_gb']} GB")
                st.write(f"**GPU Needed:** {'Yes' if profile['gpu'] else 'No'}")
                st.write(f"**Estimated Duration:** {profile['duration_min']} minutes")
            except Exception as e:
                st.error(f"Failed to analyze: {e}")

elif mode == "Predefined Workload":
    st.markdown("### Select a Predefined Workload")

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

if profile:
    if mode == "Predefined Workload":
        st.markdown("### Estimated Resource Reqiurements")
        st.write(f"vCPUs: {profile['cpu']}")
        st.write(f"RAM: {profile['ram_gb']} GB")
        st.write(f"GPU Required: {'Yes' if profile['gpu'] else 'No'}")
        st.write(f"Estimated Duration: {profile['duration_min']} minutes")
        st.markdown("---")

    # Input: how often the workload runs per day
    runs_per_day = st.number_input(
        "How many times will this workload run per day?",
        min_value=1, max_value=1000,
        value=10  # default
    )

    st.markdown("### Recommended Cloud Instances")


    # Display Azure instance recommendations
    st.markdown("### Azure")
    azure_matches = recommend_azure_instances(profile)

    if not azure_matches:
        st.info("No matching Azure instances found.")
    else:
        for inst in azure_matches:
            # Calculate monthly cost
            duration_hr = profile["duration_min"] / 60
            cost_per_run = inst["price"] * duration_hr
            monthly_cost = cost_per_run * runs_per_day * 30 # Assuming 30 days in a month

            st.markdown(f"**Azure - {inst['name']}**")
            st.write(f"- vCPUs: {inst['cpu']}")
            st.write(f"- RAM: {inst['ram_gb']} GB")
            st.write(f"- GPU: {'Yes' if inst['gpu'] else 'No'}")
            st.write(f"- Price: ${inst['price']} /hour")
            st.write(f"- Estimated Cost/Run: ${cost_per_run:.4f}")
            st.write(f"- Estimated Monthly Cost: ${monthly_cost:.2f}")
            st.markdown("---")

    # Display AWS instance recommendations
    st.markdown("### AWS")
    st.caption("Showing top 5 AWS matches by price.")
    aws_matches = recommend_aws_instances(profile)

    if not aws_matches:
        st.info("No matching AWS instances found.")
    else:
        for inst in aws_matches:
            # Calculate monthly cost
            duration_hr = profile["duration_min"] / 60
            cost_per_run = inst["price_per_hour"] * duration_hr
            monthly_cost = cost_per_run * runs_per_day * 30 # Assuming 30 days in a month

            st.markdown(f"**AWS - {inst['name']}**")
            st.write(f"- vCPUs: {inst['vcpu']}")
            st.write(f"- RAM: {inst['ram_gb']} GB")
            st.write(f"- GPU: {'Yes' if inst['gpu'] else 'No'}")
            st.write(f"- Price: ${inst['price_per_hour']} /hour")
            st.write(f"- Estimated Cost/Run: ${cost_per_run:.4f}")
            st.write(f"- Estimated Monthly Cost: ${monthly_cost:.2f}")
            st.markdown("---")
