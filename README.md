Getting Started
===============

1. Download a StackExchange dump of your choosing: http://www.clearbits.net/torrents/2076-aug-2012
2. Download Solr: http://lucene.apache.org/solr/
3. Start Solr:
```
cd apache-solr-x.x.x/example
java -jar -Dsolr.solr.home=<full_path_to_this_dir>/solr_home start.jar
```
4. Index documents (currently only works for posts):
```
python extractDocs.py "<full_path_to_stack_exchange_dump/posts.xml" | curl -d @- http://localhost:8983/solr/update?commit=true -v -H "Content-Type:text/xml"
```

Configuration details in solr_home/collection1/conf/schema.xml
