import csv

# Dictionary containing predefined stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "MSFT": 400,
    "AMZN": 170
}


# Function 1: Display welcome message
def welcome():

    print("\n" + "=" * 45)
    print("       STOCK PORTFOLIO TRACKER")
    print("=" * 45)

    print("\nAvailable Stocks:")

    for stock, price in stock_prices.items():
        print(f"{stock} : ${price}")


# Function 2: Get stock details from user
def get_portfolio():

    portfolio = {}

    try:
        number_of_stocks = int(
            input("\nHow many stock entries do you want to add? ")
        )

        if number_of_stocks <= 0:
            print("Please enter a number greater than zero.")
            return portfolio

    except ValueError:
        print("Invalid input! Please enter a whole number.")
        return portfolio

    for i in range(number_of_stocks):

        print(f"\nStock Entry {i + 1}")

        stock = input("Enter stock symbol (or EXIT to stop): ").strip().upper()

        if stock == "EXIT":
            print("Stock entry stopped.")
            break

        if stock not in stock_prices:
            print("Sorry, this stock is not available.")
            continue

        try:
            quantity = int(input("Enter quantity of shares: "))

            if quantity <= 0:
                print("Quantity must be greater than zero.")
                continue

            # Add duplicate stock quantities together
            portfolio[stock] = portfolio.get(stock, 0) + quantity

            print("Stock added successfully!")

        except ValueError:
            print("Invalid quantity! Please enter a whole number.")

    return portfolio


# Function 3: Calculate and display investment
def calculate_investment(portfolio):

    total_investment = 0

    print("\n========== YOUR PORTFOLIO ==========")

    if not portfolio:
        print("No stocks were added to your portfolio.")

    for stock, quantity in portfolio.items():

        price = stock_prices[stock]

        investment = price * quantity

        total_investment += investment

        print("\nStock:", stock)
        print("Price per share: $", price)
        print("Quantity:", quantity)
        print("Investment value: $", investment)

    print("\n====================================")
    print("Total Investment: $", total_investment)
    print("====================================")

    return total_investment


# Function 4: Save portfolio to CSV file
def save_portfolio(portfolio, total_investment):

    with open("portfolio.csv", "w", newline="") as file:

        writer = csv.writer(file)

        # Write column headings
        writer.writerow([
            "Stock",
            "Price",
            "Quantity",
            "Investment"
        ])

        # Write stock details
        for stock, quantity in portfolio.items():

            price = stock_prices[stock]

            investment = price * quantity

            writer.writerow([
                stock,
                price,
                quantity,
                investment
            ])

        # Write total investment
        writer.writerow([])
        writer.writerow(["Total Investment", "", "", total_investment])

    print("\nPortfolio saved successfully!")
    print("File name: portfolio.csv")


# Function 5: Main program
def main():

    welcome()

    portfolio = get_portfolio()

    total_investment = calculate_investment(portfolio)

    save_portfolio(portfolio, total_investment)

    print("\nThank you for using Stock Portfolio Tracker!")


# Start the program
if __name__ == "__main__":
    main()
