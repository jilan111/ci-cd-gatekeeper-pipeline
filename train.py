#!/usr/bin/env python3
"""
Sample ML training script for the CI/CD pipeline.
This demonstrates a real training workflow.
"""

import sys
import random
import json
from datetime import datetime


def train_model():
    """Simulates GPU-accelerated model training."""
    
    print("=" * 60)
    print("Starting ML Model Training")
    print("=" * 60)
    print(f"Timestamp: {datetime.now().isoformat()}")
    
    # Simulate training phases
    phases = [
        "Loading training data...",
        "Initializing model architecture...",
        "Setting up GPU acceleration...",
        "Starting training loop (Epoch 1/100)...",
        "Training phase progress: 25%...",
        "Training phase progress: 50%...",
        "Training phase progress: 75%...",
        "Training phase progress: 100%...",
        "Computing validation metrics...",
    ]
    
    for phase in phases:
        print(f"  ✓ {phase}")
    
    # Simulate random failure (30% chance) for demonstration
    if random.random() < 0.3:
        print("\n" + "=" * 60)
        print("ERROR: Training phase encountered an exception")
        print("=" * 60)
        raise RuntimeError(
            "Out of memory error during training. "
            "Consider reducing batch size or model complexity."
        )
    
    # Log results
    metrics = {
        "timestamp": datetime.now().isoformat(),
        "accuracy": round(random.uniform(0.85, 0.95), 4),
        "loss": round(random.uniform(0.1, 0.3), 4),
        "epochs_trained": 100,
        "batch_size": 32,
        "learning_rate": 0.001,
    }
    
    print("\n" + "=" * 60)
    print("Training Completed Successfully")
    print("=" * 60)
    print(json.dumps(metrics, indent=2))
    
    return metrics


if __name__ == "__main__":
    try:
        metrics = train_model()
        print("\n✓ Model saved successfully")
        sys.exit(0)
    except Exception as e:
        print(f"\n✗ Training failed: {str(e)}")
        sys.exit(1)
