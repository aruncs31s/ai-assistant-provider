from setuptools import setup, find_packages

setup(
    name="ai_assistant_provider",
    version="0.0.2",
    author="Arun CS",
    author_email="aruncs31s@proton.com",
    description="Sub Module for AI Assistant Project",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="",
    packages=find_packages(where="ai_assistant_provider"),  
    package_dir={"": "ai_assistant_provider"}, 
    include_package_data=True,
    install_requires=[
    ],
   
)