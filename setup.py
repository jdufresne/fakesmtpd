#!/usr/bin/python3

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

from setuptools import setup


def main():
    name = 'fakesmtpd'
    version = '0.0.7'
    url = 'http://pypi.python.org/packages/source/f/{name}/{name}-{version}.tar.gz'

    setup(name=name,
          version=version,
          url='http://pypi.python.org/pypi/{name}'.format(name=name),
          descriptoin='Fake SMTP server',
          long_description=open('README.rst').read(),
          author='Jon Dufresne',
          author_email='jon.dufresne@gmail.com',
          download_url=url.format(name=name, version=version),
          classifiers=[
            'Development Status :: 3 - Alpha',
            'Environment :: No Input/Output (Daemon)',
            'Intended Audience :: Developers',
            'Intended Audience :: Information Technology',
            'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',
            'Programming Language :: Python',
            'Topic :: Communications :: Email :: Mail Transport Agents',
          ],
          scripts=['fakesmtpd'],
          data_files=[('/lib/systemd/system', ['fakesmtpd.service'])])


if __name__ == '__main__':
    main()
