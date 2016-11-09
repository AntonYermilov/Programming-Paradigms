{-# LANGUAGE TupleSections #-}
module Hands where

import           Data.Function
import           Data.List
import           Data.Ord

import           Types

value :: [Card] -> (HandRank, [Card])
value h = maybe ifNotFlush ifFlush (maybeFlush h)
  where ifFlush cs = maybe (Flush, take 5 cs) (StraightFlush,) (maybeStraight cs)
        ifNotFlush = maybe (checkGroups h) (Straight,) (maybeStraight h)

maybeFlush :: [Card] -> Maybe [Card]
maybeFlush cs = undefined

maybeStraight :: [Card] -> Maybe [Card]
maybeStraight cs = if length cs'' >= 5 then Just (lastN 5 cs'') else maybeWheel cs'
  where cs' = nubBy ((==) `on` rank) cs
        cs'' = head $ sortByLength $ groupBySucc $ sort cs'

maybeWheel :: [Card] -> Maybe [Card]
maybeWheel cs = if length cs' == 5 then Just cs' else Nothing
  where cs' = filter (flip elem [Ace, Two, Three, Four, Five] . rank) cs

checkGroups :: [Card] -> (HandRank, [Card])
checkGroups h = (hr, cs)
  where gs = sortByLength $ groupBy ((==) `on` rank) $ sort h
        cs = take 5 $ concat gs
        hr = case map length gs of
                  (4:_)    -> Quads
                  (3:2:_)  -> FullHouse
                  (3:_)    -> Trips
                  (2:2:_)  -> TwoPair
                  (2:_)    -> Pair
                  _        -> HighCard

groupBySucc :: [Card] -> [[Card]]
groupBySucc = foldr f []
  where f a [] = [[a]]
        f a xs@(x:xs') = if succ (rank a) == rank (head x)
                         then (a:x):xs'
                         else [a]:xs

sortByLength :: Ord a => [[a]] -> [[a]]
sortByLength = reverse . sortBy (comparing length)

lastN :: Int -> [a] -> [a]
lastN n xs = drop (length xs - n) xs
