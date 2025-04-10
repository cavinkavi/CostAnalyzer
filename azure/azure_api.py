# azure_api.py

import requests

def fetch_azure_prices(vm_names=None, region="southeastasia", currency="USD"):
    if vm_names is None:
        vm_names = ["B1s", "D2s v3", "NC6"]

    prices = {}
    base_url = "https://prices.azure.com/api/retail/prices"
    filter_str = f"serviceName eq 'Virtual Machines' and armRegionName eq '{region}' and currencyCode eq '{currency}'"

    url = f"{base_url}?$filter={filter_str}"
    
    while url:
        response = requests.get(url)
        data = response.json()

        for item in data["Items"]:
            sku = item.get("skuName", "")
            price = item.get("unitPrice", None)
            unit = item.get("unitOfMeasure", "")
            meter = item.get("meterName", "")
            type = item.get("type", "")

            for name in vm_names:
                if(
                name.lower() in sku.lower() and 
                "1 Hour" in unit and 
                "spot" not in meter.lower() and 
                "low priority" not in meter.lower() and 
                "windows" not in meter.lower() and
                type.lower() == "consumption"
                ):
                    prices[name] = {
                        "sku": sku,
                        "unit_price": price,
                        "meter_name": meter,
                        "region": region
                    }

        url = data.get("NextPageLink", None)

    return prices
