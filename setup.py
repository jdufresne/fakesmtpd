from distutils.core import setup


setup(name='fakesmptd',
      version='0.0.1',
      description="Fake SMTP Server",
      scripts=['fakesmtpd'],
      data_files=[('/lib/systemd/system', ['fakesmtpd.service'])])
