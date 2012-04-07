from distutils.core import setup


setup(
    name='fakesmtpd',
    version='0.0.2',
    description="Fake SMTP Server",
    scripts=['fakesmtpd'],
    data_files=[('/lib/systemd/system', ['fakesmtpd.service'])]
)
