We've talked about the request/response cycle and extracting HTML
Now we're going to be looking at information online that is specifically designed for programatic consumption.
A sort of program to program.
We call this the "wire protocol" or "wire format"
There needs to be agreement over what Wire format to use accross platforms, computers and programming languages.

When we take some data from for example Python and convert that to data that adhere's to the agreed Wire format, we call that:
SERIALIZATION, the data is serialized.

A program on the other end of the line can then DESERIALIZE the data and use it for their own purpose.
So Python can send something, Java can receive it for example.

One of these wire formats is XML
Another format is JSON (JavaScript Object Notation)
We're going to be using both of these
