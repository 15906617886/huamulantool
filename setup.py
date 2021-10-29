from setuptools import setup, find_packages

setup(
    name = "huamulantool",
    version = "0.1.10",
    # keywords = ("pip", "pathtool","timetool", "magetool", "mage"),
    description = "jdapi tool",
    long_description = "jdapi tool",
    license = "MIT Licence",

    url = "https://github.com/15906617886/huamulantool",
    author = "huamulan",
    author_email = "540834498@qq.com",

    packages = find_packages(),
    include_package_data = True,
    platforms = "any",
    install_requires = []
)

# https://pypi.tuna.tsinghua.edu.cn/simple/huamulantool/
# python setup.py sdist
# twine upload dist/*
# pip uninstall huamulantool
# pip install huamulantool -i https://pypi.python.org/simple/