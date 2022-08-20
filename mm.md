# What's Metadata?

Metadata is essentially data about data.

common metadata include title, description, tags, categories, author, modification date, ... to help us that

* how data was created.
* how it was altered, who altered it.
* what it can be used for.
* ...


when the data grow rapidly. we use metadata to manage data.

# Metadata Management

* discover data. (do not rebuild a dataset which is already exist.)
* understand the relationships between different piece of data.
* track how data is used.
* assess the benifits and risk associated with that use.
* become important when datalake(data warehouse) growth rapidly.

## Technical
* schema.
* path.
* name of this data.
* quality checks.
* ...
  
## Business

* who the data is serving?
* what's the business impact?
* is it on serving? 
* serving histrory?
* ...

## Operational

* run time stats
* time stamps
* volumn metric
* log info
* system
* location.

## Implementation

A lot of ways to Implement such a `service`, `platform` or whatever it is to match the goal.

We can also use `data class` in programming language to build a metadata for software engineers:

```python
class Meta:
    basename:str
    description:str
    version:str

    @property
    def fullpath(self):
        return PJ(self.basename, self.version)

    def check_schema(self):
        ...


titanic = Meta(
    basename='filestore/titanic',
    description='sample case to demo implement the metadata', version='v1')

```

# Ref

[What is Metadata Management?](https://www.informatica.com/ca/resources/articles/what-is-metadata-management.html)