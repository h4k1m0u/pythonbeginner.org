`wxPython` is a wrapper for the C++ `GUI` API wxWidgets. It is an alternative to PyGTK, PyQt (PySide), and seems to be easier to me. In this tutorial, we will code a very basic window (or `frame`) containing a unique `button`, and when clicking on this `button`, a `message box` is shown.

<!--more-->

-- We start by importing the `wx` module which contain the `GUI` components needed in our example (`frame`, `panel`, `button`, `messagebox`):

    import wx
    

-- Next, we define the `MyFrame` class which represents our window. This class inherits from `wx.Frame`.

    class MyFrame(wx.Frame):
    

-- The `MyFrame` class has a constructor `__init__(self, parent)` in which we will add our `GUI` components (`button` in our case) to the `frame`. To avoid having the `button` filling all `frame` space, we will add a `panel` to the `frame`, and that `panel` will contain the `button`:

    def __init__(self, parent):
        wx.Frame.__init__(self, parent)
    
        panel = wx.Panel(self)
        button = wx.Button(panel, label="Show the MessageBox")
    

**Note:** The first parameter in `wx.Panel()` (resp. `wx.Button()`) constructors, represent the parent of the component; i.e: `self` or `MyClass` (resp. `panel`).

-- After that, we bind the click on the `button` to a `listener` function `OnClick`, that we will define inside the same class `MyFrame`:

    button.Bind(wx.EVT_BUTTON, self.OnClick)
    

-- The last line in the `MyFrame`'s constructor will show the window (`frame`):

    self.Show()
    

-- Inside the same `MyFrame` class, we add the `OnClick` function listener. This function will just show a `MessageBox` whose the `message` and `title` are given as parameters:

    def OnClick(self, event):
        wx.MessageBox("The button has been clicked", "Title")
    

-- At the end of the script and outside the class previously defined, the `MyFrame` class is instantiated and the `app`'s main loop is created:

    app = wx.App()
    MyFrame(None)
    app.MainLoop()
    

The full source code: <a href="https://github.com/h4k1m0u/pythonbeginner.org/blob/master/examples/python-wxpython-first-application.py" target="_blank">Python wxPython First Application on Github</a>
