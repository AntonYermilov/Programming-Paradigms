compute :: (Num a, Read a) => String -> a
compute = head . foldl computeStack [] . words
  where
    computeStack (x:y:ys) "+" = (y + x):ys
    computeStack (x:y:ys) "-" = (y - x):ys
    computeStack (x:y:ys) "*" = (y * x):ys
    computeStack xs number = read number:xs

-- foldl computeStack [] ["1", "2", "-"]
--                    [] "1":"2":"-":[]
--                    (computeStack [] "1") ("2":"-":[])
--                    1:[] ("2":"-":[])
--                    (computeStack 1:[] "2") ("-":[])
--                    (2:1:[]) ("-":[])
--                    (computeStack 2:1:[] "-") []
--                    (1 - 2:[])
-- (-1)


eachLine :: (String -> String) -> (String -> String)
eachLine f = unlines . map f . lines

main = interact $ eachLine $ show . compute
