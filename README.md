fab
===

fab stands for Flexible Address Book. 
It will be shipped with a standard set of keys like "name" but the 
user may enhance it with own keys like ID's for "jabber" and "ICQ" 
bank account data and so on.


TODO
====

JS: Create testdata


DONE
====
JS: Plan datastructure (done in group meeting on 2013-04-20)


SQL Table
=========
ID(KEY) UserID Type Valid Priority Value TimeStamp Comment


Ideas 
=====
    import time
    int(time.time())
    > 1358639061
 
 * timestamp 0 means no timestamp set yet ==> replace with current time asap
 * Do we want to add binary data (jpeg images and so on) to the database, or just as link to a directory like
 
    01 1358639061 STRING picture.jpeg EMustermann.jpeg

 * the file could be in `~/fab/gfx/EMustermann.jpeg` for example
 * we have to use python 2.7 in order to reuse existing modules like vobject
 * [Markdown syntax](http://en.wikipedia.org/wiki/Markdown)
 * how can we format the bank information (in one line)? IBAN+BIC
 * type=phone, subtype=office
 * we can use import vobject to handle vCard files https://pypi.python.org/pypi/vobject