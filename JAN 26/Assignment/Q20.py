Q. Define a class that does currency conversion. The method you define must convert at least 10
foreign currency to NRP.
Solution:
    
class CurrencyConversion:

    @staticmethod
    def usd_to_nrp(rup):
        print(f"{rup} USD = {rup*113.69} Nepalese Rupee")

    @staticmethod
    def ic_to_nrp(rup):
        print(f"{rup} IndianCurrency = {rup * 1.6} Nepalese Rupee")

    @staticmethod
    def euro_to_nrp(rup):
        print(f"{rup} euro = {rup * 130.44} Nepalese Rupee ")

    @staticmethod
    def yuan_to_nrp(rup):
        print(f"{rup} Yuan = {rup * 16.88} Nepalese Rupee")

    @staticmethod
    def aud_to_nrp(rup):
        print(f"{rup} AuD = {rup * 82.56} Nepalese Rupee")

    @staticmethod
    def hkd_to_nrp(rup):
        print(f"{rup} HKD = {rup* 14.49} Nepalese Rupee")

    @staticmethod
    def won_to_nrp(rup):
        print(f"{rup} won = {rup * 10.18 / 100} Nepalese Rupee")

    @staticmethod
    def pound_to_nrp(rup):
        print(f"{rup} pound = {rup *148.57} Nepalese Rupee")

    @staticmethod
    def swiss_to_nrp(rup):
        print(f"{rup} swiss franc = {rup * 114.55} Nepalese Rupee")

    @staticmethod
    def uae_to_nrp(rup):
        print(f"{rup} UAE Dirham = {rup *30.95} Nepalese Rupee")


rups = CurrencyConversion()
rups.ic_to_nrp(10)
rups.usd_to_nrp(1)
rups.uae_to_nrp(1)
rups.euro_to_nrp(1)
rups.swiss_to_nrp(1)
rups.pound_to_nrp(1)
rups.hkd_to_nrp(1)
rups.aud_to_nrp(1)
rups.won_to_nrp(100)
rups.yuan_to_nrp(1)
