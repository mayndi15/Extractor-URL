class extractor:

    def __init__(self, url):
        self.url = self.sanitize(url)
        self.validate()

    def sanitize(self, url):
        return url.strip()

    def validate(self):
        if not self.url:
            raise ValueError("URL is empty")

    def get_base_url(self):
        params_range_index = self.url.find("?")
        base_url = self.url[:params_range_index]
        return base_url

    def get_params_url(self):
        params_range_index = self.url.find("?")
        params_url = self.url[params_range_index + 1:]
        return params_url

    def get_params_value(self, params):
        find_params = self.get_params_url().find(params)
        index_params = find_params + len(params) + 1
        params_range_index = self.get_params_url().find("&", index_params)

        if params_range_index == -1:
            params = self.get_params_url()[index_params:]
        else:
            params = self.get_params_url()[index_params:params_range_index]

        return params
