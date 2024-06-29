# from eircode.address import Address
# address = Address(f"{3} MAIN STREET, Co. CLARE", proxy=False, reverse=False)

# print(address.serialize())
from eircode.address import Address
address = Address('D15X3P8', proxy=False, reverse=True)
print(address.serialize())