# Cathay-Hackathon
Training a Machine Leaning Model to accuratly predict fuel burn (and thus carbon emissions for each passenger) for a flight trip. <br> 

## Result 
Model accuracy of ~ 91%

## Running Instructions
- Run the file train_regression.py to train and see the accuracy of the model. 

## Dataset 
Data taken from the US bureau of statistics
 <a href='https://www.transtats.bts.gov/Fields.asp?gnoyr_VQ=FIM'> DATABASE </a> <br>
 This produces database such as below: <br> <br> 
 $ head T_T100D_SEGMENT_US_CARRIER_ONLY.csv <br> <br>
DEPARTURES_PERFORMED,PAYLOAD,SEATS,PASSENGERS,FREIGHT,DISTANCE,RAMP_TO_RAMP,AIR_TIME,AIRLINE_ID,UNIQUE_CARRIER_NAME,ORIGIN_AIRPORT_ID,ORIGIN,DEST_AIRPORT_ID,DEST,AIRCRAFT_GROUP,AIRCRAFT_TYPE,AIRCRAFT_CONFIG,YEAR <br>
0.00,0.00,0.00,0.00,0.00,2500.00,0.00,0.00,19977,United Air Lines Inc.,14893,SMF,11618,EWR,6,614,1,2022 <br>
0.00,0.00,0.00,0.00,0.00,472.00,0.00,0.00,19977,United Air Lines Inc.,13871,OMA,11292,DEN,6,614,1,2022 <br>
0.00,0.00,0.00,0.00,0.00,472.00,0.00,0.00,19977,United Air Lines Inc.,11292,DEN,13871,OMA,6,614,1,2022 <br>
0.00,0.00,0.00,0.00,0.00,996.00,0.00,0.00,19977,United Air Lines Inc.,11603,EUG,11292,DEN,6,614,1,2022 <br>

## Challenges faced 
### FDR DATA NOT AVAIALABLE 
This is by far the biggest challenge faced during this project. It would be ideal to train a model using real 
past flight record data, however since this data is not publicly available, there had to be some adjustments made:
 
- Couldn't account for the Aircraft Model.
- However, there is an aircraft group (divided by engine type) which helps 
- The Target variable, i.e, Fuel Burn was estimated using a formula used in addFuel.py (Ideally, using FDR data would make this redundant and allow us to increase the accuracy of our model in predicting carbon emissions)

## Further Potential Improvements 
With the availability of FDR, many further improvements can be made by improving feature selection. It would allow 
us to do many things such as: 
- Take weather factors such as wind speed, temperature, pressure into account 
- Get exact payload details 
- Take efficiency of different aircrafts into account (for ex. A new Airbus A350 is bound to be more efficient compared to an aircraft that has been in service for more than 10 years)

These factors should increase the accuracy further. 
