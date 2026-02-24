from datetime import date
from faker import Faker
import pandas as pd
import numpy as np


def generate_data(unique_amount: int, faker_str: str, country: str, product_dict: dict[str, float]) -> pd.DataFrame:
    
    fake = Faker(faker_str)
    customer_id_list: list[str] = [faker_str[3:]+str(x).zfill(6) for x in range(1, unique_amount + 1)]
    customer_dict_list: list[dict[str, object]] = [] 
    for i in range(unique_amount):
        customer_dict_list.append({
            "customer_id": customer_id_list[i], 
            "customer_name": fake.name(), 
            "customer_email": fake.email(), 
            "country": country
        })
    
    customer_df: pd.DataFrame = pd.DataFrame(customer_dict_list)
    order_df: pd. DataFrame = pd.DataFrame()
    product_df: pd. DataFrame = pd.DataFrame()

    start_date = date(2025, 1, 1)
    end_date = date(2025, 12, 31)
    date_range = pd.date_range(start_date, end_date)
    
    weights = np.where(date_range.month.isin([11, 12]), 5.0, 1.0)
    weights /= weights.sum()
    

    order_df["order_id"] = [str(x).zfill(7)+ faker_str[3:] for x in range(1, (unique_amount * 10) + 1)]
    order_df["date"] = np.random.choice(date_range, size=unique_amount * 10, p=weights)
    order_df["customer_id"] = np.random.choice(customer_df["customer_id"], size=unique_amount * 10)
    product_df["order_id"] = [str(x).zfill(7)+ faker_str[3:] for x in range(1, (unique_amount * 10) + 1)]
    product_df["product"] = np.random.choice(list(product_dict.keys()), size=unique_amount * 10)
    product_df["price"] = product_df["product"].map(product_dict)
    product_df["quantity"] = np.random.default_rng().integers(low=1, high=10, size=unique_amount * 10)
    product_df["order_value"] = product_df["price"] * product_df["quantity"]

    df_1: pd.DataFrame = pd.merge(order_df, customer_df, on="customer_id", how="left")
    df: pd.DataFrame = pd.merge(df_1, product_df, on="order_id", how="left")

    return df
    