#!/bin/bash

# ----------------------------
# Streamlit Deployment Setup
# ----------------------------

echo "🚀 Starting setup for Streamlit deployment..."

# 1. Ensure Python version is 3.10
PYTHON_VERSION=$(python3 -c "import sys; print(f'{sys.version_info.major}.{sys.version_info.minor}')")
if [ "$PYTHON_VERSION" != "3.10" ]; then
    echo "⚠️ Warning: Python 3.10 recommended. Current version: $PYTHON_VERSION"
fi

# 2. Install distutils (Linux only)
if ! python3 -c "import distutils" &> /dev/null; then
    echo "🛠 Installing distutils..."
    sudo apt-get update
    sudo apt-get install -y python3.10-distutils
fi

# 3. Upgrade pip, setuptools, wheel, Cython
echo "🔧 Upgrading pip, setuptools, wheel, cython..."
python3 -m pip install --upgrade pip setuptools wheel cython numpy

# 4. Install requirements
if [ -f requirements.txt ]; then
    echo "📦 Installing requirements.txt..."
    pip install -r requirements.txt
else
    echo "⚠️ requirements.txt not found!"
fi

echo "✅ Setup completed successfully!"
