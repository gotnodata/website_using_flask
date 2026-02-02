# Tests for main blueprint routes
def test_home_page(client):
    """Test that the home page loads successfully"""
    response = client.get('/')
    assert response.status_code == 200
    assert b'UserHub' in response.data  # Check for actual content, not template name

def test_view_page(client):
    """Test that the view page loads successfully"""
    response = client.get('/view')
    assert response.status_code == 200
    assert b'All Users' in response.data  # Check for actual content, not template name

def test_view_page_with_users(client):
    """Test that the view page displays users correctly"""
    from models import users, db
    
    # Add a test user
    with client.application.app_context():
        test_user = users("Test User", "test@example.com")
        db.session.add(test_user)
        db.session.commit()
    
    response = client.get('/view')
    assert response.status_code == 200
    assert b'Test User' in response.data
    assert b'test@example.com' in response.data
