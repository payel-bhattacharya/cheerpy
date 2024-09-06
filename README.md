# CheerPy

CheerPy is a simple and fun Python library that sends random success and failure messages. Perfect for integrating into your CI/CD pipelines or any Python projects.

## Installation

```bash
pip install cheerpy


## Usage

from cheerpy import CheerPy

cheerpy = CheerPy()
print(cheerpy.cheer("success"))  # Output: random success message
print(cheerpy.cheer("fail"))  # Output: random failure message

## Features
- Random success messages 🎉
- Random failure messages 💪
- Customizable messages 🚀
