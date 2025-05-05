from setuptools import setup, find_packages

setup(
    name="arafix",
    version="0.1.0",
    description="Arabic diacritization preprocessing and evaluation tools",
    author="Your Name",
    packages=find_packages(),
    install_requires=[
        "transformers",
        "datasets",
        "pyarabic",
        "jiwer",
        "torch",
        "tqdm"
    ],
    python_requires=">=3.7",
)
