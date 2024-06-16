#!/bin/bash
# Apply database migrations
python manage.py migrate --noinput

# Create superuser if it doesn't exist
echo "from django.contrib.auth.models import User; User.objects.create_superuser('root', 'root@example.com', 'root') if not User.objects.filter(username='root').exists() else None" | python manage.py shell

# Start the server
exec "$@"
