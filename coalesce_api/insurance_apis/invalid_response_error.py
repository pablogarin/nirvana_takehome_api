import json


class InvalidResponseError(Exception):
  def __init__(self, url, status_code, message="The service responded with an error"):
    super().__init__(message)
    self.message = message
    self.url = url
    self.status_code = status_code

  @property
  def details(self):
    return {
      "success": False,
      "message": self.message,
      "code": self.status_code,
      "url": self.url
    }
  
  def to_json(self):
    return json.dumps(self.details)
