"""
Setup script for Personalize-SAM.
Allows installation via: pip install -e .
"""
from setuptools import setup, find_packages

setup(
    name="personalize-sam",
    version="0.1.0",
    description="Personalize Segment Anything Model (SAM) with 1 shot in 10 seconds",
    author="Renrui Zhang",
    license="MIT",
    python_requires=">=3.8",
    packages=find_packages(include=["per_segment_anything", "per_segment_anything.*"]),
    install_requires=[
        "torch>=1.7",
        "torchvision>=0.8",
        "opencv-python",
        "matplotlib",
        "tqdm",
        "numpy",
    ],
    extras_require={
        "dev": ["pytest", "black", "isort"],
        "gradio": ["gradio"],
    },
)
