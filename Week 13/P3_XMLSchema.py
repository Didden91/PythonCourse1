XML Schema is a language that describes the LEGAL FORMAT of a XML document
A schema is expressed in terms of constraints on the structure and content of a document
A schema is often used to specify a "Contract" between systems:
"My system will only accept XML that conforms to this particular schema"
If a particular piece of XML meets the specifications of a schema, it is said to "Validate"

A piece of software that takes a piece of XML and runs it through a schema to check its validity is called a Validator

There are many XML Schema languages
We're going to be using XSD XML Schema (W3C spec)
Stands for World Wide Web Consortium (W3C) version

ISO 8601 Date/Time Format
In programming, we generally want to use ONE date/time format internationally
ISO 8601 is used, it formats like this:
2002-05-30T09:30:10Z
So that's:
Year-Month-Day T Time of day Z

Z is to specify a timezone
