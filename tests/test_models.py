# Tests for database models
def test_create_user(client):
    """Test creating a new user in the database"""
    from models import users, db
    
    with client.application.app_context():
        # Create a new user
        new_user = users("John Doe", "john@example.com")
        db.session.add(new_user)
        db.session.commit()
        
        # Retrieve the user
        retrieved_user = users.query.filter_by(name="John Doe").first()
        
        assert retrieved_user is not None
        assert retrieved_user.name == "John Doe"
        assert retrieved_user.email == "john@example.com"

def test_user_query_by_name(client):
    """Test querying users by name"""
    from models import users, db
    
    with client.application.app_context():
        # Create multiple users
        user1 = users("Alice", "alice@example.com")
        user2 = users("Bob", "bob@example.com")
        user3 = users("Alice Smith", "alice.smith@example.com")
        
        db.session.add_all([user1, user2, user3])
        db.session.commit()
        
        # Query by exact name match
        alice_users = users.query.filter_by(name="Alice").all()
        assert len(alice_users) == 1
        assert alice_users[0].email == "alice@example.com"
        
        # Query all users
        all_users = users.query.all()
        assert len(all_users) == 3

def test_user_string_representation(client):
    """Test the string representation of user model"""
    from models import users
    
    with client.application.app_context():
        user = users("Test User", "test@example.com")
        # The default string representation should include the model info
        assert "Test User" in str(user) or "users" in str(user)

def test_user_attributes(client):
    """Test user model attributes"""
    from models import users
    
    with client.application.app_context():
        user = users("Jane Doe", "jane@example.com")
        
        assert hasattr(user, 'name')
        assert hasattr(user, 'email')
        assert hasattr(user, '_id')
        
        assert user.name == "Jane Doe"
        assert user.email == "jane@example.com"
        assert user._id is None  # ID is None until saved to database

def test_user_id_after_save(client):
    """Test that user gets an ID after being saved to database"""
    from models import users, db
    
    with client.application.app_context():
        user = users("Test User", "test@example.com")
        db.session.add(user)
        db.session.commit()
        
        assert user._id is not None
        assert user._id > 0
