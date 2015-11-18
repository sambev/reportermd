#### Reporter MD
Convert your [Reporter App](http://www.reporter-app.com/) entries into markdown, then import them into [Day One](http://dayoneapp.com/)... If you want.

##### General Usage:
`python reportermd <date> <dayone>`

*Dates MUST be in YYYY-MM-DD format


##### To see command help run:
`python reportermd -h`

##### To create a markdown file from all reporter app entries on October 28th 2015 run:
`python reportermd 2015-10-28`

##### To create a markdown file from all reporter app entries on October 28th 2015 and import them into dayone for that same day:
`python reportermd 2015-10-28 --dayone=True`*
 
* Removes the markdown file when complete.
