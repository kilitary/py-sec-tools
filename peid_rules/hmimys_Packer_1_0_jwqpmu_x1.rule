rule _hmimys_Packer_1_0_jwqpmu
{
	meta:
		description = "hmimys_Packer 1_0"
	strings:
		$a = {5E83C664AD50AD5083EE6CAD50AD50AD50AD50AD50E8E7070000}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
