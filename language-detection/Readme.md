# Language detection with polyglot

This is a small example webapp which uses polyglot to detect the language of some given text. 

## Polyglot
Polyglot is a natural language pipeline that supports massive multilingual applications.
It's able to detect 196 different languages and furthermore supports such things like 
tokenization, entity recognition, sentiment analysis and many more.

In this little proof of concept, it's used to build a small web service which detects
the language of some given text. The web application contains a standard web form
for interactive testing and of course a REST interface which returns a json record
(see example below).

## Example usage
Send a request to the REST interface at /detect/json like this:
```
$ curl -X POST -H "Content-Type: application/json"  -d '{"text": "For a fews dollars more"}'  http://localhost:5000/detect/json
```
Result looks like this:
```
{
  "count":3,
  "records":[
    {"code":"en","confidence":99.0,"name":"English","read bytes":1666},
    {"code":"un","confidence":0.0,"name":"un","read bytes":0},
    {"code":"un","confidence":0.0,"name":"un","read bytes":0}
  ],
  "success":true
}
```


## Links
* [Polyglot documentation](https://polyglot.readthedocs.io/en/latest/index.html)
* [Detection example](https://polyglot.readthedocs.io/en/latest/Detection.html)
* [Image ready to go at Docker Hub](https://hub.docker.com/repository/docker/docdiesel/language-detection)

