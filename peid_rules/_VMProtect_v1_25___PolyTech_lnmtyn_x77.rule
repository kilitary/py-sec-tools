rule __VMProtect_v1_25___PolyTech_lnmtyn
{
	meta:
		description = "_ VMProtect v1_25 ___ PolyTech"
	strings:
		$a = {68????????E8????????8A06668B550083EEFF83C50266891407E9}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
