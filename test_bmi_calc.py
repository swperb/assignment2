import pytest

from bmi_calc import convert_to_inches, metric_conversion_weight, metric_conversion_height, meters_squared, bmi_conversion, bmi_category

class TestBmiCalc:

    def test_convert_to_inches(self):
        # Test arbitrary heights
        # Realistic values to ensure the function is working
        assert convert_to_inches("5 10") == 70
        assert convert_to_inches("5 5") == 65
        assert convert_to_inches("6 0") == 72

        # Test upper and lower boundaries
        # Nobody is 0 inches tall, nobody is 12 feet tall
        assert convert_to_inches("0 0") == 0
        assert convert_to_inches("12 0") == 144


    def test_metric_conversion_weight(self):
        # Test arbitrary weights
        # Realistic values to ensure the function is working
        assert metric_conversion_weight(150) == 67.5
        assert metric_conversion_weight(200) == 90
        assert metric_conversion_weight(100) == 45

        # Test upper and lower boundaries
        # Nobody weighs 0 pounds, nobody weighs 1000 pounds
        assert metric_conversion_weight(0) == 0
        assert metric_conversion_weight(1000) == 450


    def test_metric_conversion_height(self):
        # Test arbitrary heights
        # Realistic values to ensure the function is working
        assert metric_conversion_height(70) == 1.75
        assert metric_conversion_height(65) == 1.625
        assert metric_conversion_height(45) == 1.125

        # Test upper and lower boundaries
        # Nobody is 0 inches tall, nobody is 1000 inches tall
        assert metric_conversion_height(0) == 0
        assert metric_conversion_height(1000) == 25


    def test_meters_squared(self):
        # Test arbitrary values
        # Realistic values to ensure the function is working
        assert meters_squared(13) == 169
        assert meters_squared(16.5) == 272.25
        assert meters_squared(10) == 100

        # Test upper and lower boundaries
        # Nobody is 0 meters tall, nobody is 100 meters tall
        assert meters_squared(0) == 0
        assert meters_squared(100) == 10000


    def test_bmi_conversion(self):
        # Test conversions
        # Realistic values to ensure the function is working
        assert bmi_conversion(80, 130) == 14.625
        assert bmi_conversion(60, 100) == 20.0
        assert bmi_conversion(40, 75) == 33.75

        # Test upper and lower boundaries
        # Nobody is 10 inches tall and weighs 10 pounds
        assert bmi_conversion(10, 10) == 72.0
        # Nobody is 1000 inches tall and weighs 1000 pounds
        assert bmi_conversion(1000, 1000) == 0.72


    def test_bmi_category(self):

        # Utilize EPC boundary testing

        ## Test underweight subdomain
        # Test under point
        assert bmi_category(-1) == "Underweight"
        # Test minimum point
        assert bmi_category(0) == "Underweight"
        # Test interior point
        assert bmi_category(10) == "Underweight"
        # Test maximum point
        assert bmi_category(18.49) == "Underweight"
        # Test over point
        assert bmi_category(18.5) == "Normal weight"


        # Test normal weight subdomain
        # Test under point
        assert bmi_category(18.49) == "Underweight"
        # Test minimum point
        assert bmi_category(18.5) == "Normal weight"
        # Test interior point
        assert bmi_category(20) == "Normal weight"
        # Test maximum point
        assert bmi_category(24.99) == "Normal weight"
        # Test over point
        assert bmi_category(25) == "Overweight"


        ## Test over weight subdomain
        # Test under point
        assert bmi_category(24.99) == "Normal weight"
        # Test minimum point
        assert bmi_category(25) == "Overweight"
        # Test interior point
        assert bmi_category(28) == "Overweight"
        # Test maximum point
        assert bmi_category(29.99) == "Overweight"
        # Test over point
        assert bmi_category(30) == "Obese"


        ## Test obese subdomain
        # Test under point
        assert bmi_category(29.99) == "Overweight"
        # Test minimum point
        assert bmi_category(30) == "Obese"
        # Test interior point
        assert bmi_category(35) == "Obese"
        # Test maximum point
        assert bmi_category(39.99) == "Obese"
        # Test over point
        assert bmi_category(40) == "Obese"
        
