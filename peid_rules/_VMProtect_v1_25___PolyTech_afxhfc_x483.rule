rule __VMProtect_v1_25___PolyTech_afxhfc
{
	meta:
		description = "_ VMProtect v1_25 ___ PolyTech"
	strings:
		$a = {68????????E8????????8B750083C504E9}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
