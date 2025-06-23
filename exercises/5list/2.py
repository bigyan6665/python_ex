book_list = ["c","c++","dbms","dccn"]
book = input("Enter book to withdraw = ").lower()
if book in book_list:
    book_list.remove(book)
    print(sorted(book_list))
else:
    print(f"Book = {book} , not found ")