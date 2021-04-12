import json


class InvalidMethodError(Exception):
  def __init__(self, url, method, message="Invalid method supplied to API call"):
    super().__init__(message)
    self.message = message
    self.url = url
    self.method = method

  @property
  def details(self):
    return {
      "success": False,
      "message": self.message,
      "method": self.method,
      "url": self.url
    }
  
  def to_json(self):
    return json.dumps(self.details)
