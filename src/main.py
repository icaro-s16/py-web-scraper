from scraper.scraper_core   import scraper_run
from scraper.school_budget  import SchoolBudget
from typing                 import List
from scraper.csv_converter  import scraper_results_to_csv

if __name__ == "__main__":
    start_page: int = int(input("Enter the starting page:"))
    final_page: int = int(input("Enter the targed page:"))

    if (start_page > final_page):
        raise RuntimeError("[Error] The start page must be greater than the target page.")

    start_page -= 1
    final_page += 1 

    schools_budget: List[SchoolBudget] = scraper_run(
        start_page=start_page, 
        final_page=final_page
    )
    csv_name: str = input("CSV filename (no .csv needed):")
    scraper_results_to_csv(
        csv_name, 
        schools_budget
    )





