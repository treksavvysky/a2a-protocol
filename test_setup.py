#!/usr/bin/env python3
"""
Quick test to verify the virtual environment and setup is working correctly.
"""

def test_imports():
    """Test that all required dependencies can be imported."""
    try:
        import fastapi
        import uvicorn
        import requests
        import sqlalchemy
        import alembic
        import pydantic
        print("✅ All core dependencies imported successfully")
        
        # Test version info
        print(f"   - FastAPI: {fastapi.__version__}")
        print(f"   - SQLAlchemy: {sqlalchemy.__version__}")
        print(f"   - Pydantic: {pydantic.__version__}")
        return True
    except ImportError as e:
        print(f"❌ Import error: {e}")
        return False

def test_database_models():
    """Test that the database models can be imported."""
    try:
        import models
        import database
        print("✅ Database models and configuration imported successfully")
        return True
    except ImportError as e:
        print(f"❌ Database import error: {e}")
        return False

def test_app_creation():
    """Test that the FastAPI app can be created."""
    try:
        from client_server import app
        print("✅ FastAPI application created successfully")
        print(f"   - Routes: {[route.path for route in app.routes]}")
        return True
    except Exception as e:
        print(f"❌ App creation error: {e}")
        return False

def main():
    print("🔧 Testing A2A Protocol Development Environment")
    print("=" * 50)
    
    all_tests_passed = True
    
    all_tests_passed &= test_imports()
    print()
    all_tests_passed &= test_database_models()
    print()
    all_tests_passed &= test_app_creation()
    
    print("\n" + "=" * 50)
    if all_tests_passed:
        print("🎉 All tests passed! Development environment is ready.")
        print("\n💡 Next steps:")
        print("   • Run the server: python client_server.py")
        print("   • Check database: sqlite3 a2a.db")
        print("   • Run tests: python test_client.py")
    else:
        print("❌ Some tests failed. Please check the errors above.")
    
    return all_tests_passed

if __name__ == "__main__":
    main()
