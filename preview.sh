#!/bin/bash

# Preview script for The Big Book of Agent Ops
set -e

echo "👀 Starting live preview..."

# Check if Quarto is installed
if ! command -v quarto &> /dev/null; then
    echo "❌ Quarto CLI not found. Please install Quarto first:"
    echo "   Visit: https://quarto.org/docs/get-started/"
    exit 1
fi

# Install dependencies if needed
if [[ -f "requirements.txt" ]] && [[ "$VIRTUAL_ENV" != "" ]]; then
    echo "📦 Installing Python dependencies..."
    pip install -r requirements.txt > /dev/null 2>&1
fi

echo "🌐 Starting preview server..."
echo "📖 Book will open in your browser at http://localhost:4200"
echo "🔄 Changes will auto-reload. Press Ctrl+C to stop."

quarto preview