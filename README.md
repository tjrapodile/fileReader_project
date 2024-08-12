# fileReader_project
This repository contains a Django web application designed to handle file uploads and data storage. The application allows users to upload CSV or Excel files, process the data, and store it locally in a PostgreSQL database. The front end is built using a Bootstrap template for a clean and responsive user interface.

Features
File Upload: Users can upload CSV or Excel files containing data.
Data Storage: Uploaded files are processed and their contents are stored in a PostgreSQL database.
File Management: Uploaded files are stored locally, and users can view or manage these files through the admin web interface.
Responsive Design: The front end is built using Bootstrap, ensuring that the application is accessible across various devices.

Tech Stack
Django: The primary framework used for developing the web application.
PostgreSQL: The database system used for storing uploaded file data.
Bootstrap: A frontend framework used for styling and responsive design.

Project Structure
Views: Django views handle file uploads, data processing, and rendering the front end.
Templates: Bootstrap-based HTML templates provide a responsive and user-friendly interface.
Models: Django models define the structure for storing file data in the PostgreSQL database.
Forms: Django Forms handles file uploads and validation.

Clone the repository:
git clone  https://github.com/tjrapodile/fileReader_project.git

Navigate to the project directory:
cd fileReader_project

Create and activate a virtual environment:
python3 -m venv venv
source venv/bin/activate

Install dependencies:
pip install -r requirements.txt

Configure your PostgreSQL database settings in settings.py.
Apply migrations:
python manage.py migrate

Run the development server:
python manage.py runserver

Open your browser and visit:
http://localhost:8000

Usage
Uploading Files: Use the web interface to upload CSV or Excel files.
Viewing Data: Access the stored data via the admin interface or custom views, depending on the application setup
