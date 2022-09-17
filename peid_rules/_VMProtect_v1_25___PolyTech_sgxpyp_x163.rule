rule __VMProtect_v1_25___PolyTech_sgxpyp
{
	meta:
		description = "_ VMProtect v1_25 ___ PolyTech"
	strings:
		$a = {68????????E8????????8A0646668B550083C50266891407E9}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
