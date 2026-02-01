#!/bin/bash

# This script generates secure secret keys for the application
# Run the commands below to execute this script and paste the output into your .env file
# chmod +x setup_env.sh
# ./setup_env.sh

echo "Generating secure secret keys..."
SECRET_KEY=$(python3 -c "import secrets; print(secrets.token_urlsafe(32))")
JWT_SECRET_KEY=$(python3 -c "import secrets; print(secrets.token_urlsafe(32))")

echo ""
echo "Add these to your .env file:"
echo "================================"
echo "SECRET_KEY=$SECRET_KEY"
echo "JWT_SECRET_KEY=$JWT_SECRET_KEY"
echo "================================"