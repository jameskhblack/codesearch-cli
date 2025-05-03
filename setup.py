from pathlib import Path

from setuptools import find_packages, setup

# The directory containing this file
HERE = Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

setup(
    name="codesearch-cli",
    version="1.5.0",
    description="Chat with your current directory's files using a local or API LLM.",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/jameskhblack/codesearch-cli",
    author="Chase Adams",
    author_email="chase.adams@gmail.com",
    license="MIT",
    packages=find_packages(),
    install_requires=[
        "faiss-cpu",
        "litellm",
        "colorama",
        "sqlitedict",
        "prompt-toolkit",
        "watchdog",
        "google-generativeai",
        "openai",
        "boto3",
        "dynaconf",
        "toml",
    ],
    extras_require={
        "recommended": [
            "llama-cpp-python",
        ],
    },
    entry_points={
        "console_scripts": [
            "codesearch-cli=dir_assistant.main:main",
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
