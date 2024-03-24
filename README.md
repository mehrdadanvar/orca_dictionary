# Orca Dictionary

<p align="center">
<img  width="300" height="300" src="g2.svg">

</p>

Orca is a simple dictionary application meant to be used in the backend of web or mobile applications focusing on English learners.
Developers can easily deploy orca either locally or to a remote server.

## Installation

Clone this repository by running the following in a terminal. you should have <code>git</code> installed on your system

```bash
git clone https://github.com/mehrdadanvar/orca_dictionary
```

Based on your preferences you may wish to install a python virtual environment by running :

```bash

python -m venv orca
source orca/bin/activate

```

Once the virtual environment is created and activated you should notice a (orca) sign appearing at the beginning of you terminal prompt. Then go to the api

```bash

cd api/
pip install -r requirements.txt

```

## V1 Popular English Words

This version is a small and simple collection of 25K common English words that elementary to upper intermediate learners can benefit from. All of the words can be found in a the <code>populars.json</code> file in the api directory. The file represents a list of 25K objects each of which represent a word with 3 key-value pairs.

| Key         | Value                        | Type   |
| ----------- | ---------------------------- | ------ |
| word        | the word under investigation | string |
| definitions | a list of 1-6 objects        | object |

example

```json
{
  "word": "wheel",
  "definitions": [
    {
      "pos": "n",
      "definition": "a simple machine consisting of a circular frame with spokes (or a solid disc) that can rotate on a shaft or axle (as in vehicles or other machines)",
      "examples": []
    },
    { "pos": "n", "definition": "a handwheel that is used for steering", "examples": [] },
    { "pos": "n", "definition": "forces that provide energy and direction", "examples": ["the wheels of government began to turn"] },
    { "pos": "n", "definition": "a circular helm to control the rudder of a vessel", "examples": [] },
    {
      "pos": "n",
      "definition": "game equipment consisting of a wheel with slots that is used for gambling; the wheel rotates horizontally and players bet on which slot the roulette ball will stop in",
      "examples": []
    },
    { "pos": "v", "definition": "change directions as if revolving on a pivot", "examples": ["They wheeled their horses around and left"] },
    { "pos": "v", "definition": "wheel somebody or something", "examples": [] },
    {
      "pos": "v",
      "definition": "move along on or as if on wheels or a wheeled vehicle",
      "examples": ["The President's convoy rolled past the crowds"]
    }
  ],
  "family": ["wheel", "wheelchair", "wheelchairs", "wheeler", "wheeling", "wheels"]
}
```
