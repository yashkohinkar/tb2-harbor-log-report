# Parse Access Log and Generate Summary Report

You are given an Apache-style HTTP access log in the working directory at `/app/access.log`. Analyze the traffic and generate a JSON summary report.

## Success Criteria

Your solution must produce a file at `/app/report.json` containing a JSON object with these exact fields:

1. **total_requests** (integer): The total number of HTTP requests in the log
2. **unique_ips** (integer): The count of unique client IP addresses
3. **top_path** (string): The most frequently requested HTTP path (e.g., `/index.html`)

## Example Output

```json
{
  "total_requests": 6,
  "unique_ips": 3,
  "top_path": "/index.html"
}
```

## Notes

- The log follows Apache Combined or Common format (IP address is the first field on each line)
- HTTP methods include GET, POST, PUT, DELETE, HEAD, PATCH
- Paths are extracted from the request line (e.g., `"GET /path HTTP/1.1"`)
- All three fields must be present and must have the correct types (integers for counts, string for path)
- If there is a tie for the most popular path, any of the tied paths is acceptable
