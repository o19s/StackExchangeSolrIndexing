AutoTaxonomyExtractionAndTagging
================================


To start Solr:
```
cd apache-solr-x.x.x/example
java -jar -Dsolr.solr.home=<full_path_to_this_dir>/solr_home start.jar
```

To index documents:
```
python extractDocs.py "<full_path_to_stack_exchange_dump/stack_exchange_file.xml" | curl -d @- http://localhost:8983/solr/update?commit=true -v -H "Content-Type:text/xml"
```

Configuration details in solr_home/collection1/conf/schema.xml
