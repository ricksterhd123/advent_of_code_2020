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

-- replace :: Char -> Char -> String -> String
-- replace a b x = map (\y -> if y == a || y == b then (if y == a then b else a) else y) x

split :: Char -> String -> [String]
split d x = splitl d x []

-- Find pairs of integers from list a whose sum makes n
f :: Integer -> [Integer] -> [Integer]
f n a = filter (\x -> length (filter (\y -> x + y == n) (a \\ [x])) == 1) a

-- type Set a = [a]

-- powerset :: Set a -> Set (Set a)
-- powerset [] = [[]]
-- powerset (x:xs) = [x:ps | ps <- powerset xs] ++ powerset xs
-- Find group of three integers from list a that makes n

-- f number groupSize list = head $ filter (\y -> sum y == number) $ filter (\x -> length x == groupSize) $ powerset list
-- f' :: Integer -> [Integer] -> [Integer]
-- f' n a = filter (\x -> foldl (+) x (a \\ [x]) == n) a

-- combinations k ns = filter ((k==).length) $ subsequences ns

-- filterLength3 = foldr (\x rs -> if (length x) == 3 then x : rs else rs) [] 

main = do x <- readFile "day_01.txt"
          print $ foldl (*) 1 $ f 2020 $ map readInteger $ split '\n' x


readInteger :: String -> Integer
readInteger = read