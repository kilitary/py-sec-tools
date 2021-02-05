rule _VMProtect_1_06_1_07__PolyTech_qcrfez
{
	meta:
		description = "VMProtect 1_06__1_07 __ PolyTech"
	strings:
		$a = {9C6068000000008B742428BF????????FC89F3033424AC00D8}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
