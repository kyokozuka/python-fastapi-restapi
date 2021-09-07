import sys
sys.dont_write_bytecode = True
import uvicorn
from src import app


if __name__ == '__main__':
    host = '0.0.0.0'
    port = 8000
    uvicorn.run("app:app", host=host, port=port, debug=True, reload=True)