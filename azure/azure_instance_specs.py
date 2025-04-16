# azure_instance_specs.py

# This module defines the instance specifications for Azure instances.
azure_specs = [
    {"name": "B1s", "cpu": 1, "ram_gb": 1, "gpu": False},
    {"name": "B2ms", "cpu": 2, "ram_gb": 8, "gpu": False},
    {"name": "D2s v3", "cpu": 2, "ram_gb": 8, "gpu": False},
    {"name": "D4s v3", "cpu": 4, "ram_gb": 16, "gpu": False},
    {"name": "F4s v2", "cpu": 4, "ram_gb": 8, "gpu": False},
    {"name": "E8s v3", "cpu": 8, "ram_gb": 64, "gpu": False},
    {"name": "NC6", "cpu": 6, "ram_gb": 56, "gpu": True},
    {"name": "NC6s v3", "cpu": 6, "ram_gb": 112, "gpu": True}
]