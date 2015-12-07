# Reporter MD
Convert your [Reporter App](http://www.reporter-app.com/) entries into markdown, then import them into [Day One](http://dayoneapp.com/)... If you want.
[Example here](https://raw.githubusercontent.com/sambev/reportermd/master/images/dayone_example.png)

### General Usage:
`python reportermd <date> <dayone>`

*Dates MUST be in YYYY-MM-DD format


##### To see command help run:
```bash
python reportermd -h
```

##### To create a markdown file from all reporter app entries on October 28th 2015 run:
```bash
python reportermd 2015-10-28
```

##### To create a markdown file from all reporter app entries on October 28th 2015 and import them into dayone for that same day:
```bash
python reportermd 2015-10-28 --dayone=True
```
*Removes the markdown file when complete.

---

### Installation
From Source:
 1. `git clone https://github.com/sambev/reportermd.git`
 2. `cd reportermd`
 3. `python setup.py install`
 4. 
 
With pip:
`pip install reportermd`

With easy_install:
`easy_install reportermd`

### Requirements:
Tested on python 2.7.10
