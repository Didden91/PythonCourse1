First off, XML. Stand for eXtensible Markup Language
Primary purpose is to help informationm systems SHARE STRUCTURED DATA
We're going to be looking at:

TAGS - indicate the beginning and ending of elements

Attributes - Keyword/value pairs on the opening tag of XML

Serialize/De-Serialize - Convert data in one program into a common format that can be stored and/or transmitted between
systems in a programming language-independent manner

An example:

<person>                                START tag
  <name>Chuck</name>                    in between the tags is the content
  <phone type="intl">                   after the = is an ATTRIBUTE, which is ALWAYS between quotation marks
    +1 734 303 4456                     more content
  </phone>
  <email hide="yes" />                  another attribute followed by a SELF CLOSING tag, the / within the same tag means all the data is
                                        already contained within and the tag can be closed on the same line as it was opened.
</person>

XML for the most part does not really care about whitespaces and indentation

XML is hierachical!
You can have simple elements that are simply, open tag, enter content, close tag
but there are also complex elements, open tag, open a tag within this tag etc.
This creates PARENT tags and CHILD tags
Think of it as a tree with family relationships

Attributes are useful in that you can assign AS MANY AS YOU LIKE to a node (tag)
Whereas adding some text data can only be done once per node.

ANother way to look at XML is as PATHS. Just like navigating through a file system.

What we're going to be doing is WALK THROUGH pieces of XML data and parse this data. 
