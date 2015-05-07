
class Aggregator(object):
    js = set()
    js_fs = '<script type="text/javascript" src="%s"></script>'
    css = set()
    css_fs = '<link type="text/css" rel="stylesheet" href="%s" />'

    def add_js(self, file_url):
        self.js.add(file_url)

    def add_css(self, file_url):
        self.css.add(file_url)

    @property
    def rendered_js(self):
        ret = [self.js_fs%(f,) for f in self.js]
        return '\n'.join(ret)

    @property
    def rendered_css(self):
        ret = [self.css_fs%(f,) for f in self.css]
        return '\n'.join(ret)

class AggregatorMiddleware(object):
    def process_request(self, request):
        request.aggregator = Aggregator()
