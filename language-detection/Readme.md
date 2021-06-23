# Language detection with polyglot

This is a small example webapp whic uses polyglot to detect
the language of some given text. 

## Example usage
Of the REST interface at /detect/json:
```
$ curl -X POST -H "Content-Type: application/json"  -d '{"text": "For a fews dollars more"}'  http://localhost:5000/detect/json
```
Result:
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

