#!/usr/bin/env python3

from setuptools import setup, find_packages

def get_version():
	"""Get software version from the main window."""
	import gi
	gi.require_version('Gtk', '3.0')
	gi.require_version('Notify', '0.7')
	from sunflower.gui.main_window import MainWindow
	return '{major}.{minor}.{build}'.format(**MainWindow.version)


setup(
		name='Sunflower',
		version=get_version(),
		description='Twin-panel file manager.',
		author='Mladen Mijatov',
		author_email='meaneye.rcf@gmail.com',
		url='https://sunflower-fm.org',
		license='GPLv3',
		install_requires=[
			'PyGObject',
			'chardet'
			],
		packages=find_packages(),
		include_package_data=True,
                data_files=[
                    ('share/sunflower/images/', ['images/sunflower.svg', 'images/splash.png']),
                    ('share/applications', ['Sunflower.desktop'])
                ],
		entry_points={'console_scripts': ['sunflower = sunflower.__main__:main']}
		)
