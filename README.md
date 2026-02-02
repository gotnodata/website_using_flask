# Paul's First Flask Website 🐕

A modern, responsive Flask web application with user management and a cute dog gallery!

## 🌟 Features

- **User Authentication**: Login/Register system with session management
- **User Profiles**: Update and manage user information
- **Dog Gallery**: Interactive image gallery with full-screen modal viewing
- **Modern UI**: Beautiful, responsive design with smooth animations
- **Database**: SQLite database for user data storage

## 🛠️ Tech Stack

- **Backend**: Flask (Python)
- **Database**: SQLite with Flask-SQLAlchemy
- **Frontend**: HTML5, CSS3, JavaScript
- **Styling**: Custom CSS with modern design patterns
- **Icons**: Emoji icons for lightweight UI elements

## 📦 Installation

1. **Clone the repository**
   ```bash
   git clone <your-repo-url>
   cd website_using_flask
   ```

2. **Create and activate virtual environment**
   ```bash
   python -m venv venv
   # Windows
   venv\Scripts\activate
   # macOS/Linux
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the application**
   ```bash
   python app.py
   ```

5. **Open your browser**
   Navigate to `http://127.0.0.1:5000`

## 🧪 Testing

Run the test suite:

```bash
# Run all tests
pytest

# Run with verbose output
pytest -v

# Run with coverage
pytest --cov=. --cov-report=html
```

See [TESTING.md](TESTING.md) for detailed testing instructions.

## 🚀 Usage

### **Getting Started**
1. Visit the home page to see the welcome message and dog gallery
2. Click on any dog image to view it in full-screen mode
3. Register a new account or login to access user features

### **User Management**
- **Register**: Enter your name and email to create an account
- **Login**: Use your credentials to access your profile
- **Profile**: Update your email and view user information
- **View Users**: See all registered users in the system

### **Dog Gallery**
- Click any dog image to open it in full-screen modal
- Use the × button, click outside, or press Escape to close
- Enjoy the smooth animations and responsive design

## 📁 Project Structure

```
website_using_flask/
├── app.py                 # Main Flask application
├── models.py              # Database models
├── config.py              # Application configuration
├── test_config.py         # Test configuration
├── requirements.txt       # Python dependencies
├── pytest.ini            # Pytest configuration
├── blueprints/           # Flask blueprints
│   ├── auth.py           # Authentication routes
│   └── main.py           # Main routes
├── static/               # Static files
│   └── style.css
├── templates/            # HTML templates
│   ├── base.html
│   ├── index.html
│   ├── login.html
│   ├── user.html
│   └── view.html
├── tests/                # Test suite
│   ├── conftest.py       # Test fixtures
│   ├── test_auth.py      # Authentication tests
│   ├── test_main.py      # Main route tests
│   └── test_models.py    # Model tests
├── instance/             # Instance files (gitignored)
│   └── users.sqlite3     # SQLite database
└── README.md
```

## 🎨 Design Features

- **Modern UI**: Clean, card-based layout with gradients
- **Responsive Design**: Works perfectly on desktop and mobile
- **Animations**: Smooth transitions and hover effects
- **Interactive Elements**: Full-screen image modal, form validation
- **Color Scheme**: Blue/teal gradient theme with professional styling

## 🔧 Configuration

The application uses the following configuration:
- **Database**: SQLite (`users.sqlite3`)
- **Session Lifetime**: 5 minutes
- **Secret Key**: Configured for session management

## 📱 Screenshots

*(Add screenshots of your application here)*

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is open source and available under the [MIT License](LICENSE).

## 👤 Author

**Paul** - *Initial work* - [YourGitHubUsername]

## 🙏 Acknowledgments

- Flask documentation and community
- Modern CSS design patterns
- Emoji icons for UI elements

---

**Enjoy the application! 🐕✨**
