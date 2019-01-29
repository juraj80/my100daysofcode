### Error handling

```python
try:
    method1()
    method2()
    method3()
except ExceptionType1 as x:
    # details with x
except ExceptionType2 as x:
    # details with x
except Exception:
    # general error fallback.
finally:
    # code that runs regardless of error or success.
```

Starter code:

```python
import api


def main():
    keyword = input('Keyword of title search: ')
    results = api.find_movie_by_title(keyword)

    print(f'There are {len(results)} movies found.')
    for r in results:
        print(f"{r.title} with code {r.imdb_code} has score {r.imdb_score}")


if __name__ == '__main__':
    main()

```

Let's try to add the first try/except block.

```python
import api


def main():
    keyword = input('Keyword of title search: ')   
    try:
        results = api.find_movie_by_title(keyword)
    
        print(f'There are {len(results)} movies found.')
        for r in results:
            print(f"{r.title} with code {r.imdb_code} has score {r.imdb_score}")
    except:
        print("Oh that didn't work")

if __name__ == '__main__':
    main()

```

```python
import api
import requests.exceptions


def main():
    keyword = input('Keyword of title search: ')   
    try:
        results = api.find_movie_by_title(keyword)
    
        print(f'There are {len(results)} movies found.')
        for r in results:
            print(f"{r.title} with code {r.imdb_code} has score {r.imdb_score}")
    except requests.exceptions.ConnectionError:
        print("ERROR: Could not find server. Check your network connection")
    except:
        print("Oh that didn't work")

if __name__ == '__main__':
    main()

```
If we try to hit Enter as a Keyword of title search, it would return "Oh that didn't work". If we want to know details about
returned Exception we could change the except statement. What is the actual error?

```python
import api
import requests.exceptions


def main():
    keyword = input('Keyword of title search: ')
    try:
        results = api.find_movie_by_title(keyword)

        print(f'There are {len(results)} movies found.')
        for r in results:
            print(f"{r.title} with code {r.imdb_code} has score {r.imdb_score}")
    except requests.exceptions.ConnectionError:
        print("ERROR: Could not find server. Check your network connection")
    except Exception as x:
        print(type(x))
        print("Oh that didn't work: {}".format(x))


if __name__ == '__main__':
    main()
```

```
Keyword of title search:   # in case you hit Enter
<class 'ValueError'>
Oh that didn't work: Must specify a search term.

```
So it's a ValueError. So now let's add an exception clause for that.

```python
import api
import requests.exceptions


def main():
    keyword = input('Keyword of title search: ')
    try:
        results = api.find_movie_by_title(keyword)

        print(f'There are {len(results)} movies found.')
        for r in results:
            print(f"{r.title} with code {r.imdb_code} has score {r.imdb_score}")
    except requests.exceptions.ConnectionError:
        print("ERROR: Could not find server. Check your network connection")
    except ValueError:
        print("ERROR: You must specify a search term.")
    except Exception as x:
        print(type(x))
        print("Oh that didn't work: {}".format(x))

if __name__ == '__main__':
    main()
```
Now we can really tell the user what's going on.

```
Keyword of title search:   # in case you hit Enter
ERROR: You must specify a search term.

```

The final important thing to see here is the order in which we specify the errors. It's super important that this goes from most specific to most general.


### Concepts: Error handling and exceptions

![alt=text](pics/pic01.png)


Python has kind of an optimistic way of handling errors in compare to for example C. 
One of the key differentiators of professional programs and scripts thrown together by beginners is that the pro app does not crash. It anticipates all the error conditions and puts the proper error handling and user feedback to keep working. 
Ok, pro apps still crash, but they do so much less often. When they do, we have [logging](https://logbook.readthedocs.io) and other error monitoring such as [Rollbar](https://rollbar.com/?dr) so that we can get notified and fix these once we encounter them. This allows apps to grow stronger and more resilient over time.

