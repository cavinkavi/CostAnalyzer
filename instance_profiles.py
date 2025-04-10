# This mnodule defines the instance profiles for different types of workloads.

instance_profiles = [
    # AWS Instances
    {
        "provider": "AWS",
        "name": "t3.micro",
        "cpu": 2,
        "ram_gb": 1,
        "gpu": False,
        "price_per_hour": 0.0104
    },
    {
        "provider": "AWS",
        "name": "g4dn.xlarge",
        "cpu": 4,
        "ram_gb": 16,
        "gpu": True,
        "price_per_hour": 0.526
    },

    # GCP Instances
    {
        "provider": "GCP",
        "name": "e2-medium",
        "cpu": 2,
        "ram_gb": 4,
        "gpu": False,
        "price_per_hour": 0.021
    },
    {
        "provider": "GCP",
        "name": "n1-standard-8 + T4",
        "cpu": 8,
        "ram_gb": 30,
        "gpu": True,
        "price_per_hour": 0.615
    },
]