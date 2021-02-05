rule __VMProtect_v1_25___PolyTech_zjuend
{
	meta:
		description = "_ VMProtect v1_25 ___ PolyTech"
	strings:
		$a = {68????????E8????????89EC5B5E9D5D5B595A585F5AC3}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
