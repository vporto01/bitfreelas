BITFREELAS |
This Django application is a Bitcoin-only freelancing platform designed to connect clients and freelancers. It allows users to create and manage projects, and supports transactions exclusively in Bitcoin.

Features
User Management: The application uses a custom user model, CustomUser, with a custom manager for creating users and superusers. The CustomUser model includes fields for email, first name, last name, username, and status flags for active and staff users.

Clients and Freelancers: The Client and Freelancer models represent the two main types of users on the platform. Both models have a one-to-one relationship with the CustomUser model. Clients can post projects and freelancers can apply to these projects. Freelancers can list their skills, set an hourly rate, and provide a bio and portfolio link.

Skills: The Skill model represents the various skills that a freelancer can have. A freelancer can have multiple skills, which can be used by clients to find suitable freelancers for their projects.

Projects: The Projects model represents the projects posted by clients. Each project is associated with a client and has a short description, full description, posting date, type (fixed or hourly), budget, and currency (default is BTC). This allows clients to provide all the necessary details about their projects.

Wallets: The Wallets model represents the Bitcoin wallets of users. Each wallet is associated with a user and contains fields for the private key, private key in WIF format, public key in hexadecimal format, and the Bitcoin address. This allows for transactions to be made directly on the platform using Bitcoin.

API: The application provides a RESTful API with endpoints for clients, freelancers, and user registration. This allows for easy integration with other services or front-end applications.

Installation and Setup
Clone the repository: git clone https://github.com/vporto01/bitfreelas.git
Navigate to the project directory: cd repository
Install the requirements: pip install -r requirements.txt
Run the migrations: python manage.py migrate
Start the server: python manage.py runserver
Usage
To use the application, navigate to localhost:8000 in your web browser. From there, you can register as a new user, log in, create a profile as a client or freelancer, post or apply to projects, and make transactions in Bitcoin.

Please note that this is a brief description based on the code snippets provided. For a more detailed description, you may need to provide more context or specific details about the application's functionality.
