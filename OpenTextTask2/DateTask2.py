from datetime import datetime

# Function to convert any datetime format to expected datetime format
#Function to convert any date time format to expected date time format
def format_date(date_str: str, input_format: str, output_format: str) -> str:
    dt = datetime.strptime(date_str, input_format)  # parse text -> datetime
    return dt.strftime(output_format)

print(format_date("09-10-2025", "%m-%d-%Y", "%m/%d/%Y"))  # -> "07/05/2025"
print(format_date("2025/09/10", "%Y/%m/%d", "%d-%b-%Y"))  # -> "07-May-2025"
print(format_date("09-10-25", "%d-%m-%y", "%Y.%m.%d"))    # -> "2025.07.05"