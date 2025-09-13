from setuptools import setup, find_packages

setup(
    name="ai_assistant_provider",
    version="0.0.6",
    author="Arun CS",
    author_email="aruncs31s@proton.com",
    description="Sub Module for AI Assistant Project",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/aruncs31s/ai-assistant-provider",  # Add your repo URL
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
    ],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
    python_requires=">=3.7",
   
)