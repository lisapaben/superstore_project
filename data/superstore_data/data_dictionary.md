# 📘 Superstore Data Dictionary

| Column Name           | Description                                                  | Type        |
|-----------------------|--------------------------------------------------------------|-------------|
| row_id                | Unique ID for each row                                       | Integer     |
| order_id              | Unique identifier for each order                             | String      |
| order_date            | Date the order was placed                                    | Date        |
| ship_date             | Date the order was shipped                                   | Date        |
| ship_mode             | Shipping Mode specified by the Customer                      | String      |
| customer_id           |
| customer_name
| segment               | Customer segment                                             | String      |
| country
| city
| state
| postal_code
| region                | Geographic region of the order                               | String      |
| product_id
| category              | Product category                                             | String      |
| sub_category          | Product sub-category                                         | String      |
| product_name
| sales                 | Total sales amount                                           | Float       |
| quantity
| discount              | Discount applied to the order                                | Float       |
| profit                | Profit earned from the order                                 | Float       |
| shipping_delay_days   | Days between order and shipment                              | Integer     |
| profit_margin         | Profit divided by sales                                      | Float       |
| profit_zscore         | Z-score of profit for outlier detection                      | Float       |
| profit_outlier        | Flag for profit outliers (`Yes`/`No`)                        | String      |