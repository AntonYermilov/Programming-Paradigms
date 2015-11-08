foldl' :: (a -> b -> a) -> a -> [b] -> a
foldl' _ z []     = z
foldl' f z (x:xs) = foldl' f (f z x) xs

foldr' :: (b -> a -> a) -> a -> [b] -> a
foldr' _ z []     = z
foldr' f z (x:xs) = f x (foldr' f z xs)

reverse' xs = foldl' (flip (:)) [] xs
foldl'' f z xs = foldr' (\x a acc -> a (f acc x)) id xs z

-- simple examples of foldr recursive patterns
sum'     = foldr' (+) 0
product' = foldr' (*) 1
and'     = undefined
or'      = undefined
length'  = undefined
bin2int :: [Int] -> Int
bin2int  = undefined
map' f   = undefined
