-- Delete the first Volvo (id is 5 instead of 4 as the car_ID is auto incremental and starting from 1)
DELETE FROM cars WHERE (`car_ID` = '5');
