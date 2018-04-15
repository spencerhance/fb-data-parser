# fb-data-parser
An extendable parser for your Facebook data

Facebook has been allowing you to [download all of your data](https://www.facebook.com/help/131112897028467) for a while, but only in HTML format.  This tool is designed to help you export that to a variety of formats (only JSON right now) so that you can more easily analyze it.  

## Data types
Facebook gives you data about the following things:
* ads
* apps
* contact info
* events
* friends
* messages
* photos
* security

Right now this tool only supports exporting your messages, but support for all types is planned.  A CLI script is provided, but the modules are designed to be easily accessed from an IPython notebook for easier analysis.  Examples will be added soon.

## Usage
```
usage: fb-data-parser.py [-h] -d DATA_DIR [-t OUTPUT_TYPE]

Parse Facebook data.

optional arguments:
  -h, --help            show this help message and exit
  -d DATA_DIR, --data DATA_DIR
                        Path to facebook data directory
  -t OUTPUT_TYPE, --output-type OUTPUT_TYPE
                        Type of the output, only json for now
```
