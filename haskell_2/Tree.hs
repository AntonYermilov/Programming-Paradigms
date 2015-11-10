module Tree where

data Tree a = Empty | Node a (Tree a) (Tree a) deriving (Show)

instance Foldable Tree where
  foldr _ ini Empty        = ini
  foldr f ini (Node a l r) = foldr f (f a (foldr f ini r)) l

sumTree :: (Num a) => Tree a -> a
sumTree = foldr (+) 0

sizeTree :: Tree a -> Int
sizeTree = foldr (\ _ y -> 1 + y) 0
