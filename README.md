fab
===

Flexible Address Book


TODO
====

AB: parse testdata

JS: Plan datastructure
JS: Create testdata



Structure of database table (example):

    ID TIMESTAMP TYPE FIELDNAME DATA
    01 1358639061 STRING prename Erika
    01 1358639061 STRING surname Mustermann
    01 1358639061 STRING title Dr. rer. nat.
    01 1358639061 STRING street Musterstraße
    01 1358639061 STRING housenumber 2
    01 1358639061 STRING postcode 12345
    01 1358639061 STRING city Musterhausen
    01 1358639061 STRING mail em@mustermann.com
    01 1358639061 STRING phone.office +49 123 4567878 
    01 1358639061 STRING phone.mobile +49 171 4567878
    01 1158639061 STRING phone.mobile +49 178 4567878
    

Ideas 
=====
    import time
    int(time.time())
    > 1358639061
 
 * timestamp 0 means no timestamp set yet ==> replace with current time asap
 * Do we want to add binary data (jpeg images and so on) to the database, or just as link to a directory like
 
    01 1358639061 STRING picture.jpeg EMustermann.jpeg

 * the file could be in `~/fab/gfx/EMustermann.jpeg` for example
 * we want to use python 3
 * [Markdown syntax](http://en.wikipedia.org/wiki/Markdown)
 * how can we format the bank information (in one line)? IBAN+BIC
 * add a version information of the field definition to the database. May be we write `mail.office` instead of `mail` in future
