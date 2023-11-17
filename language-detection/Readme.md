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
curl -X POST -H "Content-Type: application/json"  -d '{"text": "Alea iacta est."}'  http://localhost:5000/detect/json 
```
Result looks like this:
```
{
  "count":3,
  "records":[
    {"code":"la","confidence":93.0,"name":"Latin","read bytes":1092},
    {"code":"un","confidence":0.0,"name":"un","read bytes":0},
    {"code":"un","confidence":0.0,"name":"un","read bytes":0}
  ],
  "success":true
}
```

## Dockerfile
Use the dockerfile to build and run a container with the webapp.

```
# Build the image
docker build -f Dockerfile  -t language-detector:poc .

# Run the image
docker run --rm --detach -p 5000:5000 language-detector:poc
```
Now point your browser to http://localhost:5000/detect/form and enter some text in any language.

## Links
* [Polyglot documentation](https://polyglot.readthedocs.io/en/latest/index.html)
* [Detection example](https://polyglot.readthedocs.io/en/latest/Detection.html)
* [Image ready to go at Docker Hub](https://hub.docker.com/repository/docker/docdiesel/language-detection)

