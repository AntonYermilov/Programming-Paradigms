module Hello where
import Data.Char (digitToInt, ord)

x = 2               -- глобальное связывание
y = 42

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

listCons :: Bool
listCons = (1::Int):2:3:[] == [1,2,3]

whoami [] = []
whoami [x] = [x]
whoami (x : _ : xs) = x : (whoami xs)

--list comprehensions
evens xs = [x | x <- xs, x `mod` 2 == 0]

-- lazy
k = \ x y -> x
lazyWow = print $ k 42 undefined

-- 1. fib n вовзращает n-ое число Фибоначчи
fib :: Integer -> Integer
fib n = undefined

-- 2a. Написать функцию, возвращающую количество цифр числа.
--     Для целочисленного деления можете использовать функции div и mod.
numberOfDigits :: Integer -> Int
numberOfDigits = undefined

-- 2b. Написать функцию, возвращающую сумму цифр числа.
sumOfDigits :: Integer -> Integer
sumOfDigits = undefined

-- operator
f --> a = f a
infixl 5 -->

main = do
  printThree
  print (factorial'''' 5)
  lazyWow
  print listCons
  print --> 10 + ord 'f' - ord 'a'
  putStrLn "hello, haskell"
