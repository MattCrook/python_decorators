'''
class Queries:

    def customers(self):
        return """SELECT * FROM Customer
            ORDER BY last_name ASC, first_name ASC
        """

    def coffins(self):
        return "SELECT * FROM Product"

    def employees(self):
        return """SELECT * FROM Employee
            ORDER BY last_name ASC, first_name ASC
        """

    def gravestones(self):
        return "SELECT * FROM GraveStones"

    def deceased(self):
        return """SELECT * FROM Deceased
            ORDER BY last_name ASC, first_name ASC
        """

    def obelisks(self):
        return "SELECT * FROM Obelisk"

    def vendors(self):
        return """SELECT * FROM Vendor
            ORDER BY last_name ASC, first_name ASC
        """
'''

# refactor to add decorator to extract duplicated "ORDER BY" code on appropriate properties.
class Queries:

    def sort_by_name(class_property):
        def func_wrapper(*args, **kwargs):
            original_method = class_property(*args, **kwargs)
            return f"{''.join(original_method)} ORDER BY last_name ASC, first_name ASC"
        return func_wrapper

    @sort_by_name
    def customers(self):
        return "SELECT * FROM Customer"

    def coffins(self):
        return "SELECT * FROM Coffin"

    @sort_by_name
    def employees(self):
        return "SELECT * FROM Employee"

    def gravestones(self):
        return "SELECT * FROM GraveStones"

    @sort_by_name
    def deceased(self):
        return "SELECT * FROM Deceased"

    def obelisks(self):
        return "SELECT * FROM Obelisk"

    @sort_by_name
    def vendors(self):
        return "SELECT * FROM Vendor"



queries = Queries()

print(queries.customers())
print(queries.coffins())
print(queries.employees())

# Output
# SELECT * FROM Customer ORDER BY last_name ASC, first_name ASC
# SELECT * FROM Coffin
# SELECT * FROM Employee ORDER BY last_name ASC, first_name ASC
