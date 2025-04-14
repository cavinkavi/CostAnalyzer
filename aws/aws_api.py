import requests

def fetch_aws_prices():
    region_name = "Asia Pacific (Singapore)"
    encoded_region = requests.utils.quote(region_name)

    # AWS official EC2 On-Demand Linux pricing for this region
    url = f"https://b0.p.awsstatic.com/pricing/2.0/meteredUnitMaps/ec2/USD/current/ec2-ondemand-without-sec-sel/{encoded_region}/Linux/index.json"

    response = requests.get(url)
    data = response.json()

    # Only one region key in this JSON, extract its contents
    instances = list(data["regions"].values())[0]
    instance_data = []

    for inst in instances.values():
        try:
            instance_data.append({
                "name": inst["Instance Type"],
                "vcpu": int(inst["vCPU"]),
                "ram_gb": float(inst["Memory"].split(" ")[0]),
                "gpu": "gpu" in inst["Instance Type"].lower() or "g4" in inst["Instance Type"].lower(),
                "price_per_hour": float(inst["price"])
            })
        except:
            continue  # skip any malformed entries

    return instance_data
