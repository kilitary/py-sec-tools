rule _Upack_Patch__Dwing_xjwknd
{
	meta:
		description = "Upack_Patch __ Dwing"
	strings:
		$a = {813A0000000200000000}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
