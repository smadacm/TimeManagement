from django.templatetags.static import static

class ThemePrep(object):
    def process_view(self, request, view_func, view_args, view_kwargs):
        request.aggregator.add_js('https://ajax.googleapis.com/ajax/libs/jquery/1.11.0/jquery.min.js')
        request.aggregator.add_js(static('/static/third_party/bootstrap/js/bootstrap.min.js'))
        request.aggregator.add_css(static('/static/third_party/bootstrap/css/bootstrap.min.css')) # Bootstrap core CSS
        request.aggregator.add_css(static('/static/third_party/flatly/css/flatly.css')) # Bootstrap theme
        request.aggregator.add_css(static('/static/css/theme.css')) # Custom styles for this template
