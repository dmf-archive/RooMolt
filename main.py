from mcp.server.fastmcp import FastMCP
import httpx
import os
import json

# Configuration
API_KEY = os.environ.get("MOLTBOOK_API_KEY")
# Use the canonical WWW URL
BASE_URL = "https://www.moltbook.com/api/v1"

if not API_KEY:
    raise ValueError("MOLTBOOK_API_KEY environment variable is required")

mcp = FastMCP("moltbook")

def get_headers():
    return {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json",
        "User-Agent": "node",
        "Accept": "*/*",
        "Accept-Encoding": "gzip, deflate, br",
        "Connection": "keep-alive"
    }

async def safe_request(method, url, **kwargs):
    """
    A robust request wrapper that manually handles redirects to ensure 
    headers are never stripped by the underlying library.
    """
    async with httpx.AsyncClient(follow_redirects=False) as client:
        headers = get_headers()
        if "headers" in kwargs:
            headers.update(kwargs.pop("headers"))
            
        response = await client.request(method, url, headers=headers, **kwargs)
        
        # Manual redirect handling (max 3 hops)
        redirect_count = 0
        while response.is_redirect and redirect_count < 3:
            redirect_url = response.headers.get("Location")
            if not redirect_url.startswith("http"):
                # Handle relative paths
                from urllib.parse import urljoin
                redirect_url = urljoin(url, redirect_url)
            
            # Re-issue the request to the new URL with the SAME headers
            response = await client.request(method, redirect_url, headers=headers, **kwargs)
            redirect_count += 1
            
        return response

@mcp.tool()
async def get_status():
    """Check agent claim status and basic info"""
    resp = await safe_request("GET", f"{BASE_URL}/agents/status")
    return resp.text

@mcp.tool()
async def get_me():
    """Get detailed profile of the current agent"""
    resp = await safe_request("GET", f"{BASE_URL}/agents/me")
    return resp.text

@mcp.tool()
async def get_feed(sort: str = "new"):
    """Get the latest posts from Moltbook. sort can be 'hot', 'new', or 'top'."""
    resp = await safe_request("GET", f"{BASE_URL}/feed", params={"sort": sort})
    return resp.text

@mcp.tool()
async def create_post(submolt: str, title: str, content: str, url: str = None):
    """Create a new post on Moltbook"""
    payload = {"submolt": submolt, "title": title, "content": content}
    if url: payload["url"] = url
    resp = await safe_request("POST", f"{BASE_URL}/posts", json=payload)
    return resp.text

@mcp.tool()
async def create_comment(post_id: str, content: str, parent_id: str = None):
    """Comment on a post"""
    payload = {"content": content}
    if parent_id: payload["parent_id"] = parent_id
    resp = await safe_request("POST", f"{BASE_URL}/posts/{post_id}/comments", json=payload)
    return resp.text

@mcp.tool()
async def delete_post(post_id: str):
    """Delete a post by ID"""
    resp = await safe_request("DELETE", f"{BASE_URL}/posts/{post_id}")
    return resp.text

if __name__ == "__main__":
    mcp.run()
