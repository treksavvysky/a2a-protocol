#!/bin/bash
# A2A Protocol Development Environment Activation Script

# Colors for output
GREEN='\033[0;32m'
BLUE='\033[0;34m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

echo -e "${BLUE}🚀 Activating A2A Protocol Development Environment${NC}"
echo -e "${BLUE}===============================================${NC}"

# Change to project directory
cd /Users/georgeloudon/Projects/Claude/IntelliSwarm/a2a-protocol

# Activate virtual environment
source venv/bin/activate

# Display information
echo -e "${GREEN}✅ Virtual environment activated${NC}"
echo -e "${YELLOW}📍 Project directory: $(pwd)${NC}"
echo -e "${YELLOW}🐍 Python version: $(python --version)${NC}"
echo -e "${YELLOW}📦 Pip version: $(pip --version)${NC}"

echo ""
echo -e "${BLUE}🔧 Available commands:${NC}"
echo "  • python client_server.py      # Start the A2A server"
echo "  • python test_setup.py         # Test the setup"
echo "  • python test_client.py        # Run client tests"
echo "  • alembic revision --autogenerate -m \"description\"  # Create migration"
echo "  • alembic upgrade head          # Apply migrations"

echo ""
echo -e "${GREEN}🎯 Ready for development on branch: $(git branch --show-current)${NC}"

# Start an interactive shell with the environment activated
exec $SHELL
