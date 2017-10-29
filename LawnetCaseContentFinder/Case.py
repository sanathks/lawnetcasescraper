from bs4 import BeautifulSoup
from slugify import slugify

__author__ = "Sanath Samarasinghe (sanath@serrexlabs.com)"
__version__ = "0.0.1"
__license__ = "MIT"


class Case:
    def __init__(self, html_content):
        self.html_content = BeautifulSoup(html_content, 'html.parser')

    def get(self):
        case_html = self.html_content.select("p[hidden=0]")
        return case_html[0].getText().encode('utf-8').strip()

    def get_file_slug(self):
        return slugify(self.html_content.title.getText())
