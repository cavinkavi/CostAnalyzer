# azure_instance_specs.py

# This module defines the instance specifications for Azure instances.
azure_specs = {
    "B1s":     {"cpu": 1, "ram_gb": 1,  "gpu": False},
    "D2s v3":  {"cpu": 2, "ram_gb": 8,  "gpu": False},
    "NC6":     {"cpu": 6, "ram_gb": 56, "gpu": True}
}