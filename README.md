# TemplateRepeater
A utility for taking a text template with variables and repeating it to an output, similar to mail merge.


##  Motivation
This program was created because I frequently have a need to create large, repetitive CSV or text files for import into custom software. A lot of them are the same line or lines repeated over and over with different values for important bits. So I wrote a utility to deal with it.

## Installation
I work almost exclusively on Windows, but if you want, you should be able to use / compile it on any other platform that Python works on. I haven't tested it, though.

## Use
The "template" file is the bit you want to repeat over and over, with header. For example, this might be the first three rows of a CSV file. You should add "variables" to it, which are by default delimited by ` (backtick). You can change the delimiter in the interface.
The program can excise any number of header rows and place them in the output exactly once; set the header rows control to the number of header rows you want this done to.
The "answer" file is a CSV with column name headers corresponding to the variable names you've used (without backticks). Each row will be one repetition of the template with the values on that line substituted into the text.
The output file is pretty self explanatory, I hope.

Open it up, tell it where the template file is and hit Parse. You should see the variables you placed in the file here.
Tell it where the answer file is and hit Parse. You should see an identical list of variables here; if not, make sure the column names in the CSV line up with the delimited variables in the template file.

Note: changes in either file won't be detected until you hit Parse, even if you reopen the file.

Set the output file, preview if you want, then write it. I suggest doing a quick check of the file before you import it into wherever...

## Improvements
I'm always open to pull requests, though I may be a bit slow. Things I haven't gotten around to yet:
* Footer functionality to parallel the header function
* Error checking of some sort for missing / extra variables
* Loading the file when you open it rather than having a Parse button
* Testing
