The `data-password-entropy` package provides a function to calculate the entropy of a password. The entropy is a measure of the password's strength in resisting brute-force attacks. The function uses a simple, empirical algorithm to determine the password's entropy based on the characters it contains.


## Table of contents
* [Description](#description)
* [Installation](#installation)
* [Example](#example)
* [Performance](#performance)
* [Links](#links)
* [License](#license)


# Description
Information entropy, also known as password quality or password strength when used in a discussion of the information security, is a measure of a password in resisting brute-force attacks.

There are a lot of different ways to determine a password's entropy. We use a simple, empirical algorithm: first, all characters from the string splitted to several classes, such as numbers, lower- or upper-case letters. Any characters from one class have equal probability of being in the password. Mix of the characters from the different classes extends the number of possible symbols (symbols base) in the password and thereby increases its entropy. Then, we calculate the effective length of the password to ensure the next rules:

* some orderliness decreases total entropy, so '1234' is weaker password than '1342',

* repeating sequences decrease total entropy, so 'a' x 100 insignificantly stronger than 'a' x 4 (it may seem, that's too insignificantly).

Do not expect too much: an algorithm does not check the password's weakness with dictionary lookup, can not evaluate obfuscation like 'p@ssw0rd', sequences from a keyboard row or personally related information like date of birth.

Probability of characters occurring depends on the capacity of character class only. Perhaps, it should be taken into account a prevalence of symbol class actually — it is very unlikely to find a control character in the password. But common password policies don't allow control characters, spaces or extended characters in passwords, therefore, so they should not occur in practice.

Similarly, there is no well-defined approach to process national characters. For example, the Greek letters block in Unicode Character Database contains about 400 symbols, but not all of them have equivalent frequency of usage. An intruder, who knows that password may contain Greek letters, will not probe the α (Greek letter Alpha) with the same probability as the ἆ (Greek small letter Alpha with psili and perispomeni), therefore it might be incorrect to consider a whole UCD block or script as a base for calculating probabilities. We consider all characters with codes higher than 127 form one class.


## Installation
Requires Python version 3.7 or higher. To install the package, run:
```bash
pip install data-password-entropy
```


## Example
```python
from data_password_entropy import password_entropy

e = password_entropy('password')
# returns 35
e = password_entropy('Vgk4@HDk6X7gEp7')
# returns 85
```


## Performance
On a modern processor core (as of 2024), the module can perform approximately 100,000 calls per second for random passwords of 32 characters.


## Links
* [Password strength](https://en.wikipedia.org/wiki/Password_strength) — Wikipedia article on password strength.
* [Password-Entropy](https://pypi.org/project/Password-Entropy/) at PyPI — another Python package that implements password entropy calculation.
* [Data::Password::Entropy](https://metacpan.org/pod/Data::Password::Entropy) — my module for Perl, somewhat outdated.

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
