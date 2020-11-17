from abc import ABC
import requests


# Abstract Base Class
class UrlGenerator(ABC):
    def __init__(self, base_url, substitute, start, end_cond):
        pass

    def generate_urls(self, start, stop_condition):
        pass


# This should be refactored into its own module in the future
class SimpleNumberUrlGenerator(UrlGenerator):
    def __init__(self, base_url, substitute, start=0, end_cond=lambda _: False):
        self.base_url = base_url
        self.substitute = substitute
        self.start = start
        self.end_cond = end_cond
        self.url_template = self._generate_template()

    def _generate_template(self):
        # Change part of the url to "{}", so that we can use string.format
        # later on, for example for url "https://github.com/galunid" and
        # substitute "galunid", the result would be:
        # "https://github.com/galunid" -> "https://github.com/{}"
        return self.base_url.replace(self.substitute, "{}")

    def generate_urls(self):
        url_template = self.url_template
        idx = self.start
        while True:
            should_stop = self.end_cond(idx)
            if should_stop:
                break

            yield url_template.format(idx)
            idx += 1


class Intruder:
    def __init__(self, url, substitute, params=None):
        self.url = url
        self.substitute = substitute
        self.params = params
        self.generator = SimpleNumberUrlGenerator(self.url, self.substitute)
        self.request_results = []

    def _request(self, url, headers=None):
        if not headers or not headers["method"] or headers["method"] == "GET":
            request_func = requests.get
        elif headers["method"] == "POST":
            request_func = requests.post
        else:
            raise ValueError("Unsupported method!")

        res = request_func(url, headers)
        return res

    def intrude(self):
        for url in self.generator.generate_urls():
            res = self._request(url, self.params)
            self.request_results.append((url, res))
            yield url, res


if __name__ == "__main__":
    intruder = Intruder("https://google.com/galunid", "galunid")
    generator = SimpleNumberUrlGenerator(intruder.url, intruder.substitute, 0, lambda x: x >= 100)
    intruder.generator = generator
    for url, result in intruder.intrude():
        print(url, result.status_code)
