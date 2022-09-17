rule __VMProtect_v1_25___PolyTech_egcqxk
{
	meta:
		description = "_ VMProtect v1_25 ___ PolyTech"
	strings:
		$a = {68????????E8????????0FB60646668B550083C502881407E9}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
