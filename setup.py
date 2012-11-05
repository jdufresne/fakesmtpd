from distutils.core import setup


def main():
    name = 'fakesmtpd'
    version = '0.0.4'
    url = 'http://pypi.python.org/packages/source/f/{name}/{name}-{version}.tar.gz'

    setup(name=name,
          version=version,
          url='http://pypi.python.org/pypi/{name}'.format(name=name),
          description=open('README.rst').read(),
          author='Jon Dufresne',
          author_email='jon@jondufresne.org',
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
