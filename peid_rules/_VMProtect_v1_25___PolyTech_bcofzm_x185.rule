rule __VMProtect_v1_25___PolyTech_bcofzm
{
	meta:
		description = "_ VMProtect v1_25 ___ PolyTech"
	strings:
		$a = {68????????E8????????8B4500668B550483C50666368910E9}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
