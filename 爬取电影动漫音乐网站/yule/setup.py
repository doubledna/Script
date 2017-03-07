from setuptools import setup, find_packages

setup(name = 'yule',
        entry_points = {
            'scrapy.commands': [
                'crawlall = yule.commands:crawlall',
                ],
            },
        )
