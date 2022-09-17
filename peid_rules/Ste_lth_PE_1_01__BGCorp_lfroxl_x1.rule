rule _Ste_lth_PE_1_01__BGCorp_lfroxl
{
	meta:
		description = "Ste_lth PE 1_01 __ BGCorp"
	strings:
		$a = {??????????BA??????00}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
