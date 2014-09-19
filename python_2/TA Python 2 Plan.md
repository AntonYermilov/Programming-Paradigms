# Intro

## Examples
* https://github.com/HFxTA/Programming-Paradigms

## Literature
* Dive Into Python 3.
* http://openbookproject.net/thinkcs/python/english3e/index.html
* https://docs.python.org/3.4/tutorial/
* APTU MD: http://mit.spbau.ru/sewiki/index.php/Unix_и_Скриптовые_языки_2013

## HW
* Cells coloring as notifications (yellow)
* Email with programming.paradigms@osll.ru in CC
* Programming workflow: Write Code --> Review --> Refactoring 
* Programming principles: KISS, DRY
* Consistency matters more than style itself (as soon as style is accepted)
* Писать тесты для функций в  "main"
* Самостоятельное изучение
* Python is good for rapid prototyping/test data generation

#### Python Idioms Sources
* http://python.net/~goodger/projects/pycon/2007/idiomatic/handout.html
* http://safehammad.com/downloads/python-idioms-2014-01-16.pdf
* http://python-3-patterns-idioms-test.readthedocs.org/ (Part 2)
* http://c2.com/cgi/wiki?PythonIdioms

# Функции

## Tuples как способ вернуть 2 значения
* values separated with comma (packing)
* one element tuple ( val, )
* Q: размер в элементах tuple? (A: len)
* tuple unpacking -- lvalues are separated with comma
* immutable! (but tuple elements are mutable)

## Параметры по умолчания
* способ задания необязательных аргументов. Пример: print
* передача параметров по имени. Positional параметры не могут идти после keyword параметров
* default values аre evaluated only once! Пример со списком.
	* Решение: инициализация внутри функции. По умолчанию: None (Ничто).
	* В conditionals -- always False.
	* Q: None == False? (A: False)

## Переменное число параметров (Variadic Args)
* function(pos1, pos2, v1, .., vn, keywords only) <-- function call
* Wrapped as tuple
* Unwrap sequence f(*args)
* Kwargs -- same but dictionary is used. (**kwargs vs *vagrs)
* Order: pos, vargs, kwargs

# Модули

## Common
* useful stuff --> code reuse. E.g. math, dis
* portable way to do something. E.g. os
* fun stuff. E.g. this

## Подключить чужой (Steps)
* symbol tables. Can be nested.
* Module has own symbol table. Allows to prevent clash in func/var names
* Declare: import <module name>
* Use: <module name>.<function name>

## Подключить часть чужого
* from <module_name> import <function>
* from <module_name> import <function1>, <function2>
* names are imported to local symbol table

#### "Import All"
* from <module_name> import * (Bad: namespace pollution)

## Подключить с синонимом
* all previous + as <new_name>

## Get names defined by module
* dir(<module name>) (e.g. dir(__builtins__)
* W/O args -- currently defined names (w/o builtins)
* builtins -- already defined "names", no import/prefix required

## Создать свой
* initialization statements (runs only the first time module name used in import statement)
* definitions

##### oписание "\_\_name__"
* Модули -- "объекты".  Атрибут "\_\_name\_\_"
	* при импорте -- имя модуля;
	* при запуске -- специальное значение "\_\_main\_\_"
* Переменные из командной строки: sys.argv
#### Module name search
* lookup in build-ins
* sys.path --> <module_name>.py
	* input script dir
	* $PYTHONPATH (export PYTHONPATH="blah")
	* platform (os) dependent paths

## Self-Study: Packages

# Обзор модуля os
* portable interface to OS API (POSIX-like).
* os.name -- os family; sys.platform -- higher granularity

### Перечисление содержимого директории
* os.listdir(<dirname>) --> list of file/dir names

### Утилиты для работы с путями: os.path
* https://docs.python.org/3/library/os.path.html
* isdir/isfile/is... -- checks weather path is file/dir/...
* join -- concat paths in portable way (separator)
* getsize -- size of stuff referenced by path (NOTE: dir size is not sum of file sizes)
* walk -- simple way to traverse child path elements

# Описание лабы по дeдупликации

## FS Doc
* https://docs.python.org/3/library/filesys.html
* Use os.path & listdir / walk if possible

## Решение в лоб. Его недостатки

## Хеши
* Props: consistency, same for same objects
* hash() / MD5
#### MD5 example
* moronic, but good hash function design is not what we want from this lab
```python
import hashlib
md5 = hashlib.md5()
md5.update("val".encode("utf-8"))  <-- update concatenates with previous
md5.digest()
```
## Решение с использованием хешей
