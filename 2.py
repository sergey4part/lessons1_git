# function VAT df
def get_vat(payment, persent=20):
	try:
		vat = payment / 100 * persent
		vat = round(vat, 2)
		return "Sum VAT: {}".format(vat)
	except TypeError:
		return "Check"
result = get_vat(400)
print(result)