rule _Upack_0_37_beta__Dwing_uunvok
{
	meta:
		description = "Upack 0_37 beta __ Dwing"
	strings:
		$a = {BEE011????FF36E9C30000004801????0B014B45524E454C33322E444C4C}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
