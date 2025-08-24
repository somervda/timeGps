from mcp.server.fastmcp import FastMCP
from datetime import datetime
from timezonefinder import TimezoneFinder
import pytz

# Create MCP server
mcp = FastMCP("time-server")

# Tool: return current UTC time
@mcp.tool()
def get_UTC_time() -> str:
    """Return the current UTC time as an ISO 8601 string."""
    return datetime.utcnow().replace(tzinfo=pytz.utc).isoformat()

# Tool: return local time by latitude & longitude
@mcp.tool()
def get_local_time_by_location(latitude: float, longitude: float) -> str:
    """
    Given latitude and longitude, return the local time at that location.
    Time is returned as an ISO 8601 string.
    """
    tf = TimezoneFinder()
    tz_name = tf.timezone_at(lng=longitude, lat=latitude)

    if not tz_name:
        raise ValueError("Could not determine timezone for given coordinates")

    tz = pytz.timezone(tz_name)
    utc_now = datetime.utcnow().replace(tzinfo=pytz.utc)
    local_time = utc_now.astimezone(tz)
    return local_time.isoformat()

# Run server
if __name__ == "__main__":
    mcp.run()