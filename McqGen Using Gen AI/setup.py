
from setuptools import find_packages,setup

setup(
    name='mcqgenerator',
    version='0.0.1',
    author='Amit Singh Parihar',
    author_email='amitsinghp1007@gmail.com',
    install_requires=["openai","langchain","streamlit","python-dotenv","PyPDF2"],
    packages=find_packages()
)
