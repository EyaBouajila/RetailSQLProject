few_shots = [
    {'Question': "How many t-shirts do we have left for Nike in XS size and white color?",
     'SQLQuery': "SELECT sum(stock_quantity) FROM t_shirts WHERE brand = 'Nike' AND color = 'White' AND size = 'XS'",
     'SQLResult': "Result of the SQL query",
     'Answer': "We have 0 t-shirts left for Nike in extra small size and white color."},

    {'Question': "How many t-shirts do we have left for Adidas in extra small size and red color?",
     'SQLQuery': "SELECT COUNT(*) FROM t_shirts WHERE brand = 'Adidas' AND size = 'XS' AND color = 'Red' LIMIT 1;",
     'SQLResult': "Result of the SQL query",
     'Answer': "We have 1 t-shirt."},

    {
        'Question': "If we have to sell all the Levi’s T-shirts today with discounts applied. How much revenue  our store will generate (post discounts)?",
        'SQLQuery': """SELECT sum(a.total_amount * ((100-COALESCE(discounts.pct_discount,0))/100)) as total_revenue from
(select sum(price*stock_quantity) as total_amount, t_shirt_id from t_shirts where brand = 'Levi'
group by t_shirt_id) a left join discounts on a.t_shirt_id = discounts.t_shirt_id
 """,
        'SQLResult': "Result of the SQL query",
        'Answer': "21239.55"},

    {
        'Question': "If we have to sell all the Levi’s T-shirts today. How much revenue our store will generate without discount?",
        'SQLQuery': "SELECT SUM(price * stock_quantity) FROM t_shirts WHERE brand = 'Levi'",
        'SQLResult': "Result of the SQL query",
        'Answer': "21723"},

]