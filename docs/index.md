The `data-password-entropy` package provides a function to calculate the entropy of a password. Entropy measures a password's strength in resisting brute-force attacks. The function employs a straightforward, empirical algorithm to determine the password's entropy based on the characters it contains.

The common approach to ensuring password quality typically involves enforcing specific rules, such as minimum length requirements and mandatory inclusion of punctuation characters. However, these rigid rules can inadvertently restrict a small but significant portion of users who prefer creating passwords based on their own criteria. For instance, consider why the password `jackslippedonicefellonhisass`, which is highly secure due to its length and unpredictability, should be deemed unacceptable simply because it doesn't include punctuation. Conversely, the password `P@ssw0rd`, which complies with many conventional requirements, frequently appears in public password databases, underscoring its weakness despite adhering to standard rules.

Evaluating a password based on its information entropy provides a more nuanced and accurate measure of its strength. Entropy assigns a numerical value to a password, reflecting its complexity and resistance to brute-force attacks. Unlike rule-based systems, entropy-based evaluation considers the overall unpredictability and diversity of characters within the password. According to the algorithm implemented in this module, a password achieving an entropy score of **80 bits** is deemed sufficiently secure for most applications.

## Table of contents
* [Description](#description)
* [Installation](#installation)
* [Example](#example)
* [API Reference](#api-reference)
* [Performance](#performance)
* [Links](#links)
* [License](#license)


## Description
Information entropy, also referred to as password quality or password strength, quantifies a password's ability to withstand brute-force attacks.

There are a lot of different ways to determine a password's entropy. 

### How It Works
The data-password-entropy package uses a simple, empirical algorithm to calculate password entropy through the following steps:

* Character classification:
  * Categorization: each character in the password is assigned to a specific class, such as numbers, lowercase letters, uppercase letters, or others.
  * Assumption: characters within the same class are assumed to have an equal probability of being selected.
  * Symbol base expansion: incorporating characters from multiple classes increases the total number of possible symbols (symbol base), thereby enhancing the password's entropy.

* Effective length calculation:
  * Orderliness reduction: sequences like `1234` are considered less secure than `1342` because ordered sequences reduce total entropy.
  * Repeating characters: repeating sequences, such as `aaaa`, diminish entropy compared to more varied character arrangements.

* Character classes:
  * ASCII characters: characters with Unicode code points up to 127 are categorized into predefined classes (e.g., numbers, uppercase letters).
  * Non-ASCII characters: all characters with code points above 127 are grouped into a single class.

There is no well-defined approach to processing national or extended Unicode characters. For instance, the Greek letters block in the Unicode Character Database comprises approximately 400 symbols. However, not all of these symbols are used with equal frequency. An attacker who knows that a password may contain Greek letters is unlikely to target the simple α (Greek letter Alpha) with the same probability as the more complex ἆ (Greek small letter Alpha with psili and perispomeni). This disparity in usage patterns makes it impractical to assign distinct probabilities to each individual character within a script or Unicode block.

Therefore, to maintain simplicity and efficiency, all characters with Unicode code points above 127 are grouped into a single class. This approach strikes a balance between accuracy and practicality, ensuring that the entropy calculation remains both manageable and sufficiently representative of the password's complexity.

### Limitations
* No dictionary checks: the algorithm does not verify passwords against known weak passwords or dictionary words.
* No obfuscation evaluation: it cannot assess the complexity introduced by character substitutions like `p@ssw0rd`.
* No sequence detection: keyboard sequences or other patterned inputs are not specifically handled.
* No personal information assessment: the algorithm does not account for passwords containing personally identifiable information, such as names or dates of birth.

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

## API Reference
### `password_entropy(password: str) -> int`

Calculates the entropy of the provided password.

**Parameters:**
- `password` (`str`): The password string to evaluate.

**Returns:**
- `int`: The entropy value in bits representing the password's strength.


## Performance
On a modern processor core (as of 2024), the module can perform approximately 100,000 calls per second for random passwords consisting of 32 characters.


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
