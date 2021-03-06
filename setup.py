import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
	long_description = fh.read()

setuptools.setup(
    name="naver-blog-backer",
    version="0.1.0",
    license='GLPv3',
    description="Backup your naver blog and Create backlink text file",
    long_description=long_description,
    long_description_content_type="text/markdown",
    keywords=['naver', 'naver blog', 'blog crawling', 'blog backup', 'blog backlink'],
    author="Jeongseup",
    author_email="thswjdtmq4@inu.ac.kr",
    url="https://github.com/Jeongseup/naver-blog-backer",
    download_url="https://github.com/Jeongseup/naver-blog-backer/archive/main.zip",
    install_requires=['tqdm', 'beautifulsoup4', 'requests', 'pick'],
	package_dir={"":"src"},
    packages=setuptools.find_packages(where="src"),
    python_requires='>=3.6',
    classifiers=[
        "Programming Language :: Python :: 3",
		"License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent"
    ],
)
