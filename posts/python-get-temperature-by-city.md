We are going to use `weather` data retrieved from <a href="" target="_blank">OpenWeatherMap</a> in `json` format.

<!--more-->

The following built-in modules will be needed:

*   **sys**: To get command line arguments.
*   **urllib2**: To download a webpage content by `url`.
*   **json**: To convert a `json` object to a `dictionary`.

-- First, we verify that a `city` has been provided as a command line argument. The script is exited if no `city` is given, otherwise we will save the `city` name in a variable:

    if len(sys.argv) > 1:
        country = sys.argv[1]
    else:
        print 'No city given.'
        exit()
    

-- Then, we read the `json` `weather` data for the given `city`, returned from `openweathermap.org` into a file object:

    fp = urllib2.urlopen('http://api.openweathermap.org/data/2.5/weather?units=metric&mode=json&q=' + country)
    

-- Next, we parse the `json` file object's content using `json.load()` function, which will convert the `json` data to a python `dictionary`:

    data = json.load(fp)
    

-- Having finished with the `json` file object, we can close it:

    fp.close()
    

-- At the end, we print the `temperature` which can be extracted from the `dictionary` of `weather` data retrieved earlier:

    print "Temperature in %s: %d" % (country, data['main']['temp'])
    

The full source code: <a href="https://github.com/h4k1m0u/pythonbeginner.org/blob/master/examples/python-get-temperature-by-city.py" target="_blank">Python Get Temperature by City on Github</a>
