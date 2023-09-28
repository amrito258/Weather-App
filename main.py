from current_weather import get_current_weather_report

print(" : Welcome Amrito's Weather App!\n")
city = input('Enter a city name: ')
    
def main():
    all_info = get_current_weather_report(city)
    w_data = all_info[0]
    report = all_info[1]
        
    try:
        if w_data['message'] == 'city not found':
            print(' : City not found ):')
        
    except:
        print(report)
    
    txt_file_choice = input('Do you save the report in a text file (y/n): ')
    
    try:
        if txt_file_choice == 'y':
            report_file = open('report.txt', 'w', encoding='utf-8')
            report_file.write(report)
            report_file.close()
            print('Print Successfully\nThank you for using my Weather App')
            
        else:
            print(' : Thank you for using my Weather App!')
            
    except:
        print(" : Can't write in text file")
    
if __name__ == '__main__':
    main()