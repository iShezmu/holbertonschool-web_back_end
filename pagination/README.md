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

*   2-hypermedia_pagination.py
    - Replicate code from the previous task.
      - Implement a `get_hyper` method that takes the same arguments (and defaults) as `get_page` and returns a dictionary containing the following key-value pairs:
        - `page_size`: the length of the returned dataset page
        - `page`: the current page number
        - `data`: the dataset page (equivalent to return from previous task)
        - `next_page`: number of the next page, None if no next page
        - `prev_page`: number of the previous page, None if no previous page
        - `total_pages`: the total number of pages in the dataset as an integer
      - Make sure to reuse `get_page` in your implementation.
      - You can use the `math` module if necessary.
