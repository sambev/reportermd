# Reporter MD
Convert your [Reporter App](http://www.reporter-app.com/) entries into markdown, then import them into [Day One](http://dayoneapp.com/)... If you want.

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
Currently I only have the hard way:
 1. `git clone https://github.com/sambev/reportermd.git`
 2. `cd reportermd`
 3. `pip install -r requirements.txt`
