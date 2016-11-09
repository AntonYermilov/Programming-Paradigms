module Nullable where

import Prelude hiding (Maybe, Just, Nothing, Either, Left, Right)

data Maybe a = Nothing | Just a deriving (Show)

{-
instance (Show a) => Show (Maybe a) where
  show (Just x) = "Just " ++ show x
  show Nothing  = "Nothing"
 -}

fromMaybe :: a -> Maybe a -> a
fromMaybe defval wrapped =
  case wrapped of
    Nothing    -> defval
    Just value -> value

data Either a b = Left a | Right b
