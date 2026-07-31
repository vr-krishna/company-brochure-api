class CompanyBrochureAPIError(Exception):
    """Base exception for the application."""

    def __init__(self, message: str):
        self.message = message
        super().__init__(message)


class InvalidURLError(CompanyBrochureAPIError):
    """Raised when an invalid URL is provided."""


class WebsiteFetchError(CompanyBrochureAPIError):
    """Raised when website content cannot be retrieved."""


class ParsingError(CompanyBrochureAPIError):
    """Raised when website content cannot be parsed."""


class LLMGenerationError(CompanyBrochureAPIError):
    """Raised when the LLM request fails."""