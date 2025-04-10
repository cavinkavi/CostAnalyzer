from azure.azure_instance_specs import azure_specs
from azure.azure_api import fetch_azure_prices

def recommend_azure_instances(workload):
    azure_prices = fetch_azure_prices(vm_names=list(azure_specs.keys()))
    recommendations = []

    for name, specs in azure_specs.items():
        price_info = azure_prices.get(name)
        if not price_info:
            continue  

        # Match specs with workload
        if (
            specs["cpu"] >= workload["cpu"] and
            specs["ram_gb"] >= workload["ram_gb"] and
            specs["gpu"] == workload["gpu"]
        ):
            recommendations.append({
                "provider": "Azure",
                "name": name,
                "cpu": specs["cpu"],
                "ram_gb": specs["ram_gb"],
                "gpu": specs["gpu"],
                "price": price_info["unit_price"]
            })

    return sorted(recommendations, key=lambda x: x["price"])