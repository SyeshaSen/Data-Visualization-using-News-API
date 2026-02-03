import requests
from typing import Optional, List, Dict, Any
from src.article import Article
import os


class SearchNews:
    """
    Class to interact with the News API and retrieve news articles.
    """

    def __init__(self, api_key: str):
        """
        Initialize SearchNews by reading API key from file.

        Args:
            api_key_file: Path to file containing the API key
        """
        with open(api_key, "r") as file:
            self.__api_key = file.read().strip()

    def get_top_headlines(self, *terms: str) -> List[Article]:
        """
        Get top headlines from the News API.

        Args:
            date: Optional date filter (YYYY-MM-DD format)
            domain: Optional domain filter (e.g., 'bbc.co.uk')
            language: Optional language filter (e.g., 'en')
            *terms: Variable number of search terms

        Returns:
            List of Article objects
        """
        # TODO: Implement API call to /top-headlines endpoint
        # Base URL: https://newsapi.org/v2/top-headlines
        # Remember to include your API key in the request parameters
        # Parse JSON response and create Article objects
        parameters = {"q": " ".join(terms) if terms else "",
        "language": "en"}

        response = self._make_request("top-headlines", parameters)
        return self._create_articles_from_response(response)
        

    def get_everything(
        self,
        date: Optional[str] = None,
        domains: Optional[List[str]] = None,
        language: Optional[str] = None,
        *terms: str
    ) -> List[Article]:
        """
        Get everything from the News API.

        Args:
            date: Optional date filter (YYYY-MM-DD format)
            domain: Optional domain filter (e.g., 'bbc.co.uk')
            language: Optional language filter (e.g., 'en')
            *terms: Variable number of search terms

        Returns:
            List of Article objects
        """
        # TODO: Implement API call to /everything endpoint
        # Base URL: https://newsapi.org/v2/everything
        # Remember to include your API key in the request parameters
        # Parse JSON response and create Article objects
        parameters = { "q": " ".join(terms) if terms else "", "language": language}
        if date:
            parameters["from"] = date
            parameters["to"] = date

        if domains:
            parameters["domains"] = ",".join(domains)

        response = self._make_request("everything", parameters)
        return self._create_articles_from_response(response)


    def _make_request(self, endpoint: str, params: Dict[str, str]) -> Any:
        """
        Helper method to make API requests.

        Args:
            endpoint: API endpoint (e.g., 'top-headlines')
            params: Query parameters for the request

        Returns:
            Dictionary of JSON response
        """
        # TODO: Implement helper method for making API requests
        # This can reduce code duplication between get_top_headlines and get_everything
        base_url = "https://newsapi.org/v2/"
        url = base_url + endpoint
        params["apiKey"] = self.__api_key
        response = requests.get(url, params=params)
        return response.json()
        

    def _create_articles_from_response(self, response_data: Dict[str, Any]) -> List[Article]:
        """
        Helper method to create Article objects from API response.

        Args:
            response_data: JSON response from API

        Returns:
            List of Article objects
        """
        # TODO: Parse the 'articles' field from response and create Article objects
        articles = []

        for item in response_data.get("articles", []):
            article = Article(
                url=item.get("url"),
                source=item.get("source", {}).get("name"),
                author=item.get("author"),
                title=item.get("title"),
                description=item.get("description"),
                published_at=item.get("publishedAt"),
                content=item.get("content")
            )
            articles.append(article)

        return articles
