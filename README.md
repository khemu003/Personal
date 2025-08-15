# Flask Finance - Personal Finance Management System

## Overview
Flask Finance is a modern web application designed to help users manage their personal finances effectively. Built with Flask and MySQL, it provides a secure and user-friendly interface for tracking income, expenses, and financial goals.

## Features

### User Management
- Secure user registration and authentication
- Password strength validation
- Remember me functionality
- Social login options (Google and GitHub integration ready)
- User profile management

### Financial Management
- Track income and expenses
- Categorize transactions
- View transaction history
- Financial analytics and insights
- Export transaction data

### Security
- Password hashing using Werkzeug
- CSRF protection
- Secure session management
- Input validation and sanitization

### User Experience
- Modern, responsive design
- Intuitive navigation
- Real-time feedback
- Flash messages for user notifications
- Dark mode support

## Technology Stack

### Backend
- **Framework**: Flask 3.1.0
- **Database**: MySQL
- **ORM**: SQLAlchemy 2.0.27
- **Authentication**: Flask-Login 0.6.3
- **Form Handling**: Flask-WTF 1.2.1
- **Security**: Werkzeug 3.1.0

### Frontend
- **HTML5 & CSS3**
- **JavaScript**
- **Font Awesome** for icons
- **Google Fonts** (Inter)
- **Responsive Design**

### Data Analysis
- **Pandas** for data manipulation
- **NumPy** for numerical operations
- **Matplotlib** for data visualization
- **Seaborn** for statistical graphics

## Installation

### Prerequisites
- Python 3.8 or higher
- MySQL Server
- pip (Python package manager)

### Setup Steps

1. **Clone the repository**
   ```bash
   git clone https://github.com/khemu003/Personal.git
   ```

2. **Create and activate a virtual environment**
   ```bash
   # Windows
   python -m venv venv
   .\venv\Scripts\activate

   # Linux/Mac
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Environment Configuration**
   Create a `.env` file in the root directory with the following variables:
   ```
   SECRET_KEY=your_secret_key_here
   MYSQL_HOST=localhost
   MYSQL_USER=your_mysql_username
   MYSQL_PASSWORD=your_mysql_password
   MYSQL_DB=flask_finance
   MYSQL_PORT=3306
   ```

5. **Database Setup**
   - Create a MySQL database named `flask_finance`
   - The application will automatically create necessary tables on first run

6. **Run the Application**
   ```bash
   python run.py
   ```
   The application will be available at `http://localhost:5000`

## Usage

### User Registration
1. Navigate to the signup page
2. Fill in your details (username, email, password)
3. Accept the terms and conditions
4. Click "Create Account"

### Login
1. Enter your email and password
2. Optionally check "Remember me"
3. Click "Sign In"

### Managing Finances
1. **Adding Transactions**
   - Click "Add Transaction"
   - Select transaction type (income/expense)
   - Enter amount and details
   - Choose category
   - Save transaction

2. **Viewing Transactions**
   - Access dashboard for overview
   - Use filters for specific time periods
   - Export data if needed

3. **Analytics**
   - View spending patterns
   - Track income vs expenses
   - Monitor category-wise spending

## Development

### Project Structure
```
flask_finance/
├── app/
│   ├── __init__.py
│   ├── models/
│   ├── routes/
│   ├── static/
│   ├── templates/
│   └── utils/
├── config.py
├── requirements.txt
├── run.py
└── README.md
```

### Running Tests
```bash
pytest
```

### Contributing
1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## Security Considerations
- Never commit the `.env` file
- Regularly update dependencies
- Use strong passwords
- Enable 2FA when available
- Keep your secret key secure

## License
This project is licensed under the MIT License - see the LICENSE file for details.

## Support
For support, please:
- Open an issue in the GitHub repository
- Contact through the application's feedback form
- Email: support@flaskfinance.com

## Acknowledgments
- Flask community for the excellent framework
- Contributors and maintainers
- Open source libraries used in this project
