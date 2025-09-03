# A2A Protocol Development Setup

## 🚀 Quick Start

The development environment is now fully configured and ready to use!

### Activate Development Environment

```bash
# Option 1: Use the activation script (recommended)
./activate_dev.sh

# Option 2: Manual activation
source venv/bin/activate
```

### Test Your Setup

```bash
# Run setup verification tests
python test_setup.py
```

## 📋 Project Structure

```
a2a-protocol/
├── venv/                 # Virtual environment
├── alembic/             # Database migrations
├── alembic.ini          # Alembic configuration
├── client_server.py     # Main A2A server and client implementation
├── models.py            # SQLAlchemy database models
├── database.py          # Database configuration
├── test_client.py       # Client tests
├── test_setup.py        # Environment setup tests
├── activate_dev.sh      # Development environment activation script
├── a2a.db              # SQLite database (auto-created)
├── pyproject.toml       # Project configuration
└── README.md           # This file
```

## 🔧 Development Commands

### Run the Server
```bash
python client_server.py
# Server starts on http://localhost:8000
# API docs available at http://localhost:8000/docs
```

### Database Operations
```bash
# Create a new migration
alembic revision --autogenerate -m "Add new feature"

# Apply migrations
alembic upgrade head

# Check database directly
sqlite3 a2a.db
```

### Testing
```bash
# Test the complete setup
python test_setup.py

# Run client tests
python test_client.py
```

## 🛠 Installed Dependencies

- **FastAPI** 0.116.1 - Modern web framework for APIs
- **Uvicorn** 0.35.0 - ASGI server
- **SQLAlchemy** 2.0.42 - Database ORM
- **Alembic** 1.16.4 - Database migrations
- **Pydantic** 2.11.7 - Data validation
- **Requests** 2.32.4 - HTTP client

## 🌟 Features

- **Durable Storage**: SQLite database with SQLAlchemy ORM
- **Message Persistence**: Messages are stored until delivered
- **RESTful API**: FastAPI-based server with automatic OpenAPI docs
- **Type Safety**: Full Pydantic schema validation
- **Database Migrations**: Alembic integration for schema changes
- **Development Ready**: Pre-configured testing and validation

## 📝 Current Branch

Working on: `feature/durable-storage`

This branch implements persistent message storage as the foundation for the A2A protocol's reliability features.

## 🚦 Next Steps

1. **Start Development**: Use `./activate_dev.sh` to begin
2. **Run Tests**: Verify everything works with `python test_setup.py`
3. **Start Server**: Launch with `python client_server.py`
4. **Explore API**: Visit http://localhost:8000/docs for interactive API documentation

Happy coding! 🎉
