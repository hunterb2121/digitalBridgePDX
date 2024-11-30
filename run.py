from app.utils.db import initialize_pool

print("Initializing pool...")
initialize_pool(1, 20)

from app import create_app

print("Running create_app() in run.py...")
app = create_app()


if __name__ == "__main__":
    print("Starting the Flask application...")
    app.run(host="0.0.0.0", port=5000, debug=True)