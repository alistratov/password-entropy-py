# data-password-entropy
Calculate password strength.

[![PyPI - Version](https://img.shields.io/pypi/v/data-password-entropy)](https://pypi.org/project/data-password-entropy/) [![codecov](https://codecov.io/gh/alistratov/password-entropy-py/graph/badge.svg?token=MSJLFL8XFD)](https://codecov.io/gh/alistratov/password-entropy-py) [![Documentation Status](https://readthedocs.org/projects/data-password-entropy/badge/?version=latest)](https://data-password-entropy.readthedocs.io/en/latest/?badge=latest) [![PyPI - Downloads](https://img.shields.io/pypi/dm/data-password-entropy)](https://pypistats.org/packages/data-password-entropy)


## Synopsis
```bash
pip install data-password-entropy
```

```python-repl
>>> from data_password_entropy import password_entropy
>>> password_entropy('password')
35
>>> password_entropy('Vgk4@HDk6X7gEp7')
85
```


## Overview
The `data-password-entropy` package provides a function to calculate the entropy of a password, measuring its strength against brute-force attacks. Unlike traditional rule-based methods that enforce specific criteria—such as minimum length or mandatory punctuation—which can either reject strong, unconventional passwords or accept weak ones like `P@ssw0rd`, entropy-based evaluation offers a more accurate assessment. By assigning a numerical value to a password's complexity and unpredictability, this empirical algorithm ensures that a password achieving an entropy score of 80 bits is considered sufficiently secure for most applications.


## Documentation
Read the full documentation at [Read the docs](https://data-password-entropy.readthedocs.io/en/latest/).


## License
Copyright 2024 Oleh Alistratov

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at [http://www.apache.org/licenses/LICENSE-2.0](http://www.apache.org/licenses/LICENSE-2.0).

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
