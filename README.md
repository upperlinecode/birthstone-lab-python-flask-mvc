# Flask Birthstone Lab

The goal of this lab is to create a web application that takes in a user's birth month, and outputs their birthstone. For example, someone born in December should be told that their birthstone is Turquoise or Topaz (depending on which chart you use).

<img src='https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcQ4CS7kQxoMYpy-vXqy_kH9SLDDba96bCVJCw&usqp=CAU'>

Some of the styling has been done for you, but the rest of the application needs to be created in `model.py`, `routes.py`, `index.html`, and `results.html`.

Don't forget to preview and test your application as you work!

## Bonus Challenges

**1.** Style the results page so it matches the index.

**2.** Make the results page output a picture and a description of the gemstone in addition to the name of the birthstone.

**3.** Create an "About" page with similar styling and link it to the index.

**4.** Make your own web application (remember, it must take input and output manipulated data).

## Quick Setup:

Code to make sure your application hot-reloads on file saves:
```bash
export FLASK_DEBUG=1
```

If you get character set errors, use these two additional lines:
```bash
export LC_ALL=en_US.utf-8
export LANG=en_US.utf-8
```

Code to run flask:
```bash
flask run
```
