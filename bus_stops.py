"""
Остановки
Считать из csv-файла (с http://data.mos.ru/datasets/752) количество 
остановок, вывести улицу, на которой больше всего остановок.
"""
import csv

def main():
    with open('bus_stops.csv','r', encoding='UTF-8') as b:
        fields = ["ID", "Name", "Longitude_WGS84", "Latitude_WGS84", "Street", "AdmArea", "District", "RouteNumbers", "StationName", "Direction", "Pavilion", "OperatingOrgName", "EntryState", "global_id", "geoData"]
        reader = csv.DictReader(b, fields, delimiter=';')
        for row in reader:
            print(row)

if __name__ == "__main__":
    main()