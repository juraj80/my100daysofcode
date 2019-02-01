### Logging

You'll need to install [Logbook](https://logbook.readthedocs.io/en/stable/).

In your fresh Python3 virtual environment:

`pip install logbook`

Then you have to register the logging. Recall, this looks something like:

```python
import logbook
level = logbook.TRACE
log_filename = ...

if not log_filename:
    logbook.StreamHandler(sys.stdout, level=level).push_application()
else:
    logbook.TimedRotatingFileHandler(log_filename, level=level).push_application()
   
```

Then to log something, you create a logbook instance like this:

```python
app_log = logbook.Logger('App')
# ...
app_log.notice("some message")

# actions are:
# notice / info / trace / warn / error / critical
```

Once you've got your app logging (either to the console or a file) and saving what you think is important, you're done!


### Step By Step Guide:

There are two steps in configuring logging:

One, we have to globally configure how we want to log things. 
Do we want our log messages to go to just standard out, so the terminal or console?
Do we want the to go to a file, if it's a file do you want that file based on a date and roll as the days change, or do you want that to just be one big file?
Or do you want to send that somewhere crazy like email or desktop notifications.

so we're going to configure logging and then we're just going to add the log actions as a separate way.

First we define `init_logging(filename: str = None)` function in our program file, where we can pass the filename or give it a default value of None.
In the function we need to set the level first. There's like a hierarchy of levels in logging, there is like TRACE, which is just super-verbose stuff, then 
there is ERROR, which we almost never want to skip.
```python
def init_logging(filename: str = None):
    level = logbook.TRACE
```

Then if there is a filename we choose a type of handler which we want to use. In our case we want to have TimedRotatingFileHandler, which takes a couple of things.
We have to give it the filename, level and date_format. In our case default date_format is ok. That will create handler and then we would just add `push_application()`
That means every action we do with logging is going to use this underlying system. If it's not the case we're going to say, `logbook.StreamHandler()` and we give it the stream
`sys.stdout` to print the logs in the terminal.


```python
def init_logging(filename: str = None):
    level = logbook.TRACE

    if filename:
        logbook.TimedRotatingFileHandler(filename, level=level).push_application()
    else:
        logbook.StreamHandler(sys.stdout, level=level).push_application()
```

But before we get on, let's make our first log message that says here's how we've configured logging.

```python

 msg = 'Logging initialized, level: {}, mode: {}'.format(
        level,
        "stdout mode" if not filename else 'file mode: ' + filename
    )
```

And we can create one of these logs with `logbook.Logger`. So we'll have this little startup logger:

```python
logger = logbook.Logger('Startup')
logger.notice(msg)

```

If we run our program file the first time without specified filename it will stdout the msg and we'll see that we've got everything working.

```
[2019-02-01 19:53:23.977242] NOTICE: Startup: Logging initialized, level: 9, mode: stdout mode
Keyword of title search: 
```

### Writing the log message