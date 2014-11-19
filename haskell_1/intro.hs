-- Run: ghci <file name>.hs (implicitly compiled)
-- Strongly typed.

-- Binding
test_value = 3
-- Error:
-- test_value = 5. Values are immutable

-- Functions --
-- Definition: <name> <args> = <body> (name begins with a lower-case letter)
-- :type mult -- <name>:: Type constraints => arg1 type -> ... -> argN type -> result type
mult x y = x * y
mult' = \ x y -> x * y -- via lambda.

-- Function as a param
apply2 f x y = f x y

-- Function call: <name> <args>
-- Error:  mult mult 13 4 5. Means "call mult with 4 args"
fuct_test = mult (mult 2 3) 5

-- Infix call
mult_inner_call_result = 5 `mult` 6

-- Type of "mult 3" ? (:type mult 3) (C-c C-t)
mult3 = mult 3

-- Welcome curring -- convert function of multiple args to function of single arg
mult'' = \ x -> \ y -> x * y -- explicit carring

--   Lazy args evaluation:
first' x y = x
lazy_test = first' 1 (0 / 0)

-- Factiorial (lazy execution -- thunk) --
fact n = if n > 0 then n * fact(n - 1) else 1

-- Welcome guards
fact' n | n == 0    = 1
        | otherwise = n * fact' (n - 1)

-- TCO-friendly version
fact'' n = fact''_hlpr 1 n
fact''_hlpr acc n = if n > 1 then fact''_hlpr (acc * n) (n - 1) else acc

-- Welcome "where" -- defines local binging
fact''' n = fact_hlpr init n
  where fact_hlpr a n = if n > 1 then fact''_hlpr (a * n) (n - 1) else a
        init = fact_hlpr 1 1

-- Basic
-- Bool, Char, [<Type>] -- list of <Type> (homogeneous), Int (fixed)/Integer (transparent transition), String

-- Q: What is type (in C++, Python, Java)?
-- Example of possible definition:
-- MyBool -- type ctor; MyTrue, MyFalse -- data ctors
data MyBool = MyTrue | MyFalse
-- Actual: ":info <type name>" (C-c C-i). Discuss [] (example from Lisp?)
        
and' False _ = False
and' True x = x

-- Lists: [1, 2, 3] === 1 : 2 : 3 : []
-- prepend elem --  x : list
-- concat -- list1 ++ list2
-- Common list functions -- your next task.

-- Welcome pattern matching -- picked implementation depends on args values
-- (<Data ctor> <values>)
-- NB: case matters!
data Box a = Empty | Value a

unbox Empty = []
unbox (Value val) = [val]

-- List examples
evens [] = []
evens (42 : _) = [42]
evens [x] = [x]
evens (x1 : x2 : xs) = x1 : (evens xs)
-- Updown order (swap 2nd and 3rd to demo)
-- Why [] instead of () in the 3rd?
-- What if we replace the last one with "evens [x1 : x2 : xs] = x1 : (evens xs)"
-- explain xs; turn off some cases and demo function type (example of parametric poly)

dupFst ent@(x : xs) = x : ent

-- Int example
gcd' a 1 = a
gcd' a b = gcd' b (mod a b)

-- Book: Learn You A Haskell for Great Good! -- Miran Lipovaca
