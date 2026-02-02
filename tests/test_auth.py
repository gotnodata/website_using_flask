# Tests for authentication blueprint routes
def test_login_page_get(client):
    """Test that the login page loads successfully"""
    response = client.get('/login')
    assert response.status_code == 200
    assert b'Login' in response.data  # Check for actual content, not template name

def test_login_post_new_user(client):
    """Test login with a new user creates the user in database"""
    from models import users, db
    
    response = client.post('/login', data={
        'nm': 'testuser',
        'email': 'test@example.com'
    }, follow_redirects=True)
    
    assert response.status_code == 200
    assert b'Profile' in response.data  # Check for actual content
    
    # Check user was created in database
    with client.application.app_context():
        user = users.query.filter_by(name='testuser').first()
        assert user is not None
        assert user.email == 'test@example.com'

def test_login_post_existing_user(client):
    """Test login with existing user shows info message"""
    from models import users, db
    
    # Create user first
    with client.application.app_context():
        existing_user = users('existinguser', 'existing@example.com')
        db.session.add(existing_user)
        db.session.commit()
    
    response = client.post('/login', data={
        'nm': 'existinguser',
        'email': 'newemail@example.com'
    }, follow_redirects=True)
    
    assert response.status_code == 200
    assert b'User already exists' in response.data

def test_user_page_when_logged_in(client):
    """Test user page when user is logged in"""
    with client.session_transaction() as sess:
        sess['user'] = 'testuser'
        sess['email'] = 'test@example.com'
    
    response = client.get('/user')
    assert response.status_code == 200
    assert b'Profile' in response.data  # Check for actual content
    assert b'test@example.com' in response.data

def test_user_page_when_not_logged_in(client):
    """Test user page redirects to login when not logged in"""
    response = client.get('/user', follow_redirects=True)
    assert response.status_code == 200
    assert b'Login' in response.data

def test_user_page_post_update_email(client):
    """Test updating email from user page"""
    with client.session_transaction() as sess:
        sess['user'] = 'testuser'
        sess['email'] = 'old@example.com'
    
    response = client.post('/user', data={
        'email': 'new@example.com'
    }, follow_redirects=True)
    
    assert response.status_code == 200
    assert b'Email was saved' in response.data
    assert b'new@example.com' in response.data

def test_logout(client):
    """Test logout functionality"""
    with client.session_transaction() as sess:
        sess['user'] = 'testuser'
        sess['email'] = 'test@example.com'
    
    response = client.get('/logout', follow_redirects=True)
    assert response.status_code == 200
    assert b'Login' in response.data
    
    # Check session is cleared
    with client.session_transaction() as sess:
        assert 'user' not in sess
        assert 'email' not in sess

def test_login_when_already_logged_in(client):
    """Test login page when already logged in redirects to user page"""
    with client.session_transaction() as sess:
        sess['user'] = 'testuser'
        sess['email'] = 'test@example.com'
    
    response = client.get('/login', follow_redirects=True)
    assert response.status_code == 200
    assert b'Already logged in' in response.data
    assert b'Profile' in response.data
