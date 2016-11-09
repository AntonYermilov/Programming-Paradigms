module Books where

data BookInfo = Book Int String [String] deriving (Show)
data MagazineInfo = Magazine Int String [String] deriving (Show)

type CustomerID = Int
type ReviewBody = String
data BookReview = BookReview BookInfo CustomerID ReviewBody

type BookRecord = (BookInfo, BookReview)

type CardHolder = String
type CardNumber = String
type Address = [String]


data BillingInfo = CreditCard CardNumber CardHolder Address
                 | CashOnDelivery
                 | Invoice CustomerID
                   deriving (Show)

bookID      (Book id _     _       ) = id
bookTitle   (Book _  title _       ) = title
bookAuthors (Book _  _      authors) = authors

data Customer = Customer {
    customerID      :: CustomerID
  , customerName    :: String
  , customerAddress :: Address
  } deriving (Show, Read)


customer1 :: Customer
customer1 = Customer 271828 "J.R. Hacker"
            ["255 Syntax Ct",
             "Milpitas, CA 95134",
             "USA"]
customer2 :: Customer
customer2 = Customer {
              customerID = 271829
            , customerAddress = ["1048576 Disk Drive",
                              "Milpitas, CA 95134",
                              "USA"]
            , customerName = "Jane Q. Citizen"
            }

onlyOne :: Customer -> Customer
onlyOne x@Customer { customerID = 271828 } = x
-- onlyOne (Human id name address) = show id

-- for fun
type Question   = String
type Answer     = String
type Task       = String
type TaskAnswer = String
type TaskScore  = Float

class Student a where
  question :: a -> Question
  doHomework :: a -> Maybe TaskAnswer

class Teacher a where
  answer :: a -> Question -> Maybe Answer
  checkHomework :: a -> Maybe TaskAnswer -> TaskScore

data Freshman = Freshman { myName :: String, myQuestion :: Question }
data PhdStudent = PhdStudent { phdName :: String }

instance Student Freshman where
  question _ = "why haskell in production?"
  doHomework _ = Nothing

instance Teacher PhdStudent where
  answer _ _ = Nothing
  checkHomework _ Nothing = 0
  checkHomework _ (Just ans) = 0.42 * (fromIntegral . length . words $ ans)
