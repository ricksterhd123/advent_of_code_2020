import Data.List

-- input
numbers :: [Integer]
numbers = [1721, 979, 366, 299, 675, 1456]

-- Split string with delimiter
splitl :: Char -> String -> String -> [String]
splitl _ [] _ = []
splitl d (x:xs) r
    | x /= d && (length xs /= 0) = splitl d xs (r ++ [x])
    | length xs == 0 = (r ++ [x]) : (splitl d xs [])
    | otherwise = r : (splitl d xs [])

-- replace :: Char -> Char -> String -> String
-- replace a b x = map (\y -> if y == a || y == b then (if y == a then b else a) else y) x

split :: Char -> String -> [String]
split d x = splitl d x []

-- Find sum
f :: Integer -> [Integer] -> [Integer]
f n a = filter (\x -> length (filter (\y -> x + y == n) (a \\ [x])) == 1) a

main = do x <- readFile "inputa"
          print $ foldl (*) 1 (f 2020 (map readInteger (split '\n' x)))

readInteger :: String -> Integer
readInteger = read