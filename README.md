# Cathay-Hackathon
Training a Machine Leaning Model to get accurate Carbon Emissions per passenger per flight. <br> 

## Dataset 
Data taken from the US bureau of statistics
 <a href='https://www.transtats.bts.gov/Fields.asp?gnoyr_VQ=FIM'> DATABASE </a> <br>
 This produces database such as below: <br>
 $ head T_T100D_SEGMENT_US_CARRIER_ONLY.csv <br>
DEPARTURES_PERFORMED,PAYLOAD,SEATS,PASSENGERS,FREIGHT,DISTANCE,RAMP_TO_RAMP,AIR_TIME,AIRLINE_ID,UNIQUE_CARRIER_NAME,ORIGIN_AIRPORT_ID,ORIGIN,DEST_AIRPORT_ID,DEST,AIRCRAFT_GROUP,AIRCRAFT_TYPE,AIRCRAFT_CONFIG,YEAR <br>
0.00,0.00,0.00,0.00,0.00,2500.00,0.00,0.00,19977,United Air Lines Inc.,14893,SMF,11618,EWR,6,614,1,2022 <br>
0.00,0.00,0.00,0.00,0.00,472.00,0.00,0.00,19977,United Air Lines Inc.,13871,OMA,11292,DEN,6,614,1,2022 <br>
0.00,0.00,0.00,0.00,0.00,472.00,0.00,0.00,19977,United Air Lines Inc.,11292,DEN,13871,OMA,6,614,1,2022 <br>
0.00,0.00,0.00,0.00,0.00,996.00,0.00,0.00,19977,United Air Lines Inc.,11603,EUG,11292,DEN,6,614,1,2022 <br>

## Challenges faced 
### FDR DATA NOT AVAIALABLE 
This is by far the biggest challenge faced during this project. It would be ideal to train a model using real 
past flight record data, however since this data is not publicly available, there had to be some adjustments made:
(P.S. If you wanna see how much I struggled acquiring a dataset, look at the logs)  
- Couldn't account for the Aircraft Model (Since the particular database does not disclose that info)
- However there is an aircraft which helps