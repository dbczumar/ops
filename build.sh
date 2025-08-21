#!/bin/bash

# Build script for The Big Book of Agent Ops
set -e

echo "📚 Building The Big Book of Agent Ops..."

# Check if Quarto is installed
if ! command -v quarto &> /dev/null; then
    echo "❌ Quarto CLI not found. Please install Quarto first:"
    echo "   Visit: https://quarto.org/docs/get-started/"
    exit 1
fi

# Check if Python virtual environment exists
if [[ "$VIRTUAL_ENV" == "" ]] && [[ ! -d "venv" ]]; then
    echo "⚠️  No virtual environment detected. Creating one..."
    python3 -m venv venv
    echo "✅ Virtual environment created. Activate with: source venv/bin/activate"
fi

# Install Python dependencies if requirements.txt exists
if [[ -f "requirements.txt" ]]; then
    echo "📦 Installing Python dependencies..."
    pip install -r requirements.txt
fi

# Clean previous build
if [[ -d "_book" ]]; then
    echo "🧹 Cleaning previous build..."
    rm -rf _book
fi

# Build the book
echo "🔨 Building book..."
quarto render

echo "✅ Build complete! Book available in _book/ directory"
echo "🌐 To view locally: quarto preview"