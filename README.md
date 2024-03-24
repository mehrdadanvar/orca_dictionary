# Orca Dictionary

<p align="center">
<img  width="300" height="300" src="g2.svg">

</p>

Orca is a simple dictionary application meant to be used in the backend of web or mobile application focusing on English learners.
developers can easily deploy orca either locally or to a remote server

## Installation

Clone this repository by running the following in a terminal. you should have <code>git</code> installed on your system

```bash
git clone https://github.com/mehrdadanvar/orca_dictionary
```

Once cloned navigate to the api folder/directory
based on your preferences you may wish to install a python virtual envirnoment by running

```bash

python -m venv orca
source orca/bin/activate

```

```bash

cd api/
pip install -r requirements.txt

```

## V1 Popular English Words

This version is a small and simple collection of 25K common English words that elementary to upper intermediate learners can benefit from. All of the words are can be found in a the <code>populars.json</code> file in the api directory. The file represents a list of 25K objects each of which represent a word with a 3 key-value pairs.
