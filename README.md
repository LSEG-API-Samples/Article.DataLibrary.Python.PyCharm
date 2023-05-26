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

Next, install the [Anaconda](https://www.anaconda.com/) or [Minconda](https://conda.io/en/latest/miniconda.html) in your machine. 

This project uses Miniconda version 23.3.1.

### Access to the Refinitiv Data Platform

This project uses Refinitiv Data Platform (RDP) User ID type credential (example: sample@lseg.com). 

Please contact your Refinitiv representative to help you with the RDP account and services.

### Internet Access to PyPi

The Refinitiv Data Library for Python is available in the Python Package Index ([PyPI](https://pypi.org/)). You can use the Python pip tool to download the library from [Refinitiv-Data package](https://pypi.org/project/refinitiv-data/) over internet. 

## <a id="whatis_rdp"></a>What is Refinitiv Data Library for Python?

Now let me turn to our example Python library for this project. The [Refinitiv Data Library for Python](https://developers.refinitiv.com/en/api-catalog/refinitiv-data-platform/refinitiv-data-library-for-python) (aka RD Lib - Python) provides a set of ease-of-use interfaces offering coders uniform access to the breadth and depth of financial data and services available on the Refinitiv Data Platform. The API is designed to provide consistent access through multiple access channels and target both Professional Developers and Financial Coders. Developers can choose to access content from the desktop, through their deployed streaming services, or directly to the cloud. With the Refinitiv Data Library, the same Python code can be used to retrieve data regardless of which access point you choose to connect to the platform.

This example project is focusing on the platform session which connecting to the [Refinitiv Data Platform APIs](https://developers.refinitiv.com/en/api-catalog/refinitiv-data-platform/refinitiv-data-platform-apis) only.  

![figure-1](images/rd_image.png "Refinitiv Data Library for Python")

For more detail regarding the Refinitiv Data Platform, please see the following APIs resources: 
- [Quick Start](https://developers.refinitiv.com/en/api-catalog/refinitiv-data-platform/refinitiv-data-library-for-python/quick-start) page.
- [Tutorials](https://developers.refinitiv.com/en/api-catalog/refinitiv-data-platform/refinitiv-data-library-for-python/tutorials) page.

## <a id="new_project"></a>Set up a blank project

### Step 1: Creating a new project

Firstly, create a new development project. Please open the PyCharm IDE and choose "New Project" on the welcome screen.

![figure-2](images/01_pycharm.png "step 1: new project")

Next, input the project location (I pick *C:\drive_d\Project\Code\Pycharm_RD_Python* folder as my work location) and set the following properties:

TBD

## <a id="ref"></a>References

For further details, please check out the following resources:
* [Refinitiv Data Library for Python](https://developers.refinitiv.com/en/api-catalog/refinitiv-data-platform/refinitiv-data-library-for-python) on the [Refinitiv Developer Community](https://developers.refinitiv.com/) website.
* [Getting Started with Refinitiv Data Platform](https://developers.refinitiv.com/en/article-catalog/article/getting-start-with-refinitiv-data-platform) article
* [PyCharm: Configure a conda virtual environment](https://www.jetbrains.com/help/pycharm/conda-support-creating-conda-virtual-environment.html#create-a-conda-environment)


