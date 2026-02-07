#!/bin/bash

echo "🚀 Starting Streamlit setup..."

# Check Python version
PYTHON_VERSION=$(python3 -c "import sys; print(f'{sys.version_info.major}.{sys.version_info.minor}')")
if [ "$PYTHON_VERSION" != "3.10" ]; then
    echo "⚠️ Python 3.10 recommended. Current version: $PYTHON_VERSION"
fi

# Install distutils if missing
if ! python3 -c "import distutils" &> /dev/null; then
    echo "🛠 Installing distutils..."
    sudo apt-get update
    sudo apt-get install -y python3.10-distutils
fi

# Upgrade pip, setuptools, wheel, cython, numpy
python3 -m pip install --upgrade pip setuptools wheel cython numpy

# Install requirements
if [ -f requirements.txt ]; then
    echo "📦 Installing requirements.txt..."
    pip install -r requirements.txt
else
    echo "⚠️ requirements.txt not found!"
fi

echo "✅ Setup completed!"
