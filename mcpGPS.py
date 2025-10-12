from mcp.server.fastmcp import FastMCP
import json
import sys
import os

# Create MCP server
mcp = FastMCP("gps-server",port=8101,host="0.0.0.0")

# Check if the correct number of arguments is provided
if len(sys.argv) != 2:
    print("Usage: python mcpGPS.py <directory_path>")
    sys.exit(1) # Exit with an error code

directory_path = sys.argv[1]

# Check if the provided path exists and is a directory
if not os.path.exists(directory_path):
    print(f"Error: Path '{directory_path}' does not exist.")
    sys.exit(1)
elif not os.path.isdir(directory_path):
    print(f"Error: Path '{directory_path}' is not a directory.")
    sys.exit(1)

# Tool: return location as latitude and longitude
@mcp.tool()
def get_location() -> str:
    """Return the current location as latitude and longitude. Timestamp is included 
       for information on when the location was last determined."""
    try:
        file_name = directory_path + "/gps.json"
        with open(file_name, "r") as f:
            data = json.load(f)
        
        # Extract values
        latitude = round(data.get("latitude"),5)
        longitude = round(data.get("longitude"),5)
        # altitude = data.get("altitude")
        timestamp = data.get("timestamp")

        return json.dumps({
            "latitude": latitude,
            "longitude": longitude,
            # "altitude": altitude,
            "timestamp": timestamp
        })
    
    except FileNotFoundError:
        print(f"Error: {file_name} not found.")
    except json.JSONDecodeError:
        print("Error: Invalid JSON format.")


# Run server
if __name__ == "__main__":
    mcp.run(transport="streamable-http")