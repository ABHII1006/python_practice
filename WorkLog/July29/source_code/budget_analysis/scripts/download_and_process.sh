#!/bin/bash

echo "Activating virtual environment..."

# Explicit path to venv's python
VENV_PYTHON="/home/abhishek/budget_analysis/venv/bin/python"

echo "Running process_data.py..."
$VENV_PYTHON /home/abhishek/budget_analysis/scripts/process_data.py

echo "Running generate_report.py..."
$VENV_PYTHON /home/abhishek/budget_analysis/scripts/generate_report.py

echo "All steps completed!"
