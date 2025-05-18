from setuptools import setup, find_packages

setup(
    name="ml_eval_dashboard",
    version="0.1",
    description="A reusable machine learning evaluation dashboard built with Streamlit.",
    author="MTB",
    author_email="your.email@example.com",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "streamlit",
        "matplotlib",
        "scikit-learn",
        "pandas",
        "numpy"
    ],
    entry_points={
        "console_scripts": [
            "ml-eval-dashboard=ml_eval_dashboard.main:main"
        ]
    },
)
