import os
from setuptools import find_packages, setup

with open(os.path.join(os.path.dirname(__file__), 'README.rst')) as readme:
    README = readme.read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
        name='kbims-reptile',
        version='0.1',
        packages=find_packages(exclude=['tests', ]),
        include_package_data=True,
        license='MIT License',
        description='BIMS Project',
        long_description=README,
        url='http://staging.healthyrivers.kartoza.com',
        author='Dimas Ciputra, Alison Mukoma',
        author_email='dimas@kartoza.com, alison@kartoza.com',
        classifiers=[
            'Environment :: Web Environment',
            'Framework :: Django',
            'Framework :: Django :: 1.11',
            'Intended Audience :: Developers',
            'License :: OSI Approved :: MIT License',  # example license
            'Operating System :: OS Independent',
            'Programming Language :: Python',
            'Programming Language :: Python :: 2.7',
            'Topic :: Internet :: WWW/HTTP',
            'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        ],
        install_requires=[
            'Django==1.11',
            'django-allauth==0.35.0',
            'django-role-permissions==2.2.0',
            'markdown==2.6.11',
            'django-braces==1.9.0',
            'django-model-utils==1.4.0',
            'djangorestframework==3.7.7',
            'django-filter==1.1.0',
            'coreapi==2.3.3',
            'pygbif==0.2.0',
        ],
        dependency_links=[
            'git+https://github.com/soynatan/django-easy-audit.git',
            'git+https://github.com/kartoza/django-bims.git',
        ]
)
