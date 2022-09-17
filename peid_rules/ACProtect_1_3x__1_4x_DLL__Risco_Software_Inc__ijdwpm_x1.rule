rule _ACProtect_1_3x__1_4x_DLL__Risco_Software_Inc__ijdwpm
{
	meta:
		description = "ACProtect 1_3x _ 1_4x DLL __ Risco Software Inc_"
	strings:
		$a = {807C2408010F85}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
