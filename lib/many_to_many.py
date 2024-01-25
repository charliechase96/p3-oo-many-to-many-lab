class Author:
    all = []

    def __init__(self, name):
        self._name = name
        self._contracts = []
        Author.all.append(self)

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        if isinstance(value, str):
            self._name = value
        else:
            raise Exception("Name must be a string.")

    def contracts(self):
        return self._contracts
    
    def books(self):
        return [contract.book for contract in self._contracts]

    def sign_contract(self, book, date, royalties):
        contract = Contract(self, book, date, royalties)
        self._contracts.append(contract)
        book._contracts.append(contract)
        return contract
    
    def total_royalties(self):
        return sum(contract.royalties for contract in self._contracts)
    
    @classmethod
    def all_authors(cls):
        return cls.all


class Book:
    all = []

    def __init__(self, title):
        self._title = title
        self._contracts = []
        Book.all.append(self)

    @property
    def title(self):
        return self._title
    
    @title.setter
    def title(self, value):
        if isinstance(value, str):
            self._title = value
        else:
            raise Exception("Title must be a string.")
        
    def contracts(self):
        return self._contracts
    
    def authors(self):
        return [contract.author for contract in self._contracts]
    
    @classmethod
    def all_books(cls):
        return cls.all
    

class Contract:
    all = []

    def __init__(self, author, book, date, royalties):
        if not isinstance(author, Author):
            raise Exception("Author must be an Author instance.")
        if not isinstance(book, Book):
            raise Exception("Book must be a Book instance.")
        if not isinstance(date, str):
            raise Exception("Date must be a string.")
        if not isinstance(royalties, int):
            raise Exception("Royalties must be an integer.")

        
        self._author = author
        self._book = book
        self._date = date
        self._royalties = royalties

        author._contracts.append(self)
        book._contracts.append(self)
        
        Contract.all.append(self)

    @property
    def author(self):
        return self._author
    
    @property
    def book(self):
        return self._book
    
    @property
    def date(self):
        return self._date
    
    @property
    def royalties(self):
        return self._royalties
        
    @classmethod
    def contracts_by_date(cls, date):
        return [contract for contract in cls.all if contract.date == date]
    
    @classmethod
    def all_contracts(cls):
        return cls.all