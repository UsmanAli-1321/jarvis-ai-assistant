"""Web Search Utilities"""

import webbrowser
import urllib.parse

class WebSearch:
    def google_search(self, query):
        """Search Google"""
        try:
            url = f"https://www.google.com/search?q={urllib.parse.quote(query)}"
            webbrowser.open(url)
            return f"Searching for '{query}'"
        except Exception as e:
            return f"Error: {str(e)}"