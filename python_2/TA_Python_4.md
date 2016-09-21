## Questions
* slice[None:]
* help(module)
* exceptions recap
* regex recap
* bool(None)
* list keywords
* return None

## HW1 pitfalls
* DRY
* remove the first element form list
* close file
* read whole file

## itertools?
* chain, takewhile, compress, dropwhile, filterfalse, islice,
* groupby, starmap, product, combinations, ...

## anaconda
* https://www.continuum.io/downloads
* conda install vs pip install

## ipython
* ? ! quickref
* lsmagic, timeit

## numpy
* why in c?

| Access                             | Time           |                             Relative |
|------------------------------------|---------------:|--------------------------------------|
| L1 cache reference                 |         0.5 ns |                                      |
| Branch mispredict                  |           5 ns |                                      |
| L2 cache reference                 |           7 ns | 14x L1 cache                         |
| Mutex lock/unlock                  |          25 ns |                                      |
| Main memory reference              |         100 ns | 20x L2 cache, 200x L1 cache          |
| Send 1K bytes over 1 Gbps network  |      10,000 ns |   0.01 ms                            |
| Read 1 MB sequentially from memory |     250,000 ns |   0.25 ms                            |
| Read 1 MB sequentially from SSD    |   1,000,000 ns |   1    ms  4X memory                 |
| Read 1 MB sequentially from disk   |  20,000,000 ns |   20   ms  80x memory, 20X SSD       |
| Send packet RU->USA->RU            | 150,000,000 ns |   150  ms                            |
| Human blink                        | 300,000,000 ns |   300  ms                            |

* doc: http://docs.scipy.org/doc/numpy/reference/
* tutorial: http://cs231n.github.io/python-numpy-tutorial/#numpy
* ndarray
* shapes
* types
* slicing
* ufunc
* examples: softmax, fib


## Strassen
* http://www.stoimen.com/blog/wp-content/uploads/2012/11/7.-Strassens-Algorithm.png

Q: Why programming is hard?
 * Main goal: Fight with structural complexity --> Functions --> Objects (data + functions)

# Objects
"I invented the term object-oriented, and I can tell you that C++ wasn't what I had in mind"
  Alan Key

## OOP Terminology
* Class
* Object
* Instance
* Instantiation
* Class variable
* Instance variable
* Method
* Method overloading
* Operator overloading
* Inheritance

1. EverythingIsAnObject
2. type(obj)
3. isinstance


### Practice
* assignment == aliasing
* class -- as namespace with entities
* def method(self, *args) (self just a convention)
* x.f() is exactly equivalent to MyClass.f(x)
* static vs non-static
* data attr overrides method name
* _name is "treated" as protected
* name mangling __blha --> _classname__blha (to prevent name clash during inheritance)
* __str__ -- toString

* Example: iterator (case study)
	* docstring
	* self
	* __init__ -- ctor
	*  vars: self.<name>
	* __iter__
	* __next__ --> StopIteration # itertools


# Homework

![alt text](http://memecrunch.com/meme/1J8V/deadline-is-coming/image.jpg?w=400&c=1 "Deadline is coming")
