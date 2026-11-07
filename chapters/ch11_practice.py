# Python book chapter 11, worked practice
# نمونه یک‌فایلی از الگوی entry point
def total_cost(prices):
    return sum(prices)

def main():
    prices = [12000, 18000]
    print("جمع:", total_cost(prices))

if __name__ == "__main__":
    main()
