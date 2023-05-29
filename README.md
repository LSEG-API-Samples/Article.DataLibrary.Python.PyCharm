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
- *New environment using*: Conda
- *Location*: Point to your &lt;Conda&gt;\envs\\&lt;Project name&gt;
- *Python version*: Based on your preference, I choose Python 3.10. Please refer to the [Python End Of Life page](https://endoflife.date/python)
- *Conda executable*: Point to &lt;Conda&gt;\Script\conda.exe location in your Conda installation folder
- *Create a main.py welcome script*: Choose this option

![figure-2](images/02_pycharm_newproject_a.png "PyCharm new project")

Note: PyCharm supports the [Virtualenv](https://virtualenv.pypa.io/en/latest/), [Pipenv](https://pipenv.pypa.io/en/latest/), [Poetry](https://python-poetry.org/), and [Anaconda](https://www.anaconda.com/)/[Minconda](https://conda.io/en/latest/miniconda.html) Python virtual environment and Packaging/Dependencies Management tools. I choose Conda for Python versioning flexibility. Please choose this option based on your development requirement.

Then PyCharm initializes the project and Conda environment.

![figure-3](images/03_pycharm.png)

Once the project and Conda environment are created successfully, you see this IDE screen with an example ```main.py``` code as follows:

![figure-4](images/04_pycharm.png "create new project success")

You can use this example ```main.py``` script to test if PyCharm can run Python properly on your machine. To run the code, right-click and choose Run 'Main' menu or click the Run command at the toolbar.

![figure-5](images/04_pycharm_2.png 'Run Python project')

The result is as follows:

![figure-6](images/05_pycharm.png "hello world example")

### Step 2: Set up the Project setting for Refinitiv Data Library for Python

The next step is installing the Refinitiv Data Library for Python dependencies. Firstly, open the Python Package tool window available at the bottom of the screen as follows:

![figure-7](images/06_pycharm_package.png "PyCharm Package tool window")

You can start typing the package name in the Search field. PyCharm then shows matching packages on each repository. Since we are using a Conda environment, so PyCharm shows search results on both Conda and PyPI repositories like the following search result for the *python-dotenv* package.

![figure-8](images/06_pycharm_package_conda.png "PyCharm search package")

To install Refinitiv Data Library for Python, type **refinitiv** in the Search field. The RD Lib - Python is available on PyPI only, so I choose the **refinitiv-data** package under PyPI and click the "Install with pip" button to install the package.

![figure-9](images/06_pycharm_package_rd.png "PyCharm install refinitiv-data 1")

Once the package installation is successful, you see the notification, and the **refinitiv-data** package is listed in the installed packages.

![figure-10](images/06_pycharm_package_rd_3.png "PyCharm install refinitiv-data 2")

![figure-11](images/06_pycharm_package_rd_4.png "PyCharm install refinitiv-data 3")

The next step is testing the RD Lib - Python. You can add the **refinitiv-data.config.json** file to the IDE with the following configurations:

``` JSON
{
    "logs": {
        "level": "debug",
        "transports": {
            "console": {
                "enabled": false
            },
            "file": {
                "enabled": false,
                "name": "refinitiv-data-lib.log"
            }
        }
    },
    "sessions": {
        "default": "platform.rdp",
        "platform": {
            "rdp": {
                "app-key": "App Key",
                "username": "RDP User ID",
                "password": "RDP Password"
            },
           
        }
       
    }
}
```

Please refer to the [Quickstart page](https://developers.refinitiv.com/en/api-catalog/refinitiv-data-platform/refinitiv-data-library-for-python/quick-start) if you are using other Access Points such as Desktop session, etc.

Next, change the code of ```main.py``` to call RD - Lib Python instead as follows:

``` Python

import json
import refinitiv.data as rd

if __name__ == '__main__':
    rd.open_session(name='platform.rdp')
    data = rd.get_data(['EUR=', 'THB='], fields=['BID', 'ASK'])
    print(data)

    rd.close_session()
```

Your PyCharm IDE should look like the following screenshot:

![figure-12](images/07_pycharm_code.png "PyCharm with RD Code")

If your RDP credential works fine, the running result shows as follows:

![figure-13](images/07_pycharm_code_2.png "PyCharm with RD Run Result")

Now your PyCharm is ready to work with Refinitiv Data Library for Python.

For more detail about packages management with PyCharm, please check the [official document](https://www.jetbrains.com/help/pycharm/installing-uninstalling-and-upgrading-packages.html).

### Step 3: Plotting Graph

TBD

## <a id="ref"></a>References

For further details, please check out the following resources:
* [Refinitiv Data Library for Python](https://developers.refinitiv.com/en/api-catalog/refinitiv-data-platform/refinitiv-data-library-for-python) on the [Refinitiv Developer Community](https://developers.refinitiv.com/) website.
* [Getting Started with Refinitiv Data Platform](https://developers.refinitiv.com/en/article-catalog/article/getting-start-with-refinitiv-data-platform) article
* [PyCharm: Configure a conda virtual environment](https://www.jetbrains.com/help/pycharm/conda-support-creating-conda-virtual-environment.html#create-a-conda-environment)


