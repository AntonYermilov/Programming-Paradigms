# Testing

## Unit-testing
* one tiny bit of functionality
* documentation
* catch regressions
* mocks
* tox https://tox.readthedocs.io/en/latest/


## Code metrics

### Code coverage
sudo pip install coverage
coverage run file.py
coverage html -d coverage_html
xdg-open coverage_html/index.html
* exceptions
* corner cases

### Cyclomatic complexity
![Cyclomatic complexity](http://risovach.ru/upload/2014/10/mem/muzhik-bleat_63373490_orig_.jpg "Cyclomatic complexity")
* codeclimate.com


## Functional testing
* correctness
* stability
* UI testing (Selenium)
* profiling
    * cProfile
    * timeit
    * pycallgraph graphviz --
    * memory_profiler
    * callgrind

## Continuous integration
* https://github.com/integrations
* https://shields.io/ fancy badges
* travis, appveyor
* example https://github.com/ordian/pydirectio
