-- Solves part A of the problem
import Data.List

-- input
numbers :: [Integer]
numbers = [1721, 979, 366, 299, 675, 1456]

-- Split string with delimiter
splitl :: Char -> String -> String -> [String]
splitl _ [] _ = []
splitl d (x:xs) r
    | length xs == 0 = (r ++ [x]) : (splitl d xs [])
    | x /= d = splitl d xs (r ++ [x])
    | otherwise = r : (splitl d xs [])

split :: Char -> String -> [String]
split d x = splitl d x []

-- Find pairs of integers from list a whose sum makes n
f :: Integer -> [Integer] -> [Integer]
f n a = filter (\x -> length (filter (\y -> x + y == n) (a \\ [x])) == 1) a

main = do x <- readFile "day_01.txt"
          print $ foldl (*) 1 $ f 2020 $ map readInteger $ split '\n' x


readInteger :: String -> Integer
readInteger = read