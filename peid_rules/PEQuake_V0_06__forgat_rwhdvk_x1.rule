rule _PEQuake_V0_06__forgat_rwhdvk
{
	meta:
		description = "PEQuake V0_06 __ forgat"
	strings:
		$a = {E8A5000000}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
