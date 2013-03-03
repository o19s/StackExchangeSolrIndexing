Getting Started
===============

1. Download a StackExchange dump of your choosing: http://www.clearbits.net/torrents/2076-aug-2012
1. Unzip the data set you're interested in (7-zip format)
1. Download Solr: http://lucene.apache.org/solr/
1. Start Solr:
```
cd apache-solr-x.x.x/example
java -jar -Dsolr.solr.home=<full_path_to_this_dir>/solr_home start.jar
```
1. Index documents (currently only works for posts):
```
python extractDocs.py "<full_path_to_stack_exchange_dump>/posts.xml"
```
(Configuration details can be found in solr_home/collection1/conf/schema.xml)
1. Search!
```
localhost:8983/solr/collection1/select?q=Tags:java
```
1. And for a neat visual, try `file://localhost<full_path_to_this_dir>/plot.html?q=OwnerUserId:22656&fq=PostTypeId:2` in your browser
