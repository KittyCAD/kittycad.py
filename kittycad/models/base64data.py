import base64
import binascii


class Base64Data:
    def __init__(self, data: bytes):
        """
        Initializes the object.

        If the provided data is already in base64 encoded format, it will store it.
        If the data is a regular byte string, it will encode and then store it.
        """
        if self.is_base64(data):
            self._data = str(data, "utf-8")
        else:
            encoded = base64.b64encode(data)
            self._data = str(encoded, "utf-8")

    @staticmethod
    def is_base64(data: bytes) -> bool:
        """Checks if given data is base64 encoded."""
        try:
            str_data = str(data, "utf-8")
            _ = base64.urlsafe_b64decode(str_data.strip("=") + "===")
            return True
        except binascii.Error:
            return False

    def get_encoded(self) -> str:
        """Returns the stored base64 encoded data."""
        return self._data

    def get_decoded(self) -> bytes:
        """Returns the decoded byte string."""
        return base64.urlsafe_b64decode(self._data.strip("=") + "===")
