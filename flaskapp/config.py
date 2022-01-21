"""
Configure application
"""


class Config:
    """
    Configure application

    Attributes
    ----------
    testing : bool
        Set testing flag
    """
    def __init__(self, testing=False):
        self.testing = testing
        self.cors_headers = 'Content-Type'

    def get_testing(self) -> bool:
        """
        Get testing flag

        Returns
        -------
        bool
            Testing flag
        """
        return self.testing

    def get_cors_headers(self) -> str:
        """
        Get CORS headers

        Returns
        -------
        str
            Cors headers
        """
        return self.cors_headers
