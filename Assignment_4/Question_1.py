import csv
data = [
    ["Name","Address","Mobile","Email"],
    ["Sumit","Jaipur",8575847584,"Sumit@gmail.com"],
    ["Rajat","Udaipur",7854129547,"Rajat@gmail.com"],
    ["Vikas","chaksu",4574967212,"Vikas@gmail.com"],
    ["Akshay","Mumbai",9685741245,"Akshay@gmail.com"]
]
with open("data.csv", "w", newline="") as file:
     writer = csv.writer(file)
     for row in data:
        writer.writerow(row)