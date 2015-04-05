`Flask` is a microframework for `Python`. You install `Flask` using `pip` package manager:

    pip install flask
    

<!--more-->

We will use `Flask` to build a simple webapp that contains a `text input`, inside of which the user will type an arithmetic `expression` (ex: `3 + 5`). This `expression` will be evaluated (calculated), and the `result` is shown to the user.

`Flask` scripts are run like any normal `python` script using `python <script.py>`. The webapp will be accessible on port `5000` in localhost. You could go in your browser to `localhost:5000` to visualize it once you have run it.

-- We start our webapp script code by importing from the `flask` module, the `Flask` class and the `request` context object that we are going to need later:

    from flask import Flask, request 
    

-- The `app` object is instantiated from the `Flask` class, by providing the name of the module (script) as a first parameter:

    app = Flask(__main__)
    

-- `Routes` are defined using the `route()` decorator to tell `Flask` what URL should trigger our function. In our case, we have a unique route `/` which triggers the `index()` function, and this `route` accepts `GET` and `POST` requests:

    @app.route('/', methods=['GET', 'POST'])
    def index():
    

This `index()` function will have two blocks depending on the request type: `GET` or `POST`.

-- If the request is of type `GET`, we simply show an html `form` which contains a `text input` named `expression` and a `submit button`:

    if request.method == 'GET':
    return '''
        <form method="post">
            <input type="text" name="expression" />
            <input type="submit" value="Calculate" />
        </form>
    '''
    

-- If the function receive a `POST` which means that the `form` has been submitted, we retrieve the value filled inside the `expression` input using `request.form` object. After that, we evaluate the `expression` submitted using built-in `eval()` function and we print it in the browser:

    elif request.method == 'POST':
        expression = request.form.get('expression')
        result = eval(expression)
        return 'result: %s' % result
    

**Important**: `eval()` function interprets string as a `python` code. A user can pass a malicious `python` code that will be executed by `eval()`. It has been used in this example just to make it brief, and it should not be used in a real application to avoid code-injection inside your application.

-- If our script is executed and not being imported as a `module` in another script, we run our `app`. The `debug` parameter is set to `True`, to reload the server on code changes and provide us with helpful debugger messages:

    if __name__ == '__main__':
        app.run(debug=True)
    

The full source code: <a href="https://github.com/h4k1m0u/pythonbeginner.org/blob/master/examples/python-flask-web-calculator.py" target="_blank">Python Flask Web Calculator on Github</a>
