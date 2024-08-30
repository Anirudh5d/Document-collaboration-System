import json
import random
import os
import django
from django.conf import settings
from datetime import datetime, timedelta
import pytz

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
django.setup()

from django.contrib.auth import get_user_model
from documents.models import Document
from tasks.models import Task

User = get_user_model()

# Number of additional documents and tasks to generate
num_documents = 1500
num_tasks = 1500

# Lists to hold the document and task data
documents = []
tasks = []

# Get all users in the system
users = list(User.objects.all())
if not users:
    raise Exception("No users found. Ensure that you have users in your database before generating data.")

# Set timezone
timezone = pytz.timezone('UTC')  # Adjust to your specific timezone if needed

# Generate documents data with more content
for i in range(num_documents):
    long_content = " ".join([f"Content for document {i + 1}." for _ in range(50)])
    created_at = timezone.localize(datetime.now() - timedelta(days=random.randint(0, 365))).isoformat()
    doc = {
        "model": "documents.document",
        "pk": i + 1,
        "fields": {
            "title": f"Document {i + 1}",
            "content": long_content,
            "collaborators": random.sample([user.id for user in users], k=random.randint(3, len(users))),
            "created_by": random.choice(users).id,
            "created_at": created_at,  # Add created_at field
            "updated_at": created_at  # Add updated_at field
        }
    }
    documents.append(doc)

# Generate tasks data with more details
for i in range(num_tasks):
    long_description = " ".join([f"Description for task {i + 1} with more details." for _ in range(20)])
    created_at = timezone.localize(datetime.now() - timedelta(days=random.randint(0, 365))).isoformat()
    task = {
        "model": "tasks.task",
        "pk": i + 1,
        "fields": {
            "title": f"Task {i + 1}",
            "description": long_description,
            "assigned_users": random.choice(users).id,
            "status": random.choice(['pending', 'in_progress', 'completed']),
            "created_at": created_at,  # Add created_at field
            "updated_at": created_at  # Add updated_at field
        }
    }
    tasks.append(task)

# Save documents data to JSON file
with open('documents_data.json', 'w') as f:
    json.dump(documents, f, indent=4)

# Save tasks data to JSON file
with open('tasks_data.json', 'w') as f:
    json.dump(tasks, f, indent=4)

print('Data generated successfully')
