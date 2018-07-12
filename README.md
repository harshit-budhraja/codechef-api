[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](http://makeapullrequest.com)
[![HitCount](http://hits.dwyl.io/harshitbudhraja/codechef-api.svg)](http://hits.dwyl.io/harshitbudhraja/codechef-api)
# codechef-api

An unofficial Codechef API.<br>
Developed by [Harshit Budhraja](https://github.com/harshitbudhraja).

Based on simple REST principles, this Codechef API endpoints return JSON metadata about contests and ranklists, directly from the Codechef's Web Platform.

* View Contest Lists (Contest Code, Contest Name, Start, End)
	* Present Contests
	* Future Contests
	* Past Contests
* View Contest Ranklists
	* Filter By - Institution and/or Country
	* Using custom search term - User Handle, User Name etc.

## Disclaimer

**This is not an official API. Neither this API nor the developers or contributors are affiliated with Codechef or Directi in any way. The user shall be held solely responsible for any damage that could be done by its reproduction and/or use.**

## Usage

This API is deployed on Heroku from the `master` branch and is publicly accessible to everyone. The documentation will, more clearly, explain all the endpoints available.

In case you'd like to make your own deployment, you could always do it by clicking the **Deploy** button below.<br><br>
[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy)

## Documentation

*API Endpoint Root:- [https://codechef-api.herokuapp.com](https://codechef-api.herokuapp.com)*

### Contests

With the contests endpoint, you can view the present, future and past contests. All responses will be in JSON.

| Endpoint          														| Description 	| Usage	|
|---------------------------------------------------------------------------|---------------|-------|
| [/contests/present](https://codechef-api.herokuapp.com/contests/present) 	|             	|       |
| [/contests/future](https://codechef-api.herokuapp.com/contests/future)    |             	|       |
| [/contests/past](https://codechef-api.herokuapp.com/contests/past)		|				|		|

## License

```
Permission is hereby granted, free of charge, to any person obtaining a copy
of this API and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, and/or sublicense copies 
of the Software, and to permit persons to whom the Software is furnished to 
do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS, DEVELOPERS, CONTRIBUTORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, 
DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, 
ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER 
DEALINGS IN THE SOFTWARE.
```