# coding=utf-8

from pybuilder.core import use_plugin, init, Author

use_plugin('python.core')
use_plugin('python.install_dependencies')

use_plugin('filter_resources')
use_plugin('copy_resources')

use_plugin('python.coverage')
use_plugin('python.distutils')
use_plugin('python.unittest')
use_plugin('python.flake8')
use_plugin('python.pydev')

authors = [Author('Aaron Swartz', ''), Author('Maximilien Riehl', 'maximilien.riehl@gmail.com')]
license = 'GPL'
name = 'html2text'
url = 'https://github.com/mriehl/html2text'
summary = 'Render html as readable plaintext'
version = '1.0.0'

default_task = ['analyze', 'publish']


@init
def set_properties(project):
    project.get_property('filter_resources_glob').append('**/html2text/__init__.py')
    project.set_property('copy_resources_target', '$dir_dist')
    project.get_property('copy_resources_glob').append('README.md')

    project.set_property('coverage_break_build', False)
    project.set_property('distutils_classifiers', [
       'Development Status :: 5 - Production/Stable',
       'Intended Audience :: Developers',
       'License :: OSI Approved :: GNU General Public License (GPL)',
       'Programming Language :: Python',
       'Programming Language :: Python :: 2',
       'Programming Language :: Python :: 2.3',
       'Programming Language :: Python :: 2.4',
       'Programming Language :: Python :: 2.5',
       'Programming Language :: Python :: 2.6',
       'Programming Language :: Python :: 2.7',
       'Programming Language :: Python :: 3',
       'Programming Language :: Python :: 3.0',
       'Programming Language :: Python :: 3.1',
       'Programming Language :: Python :: 3.2'])
