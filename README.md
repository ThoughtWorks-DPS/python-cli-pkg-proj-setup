# python-cli-setup

[![PyPI - Version](https://img.shields.io/pypi/v/python-cli-setup.svg)](https://pypi.org/project/python-cli-setup)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/python-cli-setup.svg)](https://pypi.org/project/python-cli-setup)

-----

**Table of Contents**

- [Installation](#installation)
- [License](#license)

## Installation

```console
pip install python-cli-setup
```

## License

`python-cli-setup` is distributed under the terms of the [MIT](https://spdx.org/licenses/MIT.html) license.


local development 

```
hatch new python-cli-setup # how created
hatch run lint
hatch run test
hatch build
hatch publish
```

for publish set  

HATCH_INDEX_REPO=test or main  
HATCH_INDEX_USER=__token__  
HATCH_INDEX_AUTH=appropriate pypi api token  