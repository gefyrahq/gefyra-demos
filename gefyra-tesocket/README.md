# Gefyra Websocket Tester

A simple FastAPI application with WebSocket support, containerized with Docker and ready for Kubernetes deployment.

## Features
- WebSocket endpoint at `/ws`
- Simple web interface for testing
- Docker containerization
- Built with `uv` for faster package installation

## Prerequisites
- Python 3.12+
- Docker
- `uv` (Rust-based Python package installer)

## Local Development

1. Install dependencies:
```bash
uv sync
```

2. Run the application:
```bash
fastapi dev main.py
```

3. Open http://localhost:8000 in your browser to test the WebSocket.

## Docker Build

```bash
docker build -t gefyra-tesocket .
docker run -p 8000:8000 gefyra-tesocket
```

## Testing the WebSocket

After deployment, you can test the WebSocket connection using the web interface at the root URL or by using a WebSocket client:

```python
import asyncio
import websockets

async def test_websocket():
    uri = "ws://localhost:8000/ws"
    async with websockets.connect(uri) as websocket:
        # Send a message
        await websocket.send("Hello, WebSocket!")
        # Receive message
        response = await websocket.recv()
        print(f"Received: {response}")

asyncio.get_event_loop().run_until_complete(test_websocket())
```
