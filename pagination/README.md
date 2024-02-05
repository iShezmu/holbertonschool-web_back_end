# Project: Pagination

*   0-simple_helper_function.py
    - Write a function named `index_range` that takes two integer arguments `page` and `page_size`.
      - The function should return a tuple of size two containing a start index and an end index corresponding to the range of indexes to return in a list for those particular pagination parameters.

*   1-simple_pagination.py
    - Implement a method named `get_page` that takes two integer arguments `page` with default value 1 and `page_size` with default value 10.
      - You have to use a CSV file
      - Use `assert` to verify that both arguments are integers greater than 0.
      - Use `index_range` to find the correct indexes to paginate the dataset correctly and return the appropriate page of the dataset (i.e. the correct list of rows).
      - If the input arguments are out of range for the dataset, an empty list should be returned.
