import sys

from backend.main import create_app
from backend.config import Config

app = create_app(Config)

if __name__ == '__main__':
    app.run(
        host='0.0.0.0',
        port=int(sys.argv[1]) if len(sys.argv) > 1 else 5000,
        threaded=True,
        debug=True)
