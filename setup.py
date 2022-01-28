from setuptools import setup, find_packages


setup(
    name="naver-blog-backer",
    version="0.1",
    license='MIT',
    description="for your naver blog backup and backlinks",
    long_description=open('README.md').read(),
    keywords=['naver','naver blog','blog crawling', 'blog backup', 'blog backlink'],

    author="Jeongseup",
    author_email="thswjdtmq4@inu.ac.kr",
    url="https://github.com/Jeongseup/naver-blog-backer",
    download_url="https://github.com/Jeongseup/naver-blog-backer/archive/main.zip",

    install_requires = ['tqdm', 'beautifulsoup4', 'requests'],
    packages=find_packages(exclude=[]),
    python_requires = '>=3',
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: BSD License",
        "Operating System :: Windows OS"
    ],
)