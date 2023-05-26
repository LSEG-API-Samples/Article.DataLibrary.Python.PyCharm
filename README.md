# How to set up Python Development Project with PyCharm

- version: 1.0.0
- Last update: June 2023
- Environment: Windows
- Compiler: Python
- Prerequisite: [Python and PyCharm prerequisite](#prerequisite)

## <a id="Introduction"></a>Introduction

[PyCharm](https://www.jetbrains.com/pycharm/) is a flagship cross-platform [Python](https://www.python.org/) IDE developed by [JetBrains](https://www.jetbrains.com/) (the same company that developed [IntelliJ IDEA](https://www.jetbrains.com/idea/)). The IDE provides coding assistance such as code completion and syntax/error highlight, project and code navigation, package management, debugger, version control, and much more. 

PyCharm has two editions, a Professional Edition with full features, and a free Community Edition (see the [comparison](https://www.jetbrains.com/products/compare/?product=pycharm&product=pycharm-ce)), this makes the IDE attractive to both newbie and full-stack Python developers.

As a developer, I am using the [IntelliJ IDEA](https://www.jetbrains.com/idea/) for Java development projects and [Visual Studio Code](https://code.visualstudio.com/) editor for Python and JavaScript/TypeScript development projects. I admit that I am never interested in PyCharm. However, there are a lot of questions about how to use our Python APIs/libraries with PyCharm, so it is a good opportunity for me to learn how to use PyCharm and share my knowledge.

This example project shows how to create a Python project with the [Refinitiv Data Library for Python](https://developers.refinitiv.com/en/api-catalog/refinitiv-data-platform/refinitiv-data-library-for-python) on PyCharm. It covers from starting a blank project to importing existing source code and dependencies configuration file to the IDE. 

Note: This project is based on **PyCharm Community Edition 2023.1.2** and the **Classic UI**. If you are using a Professional Edition or New UI, some user interfaces may be different. 

## <a id="prerequisite"></a>Python and PyCharm prerequisite

Before I am going further, there is some prerequisite, dependencies, and libraries that the project is needed.

### PyCharm

Firstly, you can download (or purchase) the PyCharm IDE installer file from [PyCharm](https://www.jetbrains.com/pycharm/download) website. 

### Anaconda or Miniconda

Next, the [Anaconda](https://www.anaconda.com/) or [Minconda](https://conda.io/en/latest/miniconda.html)

### Access to the Refinitiv Data Platform

This project uses Refinitiv Data Platform (RDP) User ID type credential (example: sample@lseg.com). 

Please contact your Refinitiv representative to help you with the RDP account and services.

TBD

## <a id="ref"></a>References

For further details, please check out the following resources:
* [Refinitiv Data Library for Python](https://developers.refinitiv.com/en/api-catalog/refinitiv-data-platform/refinitiv-data-library-for-python) on the [Refinitiv Developer Community](https://developers.refinitiv.com/) website.
* [Getting Started with Refinitiv Data Platform](https://developers.refinitiv.com/en/article-catalog/article/getting-start-with-refinitiv-data-platform) article
* [PyCharm: Configure a conda virtual environment](https://www.jetbrains.com/help/pycharm/conda-support-creating-conda-virtual-environment.html#create-a-conda-environment)


