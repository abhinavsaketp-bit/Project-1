books=['Diary of the wimpy kid','harry potter','charlie', 'documentary']
book_count=[10,8,5,0]

library={book:count for book,count in zip(books,book_count)}
print("This is the book library", library)

books_in_stock=[book for book in books if library[book]>0]
print("Books in stock", books_in_stock)

chosen_book=input("Enter a book you want to borrow: ")
if chosen_book not in library or library[chosen_book]==0:
    print("Book not in stock!")
    exit()


