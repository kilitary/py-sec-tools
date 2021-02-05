rule __VMProtect_v1_25___PolyTech_mnvrrx
{
	meta:
		description = "_ VMProtect v1_25 ___ PolyTech"
	strings:
		$a = {68????????E8????????0FB606668B550083EEFF83C502881407E9}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
