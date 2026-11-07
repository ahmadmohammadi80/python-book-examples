# Python book chapter 07, example 2
choices = ["نامعتبر", "نمایش", "خروج"]
for choice in choices:
    if choice == "خروج":
        print("پایان")
        break
    if choice != "نمایش":
        print("دوباره تلاش کنید")
        continue
    print("اطلاعات نمایش داده شد")
