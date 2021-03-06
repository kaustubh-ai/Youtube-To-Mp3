import setuptools


with open('README.md', 'r') as f:
	long_description = f.read()

setuptools.setup(
	name='dizzy-dj',
	version='2.0.1',
	author="Kaustubh Dixit",
	author_email='kaustubh.29.dixit@gmail.com',
	description='YouTube video to mp3 converter',
	long_description=long_description,
	long_description_content_type='text/markdown',
	url='https://github.com/kaustubh-ai/Youtube-To-Mp3',
	packages=setuptools.find_packages(),
	install_requires=['Selenium>=3', 'beautifulsoup4', 'requests'],
	python_requires='>=3',
	classifiers=[
		'Programming Language :: Python :: 3',
		"License :: OSI Approved :: MIT License",
		"Operating System :: OS Independent",
	],
)
