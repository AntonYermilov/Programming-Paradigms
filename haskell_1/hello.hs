module Main where
import Data.Char (digitToInt, ord)

x = 2               -- глобальное связывание
y = 42

add :: Int -> Int -> Int
add x y = x + y         -- определение add
add' x = \ y -> x + y
add''  = \ x y -> x + y

foo = let z = x + y -- глобальное (foo) локальное (z)
          s = z * z
      in print s    -- отступ (layout rule)

fortyTwo = add 40 2     -- вызов add


--oops = print add 1 2
printThree = print (add 1 2)


z = 1         -- ok, связали
-- z = 2         -- ошибка
q q = \ q -> q -- ok, но...

factorial n = if n > 1
              then n * factorial (n-1)
              else 1

-- where
factorial'' n' = helper 1 n'
   where helper acc n = if n > 1
                        then helper (acc * n) (n - 1)
                        else acc

-- let in
factorial''' n' =
   let helper acc n = if n > 1
                      then helper (acc * n) (n - 1)
                      else acc
   in helper 1 n'

-- guard
factorial''''    :: Integer -> Integer
factorial'''' n' = helper 1 n'
    where helper acc n | n > 1 = helper (acc * n) (n - 1)
                       | otherwise = acc


--factorial' n = helper 1 n
--helper acc n = if n > 1
--               then (helper $! acc * n) (n - 1) -- helper (acc * n) (n - 1)
--               else acc

-- :t mult
mult x1 x2 = x1 * x2

--int gcd(int a, int b) {
--  while (b) {
--    int tmp = a;
--    a = b;
--    b = tmp % b
--  }
--  return a;
--}


--int gcd(int a, int b) {
--    return b == 0 ? a : gcd(b, a % b);
--}

-- pattern matching
gcd' a 0 = a
gcd' a b = gcd' b (mod a b)

listCons = (1::Int):2:3:[] == [1,2,3]

whoami [] = []
whoami [x] = [x]
whoami (x : _ : xs) = x : (whoami xs)

--list comprehensions
evens xs = [x | x <- xs, x `mod` 2 == 0]

-- lazy
k = \ x y -> x
lazyWow = print $ k 42 undefined

-- 2a. Написать функцию, возвращающую количество цифр числа.
--     Для целочисленного деления можете использовать функции div и mod.
toDigits :: Int -> [Int]
-- toDigits = reverse . helper'
--   where helper' 0 = [0]
--         helper' a = helper (abs a)
--         helper 0 = []
--         helper a = (a `mod` 10) : helper (a `div` 10)
toDigits = map digitToInt . show

numberOfDigits :: Int -> Int
numberOfDigits = length . toDigits

-- 2b. Написать функцию, возвращающую сумму цифр числа.
sumOfDigits :: Int -> Int
sumOfDigits = sum . toDigits

-- operator
f --> a = f a
infixl 5 -->


index :: Int -> [Int] -> Int
index k l = let
  helper [] _ = -1
  helper (x:xs) i | x == k = i
                  | otherwise = helper xs (i + 1)
  in helper l 0

-- Determine if list l is a palindrome
isPalindrome l = undefined

{-
 - Duplicate the elements in list xs, for example "duplicate [1,2,3]" would give the list [1,1,2,2,3,3]
 - Hint: The "concat [l]" function flattens a list of lists into a single list.
 - (You can see the function definition by typing ":t concat" into the interpreter. Perhaps try this with other variables and functions)
 -
 - For example: concat [[1,2,3],[3,4,5]] returns [1,2,3,3,4,5]
 -}
duplicate xs = undefined

{-
 - Imitate the functinality of zip
 - The function "min x y" returns the lower of values x and y
 - For example "ziplike [1,2,3] ['a', 'b', 'c', 'd']" returns [(1,'a'), (2, 'b'), (3, 'c')]
 -}
ziplike xs ys = undefined

-- Split a list l at element k into a tuple: The first part up to and including k, the second part after k
-- For example "splitAtIndex 3 [1,1,1,2,2,2]" returns ([1,1,1],[2,2,2])
splitAtIndex k l = undefined

-- Insert element x in list l at index k
-- For example, "insertElem 2 5 [0,0,0,0,0,0]" returns [0,0,0,0,0,2,0]
insertElem x k l = undefined

-- Rotate list l n places left.
-- For example, "rotate 2 [1,2,3,4,5]" gives [3,4,5,1,2]
rotate n l = undefined

main = do
  printThree
  print (factorial'''' 5)
  lazyWow
  print listCons
  print --> 10 + ord 'f' - ord 'a'
  putStrLn "hello, haskell"
