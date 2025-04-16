from azure.azure_instance_specs import azure_specs
from azure.azure_api import fetch_azure_prices

def recommend_azure_instances(workload):
    vm_names = [spec["name"] for spec in azure_specs]
    azure_prices = fetch_azure_prices(vm_names=vm_names)
    recommendations = []

    for specs in azure_specs:
        name = specs["name"]
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

    return sorted(recommendations, key=lambda x: x["price"])[:5]  # Return top 5 cheapest instances