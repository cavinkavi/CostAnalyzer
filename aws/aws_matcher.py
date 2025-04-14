from aws.aws_api import fetch_aws_prices

def recommend_aws_instances(workload):
    aws_instances = fetch_aws_prices()
    recommendations = []

    for inst in aws_instances:
        if (
            inst["vcpu"] >= workload["cpu"] and
            inst["ram_gb"] >= workload["ram_gb"] and
            inst["gpu"] == workload["gpu"]
        ):
            recommendations.append(inst)

    return sorted(recommendations, key=lambda x: x["price_per_hour"])[:5]  # Return top 5 cheapest instances