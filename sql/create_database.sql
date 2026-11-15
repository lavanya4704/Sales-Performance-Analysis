
CREATE TABLE sales_data (
    order_id VARCHAR(30),
    order_date DATE,
    region VARCHAR(30),
    category VARCHAR(50),
    product_name VARCHAR(100),
    sales DECIMAL(12,2),
    quantity INT,
    profit DECIMAL(12,2)
);

INSERT INTO sales_data VALUES
('O001', '2025-01-05', 'East', 'Technology', 'Laptop', 800.00, 1, 120.00),
('O002', '2025-01-12', 'West', 'Furniture', 'Chair', 150.00, 2, 30.00),
('O003', '2025-02-08', 'East', 'Office Supplies', 'Paper', 50.00, 5, 10.00),
('O004', '2025-02-15', 'South', 'Technology', 'Monitor', 300.00, 2, 45.00),
('O005', '2025-03-02', 'West', 'Furniture', 'Desk', 400.00, 1, -20.00);