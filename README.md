# KitchMake

KitchMake is a modern e-commerce platform for wholesaler and retailer built using Django, providing a seamless online shopping experience. It integrates essential services like email notifications and payment processing to deliver a comprehensive solution for small-to-medium-sized businesses.

---

## Features

- **Backend**: Built with Python and Django framework for robust server-side logic.
- **Frontend**: A responsive and user-friendly interface using HTML, CSS, Bootstrap, and JavaScript.
- **Database**: PostgreSQL for reliable and scalable data storage.
- **Services**:
  - **Google Email**: For sending automated emails (order confirmations, updates, etc.).
  - **Twilio and SendBird Gateway**: For sending automated message (authentication, etc.).
  - **Razorpay and Stripe Payment Gateway**: Secure payment processing.

---

## Installation

Follow these steps to set up the project locally:

### Prerequisites
Ensure you have the following installed on your system:

- Python (>=3.10)
- pip (Python package installer)
- PostgreSQL Server
- Virtualenv (optional but recommended)

### Steps

1. **Clone the repository**:
   ```bash
   git clone https://github.com/ruchitpx/kitchmake.git
   cd kitchmake
   ```

2. **Create a virtual environment** (optional):
   ```bash
   python -m venv venv
   venv\scripts\activate   # On Windows
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Create required directories**:
   ```bash
   mkdir media
   ```

5. **Configure PostgreSQL database**:
   - Create a database in PostgreSQL:
     ```sql
     CREATE DATABASE database-name;
     USE database-name;
     ```
   - Update `settings.py` with your PostgreSQL credentials:
     ```python
     DATABASES = {
         'default': {
             'ENGINE': 'django.db.backends.postgresql',
             'NAME': 'database-name',
             'USER': 'your-username',
             'PASSWORD': 'your-password',
             'HOST': 'localhost',
             'PORT': '3306',
         }
     }
     ```

6. **Apply migrations**:
   ```bash
   python manage.py makemigrations app-name
   python manage.py migrate app-name

   python manage.py makemigrations
   python manage.py migrate
   ```

7. **Create a superuser**:
   ```bash
   python manage.py createsuperuser
   ```

   If required to change the password:
   ```bash
   python manage.py changepassword ADMIN_USER_NAME
   ```

8. **Run the development server**:
   ```bash
   python manage.py runserver
   ```

9. **Access the application**:
   Open your browser and navigate to `http://127.0.0.1:8000/`, `http://localhost:8000/`.

---

## Configuration

### Email Service (Google Email)
Update the email settings in `settings.py`:
```python
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True

EMAIL_HOST_USER = 'your-email@gmail.com'
EMAIL_HOST_PASSWORD = 'your-password'
```

### Razorpay Payment Gateway
Add your Razorpay API keys in `settings.py`:
```python
RAZORPAY_API_KEY = 'your-api-key'
RAZORPAY_API_SECRET = 'your-api-secret'
```

---

## Project Structure

```
kitchmake/
├── manage.py
├── kitchmake/
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── ...
├── app/
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   └── ...
├── static/
├── templates/
├── requirements.txt
└── README.md
```

---

## Key Functionalities

- **User Authentication**: Secure login and registration.
- **Product Management**: Add, update, and delete products.
- **Shopping Cart**: Add to cart, update quantity, and checkout.
- **Order Management**: Track orders and view order history.
- **Payment Integration**: Razorpay and Stripe payment processing.
- **Email Notifications**: Automated email alerts.

---

## Technologies Used

- **Frontend**: HTML, CSS, Bootstrap, JavaScript
- **Backend**: Python, Django
- **Database**: PostgreSQL
- **Payment Gateway**: Razorpay, Stripe
- **Email Service**: Google SMTP
- **Phone Service**: Twilio, SendBird

---

## Contribution

We welcome contributions! To contribute:

1. Fork the repository.
2. Create a new branch for your feature/bug fix:
   ```bash
   git checkout -b feature-name
   ```
3. Commit your changes:
   ```bash
   git commit -m "Description of changes"
   ```
4. Push to the branch:
   ```bash
   git push origin feature-name
   ```
5. Open a pull request on GitHub.

---

## License

This project is licensed under the [KitchMake License](LICENSE).

---

## Contact

For any questions or feedback, feel free to reach out:

- Email: ruchitpx@example.com
- GitHub: [your-username](https://github.com/ruchitpx)

---

Enjoy using **KitchMake**! 🚀
