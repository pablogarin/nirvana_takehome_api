from coalesce_api.strategies.base_strategy import BaseStrategy
from coalesce_api.strategies.context_handler import register_strategy

@register_strategy
class AverageStrategy(BaseStrategy):
  def run(self, *args, **kwargs):
    if "fields" not in kwargs:
      raise ValueError("You must provide the fields to average out.")
    keys_to_average = kwargs["fields"]
    values_sum = { key: 0 for key in keys_to_average}
    average_total_values = len(kwargs["payload"])
    for api_response in kwargs["payload"]:
      for key in keys_to_average:
        if api_response[key]:
          values_sum[key] += api_response[key]
    averaged_values = {
      key: value/average_total_values
      for key, value
      in values_sum.items()}
    return averaged_values
  
  @classmethod
  def get_type(cls):
    return 'average', cls
