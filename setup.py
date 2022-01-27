import setuptools


setuptools.setup(
    name="naver 이름",
    version="0.1",
    license='MIT',
    author="패키지 제작자 이름",
    author_email="패키지 제작자 이메일",
    description="패키지 요약",
    long_description=open('README.md').read(),
    url="github url 등",
    packages=setuptools.find_packages(),
    classifiers=[
        # 패키지에 대한 태그
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent"
    ],
)