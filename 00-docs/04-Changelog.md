# Changelog
> Change History

## MVP - v0.1

### v0.0.2
- Creation of CSV functions:
    - Route to import `CSV` data and insert it into the database
        - Read the `CSV` file into a `DataFrame`
        - Convert `"Categorias"` text values into `subcategory_id`
        - Convert the `DataFrame` into `Pydantic` models
        - Insert the validated `Pydantic` models into the database
- Creation of Route and function to delete all Bills

### v0.0.1
- Creation of routes for CRUD of:
    - Bills
    - Account
    - Category
    - Subcategory
- Creation of Pydantic schemas
    - Bills
    - Account
    - Category
    - Subcategory
- Creation of SQLAlchemy models
    - Bills
    - Account
    - Category
    - Subcategory
- Initializing `docker-compose`
- Creation of `/init` with SQL code
