# Blogging Website

This project is a blogging website built with Django, designed to provide a platform for users to create, manage, and read blog posts. It features user authentication, post creation, and a clean, user-friendly interface for managing blog content.

## Features

- User Authentication: Register, login, and manage user accounts.
- Blog Management: Create, edit, delete, and view blog posts.
- Categories and Tags: Organize blog posts with categories and tags.
- Responsive Design: A modern and responsive UI for an optimal experience on any device.
- Search Functionality: Easily find posts by keywords or tags.

## Setup Instructions

1. Clone the Repository:
   ```bash
   git clone https://github.com/Raistar22/blogsite.git
   cd blogsite
   ```

2. Create and Activate a Virtual Environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install Dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Run Migrations:
   ```bash
   python manage.py migrate
   ```

5. Create a Superuser (Admin):
   ```bash
   python manage.py createsuperuser
   ```

6. Start the Development Server:
   ```bash
   python manage.py runserver
   ```

7. Access the Website:
   Open your browser and navigate to `http://127.0.0.1:8000/` to view the blogging website. Access the admin interface at `http://127.0.0.1:8000/admin/` using the superuser credentials created.

## Technologies Used

- Django
- Python 3.x
- HTML/CSS


## Contributing

Contributions are welcome! Please follow the [guidelines](CONTRIBUTING.md) for contributing to this project.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgements

- [Django](https://www.djangoproject.com/)
