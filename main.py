from fastmcp import FastMCP
import random
import json


mcp = FastMCP("Simple Calculator Server")

@mcp.tool
def add(a: float, b: float) -> float:
    """Add two numbers."""
    return a + b

@mcp.tool
def random_number(min_val: int, max_val: int) -> int:
    """Generate a random number between min_val and max_val."""
    return random.randint(min_val, max_val)

@mcp.resource("info://server")
def server_info() -> str:
    """Return server information."""
    info = {
        "name": "Simple Calculator Server",
        "version": "1.0",
        "description": "A simple server that performs basic arithmetic operations.",
        "tools": ["add", "random_number"],
        "authors": ["Alok Kumar"],
    }
    return json.dumps(info, indent=4)

## start
if __name__ == "__main__":
    mcp.run(transport = "http", host = "0.0.0.0", port = 8000)