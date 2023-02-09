class Solution:
    def __init__(self):
        self.months = {
            "Jan" : "01", "Feb" : "02", "Mar" : "03", 
            "Apr" : "04", "May" : "05", "Jun" : "06", 
            "Jul" : "07", "Aug" : "08", "Sep" : "09", 
            "Oct" : "10", "Nov" : "11", "Dec" : "12"
        }
        
    def reformatDate(self, date: str) -> str:
        
        day, month, year = date.split(" ")
        
        day = day.rstrip("th").rstrip("nd").rstrip("st").rstrip("rd").rjust(2, "0")
        
        # print(day, month, year)
        ans = year + "-" + self.months[month] + "-" + day
        
        
        return ans