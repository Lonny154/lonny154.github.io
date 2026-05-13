from db import get_connection


def print_rows(rows, columns):
    """
    Helper function to print query results in a readable format.
    """
    if not rows:
        print("\nNo results found.\n")
        return

    print()
    print(" | ".join(columns))
    print("-" * 100)

    for row in rows:
        print(" | ".join(str(value) if value is not None else "NULL" for value in row))

    print()


def get_customer_address():
    customer_id = input("Enter customer ID: ")

    query = """
        SELECT 
            c.customer_id,
            c.first_name,
            c.last_name,
            c.email,
            a.address,
            a.district,
            a.postal_code,
            ci.city,
            co.country
        FROM customer c
        JOIN address a 
            ON c.address_id = a.address_id
        JOIN city ci 
            ON a.city_id = ci.city_id
        JOIN country co 
            ON ci.country_id = co.country_id
        WHERE c.customer_id = %s;
    """

    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute(query, (customer_id,))
            rows = cur.fetchall()
            columns = [desc[0] for desc in cur.description]
            print_rows(rows, columns)


def get_customer_rental_history():
    customer_id = input("Enter customer ID: ")

    query = """
        SELECT 
            c.customer_id,
            c.first_name,
            c.last_name,
            f.title,
            f.rating,
            f.rental_rate,
            r.rental_date,
            r.return_date
        FROM customer c
        JOIN rental r 
            ON c.customer_id = r.customer_id
        JOIN inventory i 
            ON r.inventory_id = i.inventory_id
        JOIN film f 
            ON i.film_id = f.film_id
        WHERE c.customer_id = %s
        ORDER BY r.rental_date DESC;
    """

    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute(query, (customer_id,))
            rows = cur.fetchall()
            columns = [desc[0] for desc in cur.description]
            print_rows(rows, columns)


def get_unreturned_films_by_customer():
    customer_id = input("Enter customer ID: ")

    query = """
        SELECT 
            c.customer_id,
            c.first_name,
            c.last_name,
            f.title,
            r.rental_date,
            r.return_date
        FROM customer c
        JOIN rental r 
            ON c.customer_id = r.customer_id
        JOIN inventory i 
            ON r.inventory_id = i.inventory_id
        JOIN film f 
            ON i.film_id = f.film_id
        WHERE c.customer_id = %s
          AND r.return_date IS NULL
        ORDER BY r.rental_date;
    """

    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute(query, (customer_id,))
            rows = cur.fetchall()
            columns = [desc[0] for desc in cur.description]
            if not rows:
                print("\nThis customer has no unreturned films.\n")
            else:
                print_rows(rows, columns)


def get_all_films_with_categories():
    query = """
        SELECT 
            f.film_id,
            f.title,
            f.description,
            f.length,
            f.rental_rate,
            f.rating,
            cat.name AS category
        FROM film f
        JOIN film_category fc 
            ON f.film_id = fc.film_id
        JOIN category cat 
            ON fc.category_id = cat.category_id
        ORDER BY f.title
        LIMIT 50;
    """

    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute(query)
            rows = cur.fetchall()
            columns = [desc[0] for desc in cur.description]
            print_rows(rows, columns)


def get_sales_by_category():
    query = """
        SELECT 
            cat.name AS category,
            SUM(p.amount) AS total_sales
        FROM payment p
        JOIN rental r 
            ON p.rental_id = r.rental_id
        JOIN inventory i 
            ON r.inventory_id = i.inventory_id
        JOIN film f 
            ON i.film_id = f.film_id
        JOIN film_category fc 
            ON f.film_id = fc.film_id
        JOIN category cat 
            ON fc.category_id = cat.category_id
        GROUP BY cat.name
        ORDER BY total_sales DESC;
    """

    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute(query)
            rows = cur.fetchall()
            columns = [desc[0] for desc in cur.description]
            print_rows(rows, columns)


def count_unreturned_films():
    query = """
        SELECT 
            COUNT(*) AS unreturned_films
        FROM rental
        WHERE return_date IS NULL;
    """

    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute(query)
            rows = cur.fetchall()
            columns = [desc[0] for desc in cur.description]
            print_rows(rows, columns)