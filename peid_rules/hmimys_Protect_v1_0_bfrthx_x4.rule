rule _hmimys_Protect_v1_0_bfrthx
{
	meta:
		description = "hmimys Protect v1_0"
	strings:
		$a = {5E83C664AD50AD5083EE6CAD50AD50AD50AD50AD50E8}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
