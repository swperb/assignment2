import pytest

from bmi_calc import convert_to_inches, metric_conversion_weight, metric_conversion_height, meters_squared, bmi_conversion, bmi_category

class TestBmiCalc:

    def test_convert_to_inches(self):
        # Test arbitrary heights
        assert convert_to_inches("5 10") == 70
        assert convert_to_inches("5 5") == 65
        assert convert_to_inches("6 0") == 72


    def test_metric_conversion_weight(self):
        # Test arbitrary weights
        assert metric_conversion_weight(150) == 67.5
        assert metric_conversion_weight(200) == 90
        assert metric_conversion_weight(100) == 45


    def test_metric_conversion_height(self):
        # Test arbitrary heights
        assert metric_conversion_height(70) == 1.75
        assert metric_conversion_height(65) == 1.625
        assert metric_conversion_height(45) == 1.125


    def test_meters_squared(self):
        # Test arbitrary values
        assert meters_squared(13) == 169
        assert meters_squared(16.5) == 272.25
        assert meters_squared(10) == 100


    def test_bmi_conversion(self):
        # Test conversions
        assert bmi_conversion(80, 130) == 14.625
        assert bmi_conversion(60, 200) == 40.0
        assert bmi_conversion(40, 100) == 45.0


    def test_bmi_category(self):

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
        
