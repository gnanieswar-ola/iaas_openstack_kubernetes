from inventory import app
from cluster_creation import app as cluster_creation_app

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', use_reloader=False)
