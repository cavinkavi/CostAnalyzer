# This module defines the workload profiles for different types of workloads.

workload_profiles = {
    "Web API - Small": {
        "description": "A lightweight web service handling API calls with minimal compute.",
        "cpu": 1,
        "ram_gb": 0.5,
        "gpu": False,
        "duration_min": 1
    },
    "ML Inference - Medium": {
        "description": "Running inference on models like BERT or sentiment classifiers.",
        "cpu": 2,
        "ram_gb": 4,
        "gpu": True,
        "duration_min": 2
    },
    "ML Training - Large": {
        "description": "Training a mid-sized machine learning model on a dataset.",
        "cpu": 8,
        "ram_gb": 16,
        "gpu": True,
        "duration_min": 30
    },
    "Video Encoding": {
        "description": "Converting or compressing video files, ideally GPU-accelerated.",
        "cpu": 4,
        "ram_gb": 8,
        "gpu": True,
        "duration_min": 10
    },
    "Data Processing - Batch": {
        "description": "Running batch jobs like data aggregation or ETL pipelines.",
        "cpu": 4,
        "ram_gb": 8,
        "gpu": False,
        "duration_min": 20
    },
    "Document Processing - OCR": {
        "description": "Extracting text from images or scanned documents.",
        "cpu": 2,
        "ram_gb": 2,
        "gpu": False,
        "duration_min": 5
    },
    "Image Classification - Lightweight": {
        "description": "Classifying simple images using a small neural net.",
        "cpu": 2,
        "ram_gb": 2,
        "gpu": True,
        "duration_min": 2
    },
    "Large Scale Simulation - Scientific": {
        "description": "Running scientific or engineering simulations that need heavy compute.",
        "cpu": 16,
        "ram_gb": 64,
        "gpu": True,
        "duration_min": 60
    }
}