from coalesce_api.strategies.base_strategy import BaseStrategy


class AverageStrategy(BaseStrategy):
    def coalesce_values(self, *args, **kwargs):
        """
        {deductible: 1000, stop_loss: 10000, oop_max: 5000}
        """
        keys_to_average = kwargs["fields"]
        values_sum = { key: 0 for key in keys_to_average}
        average_total_values = len(args)
        for api_response in args:
            for key in keys_to_average:
                if api_response[key]:
                    values_sum[key] += api_response[key]
        averaged_values = {
            key: value/average_total_values
            for key, value
            in values_sum.items()}
        return averaged_values
