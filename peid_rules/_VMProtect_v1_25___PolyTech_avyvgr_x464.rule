rule __VMProtect_v1_25___PolyTech_avyvgr
{
	meta:
		description = "_ VMProtect v1_25 ___ PolyTech"
	strings:
		$a = {68????????E8????????89EC5B5E5A599D5F5D5B585BC3}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
