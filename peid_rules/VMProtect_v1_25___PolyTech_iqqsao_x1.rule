rule _VMProtect_v1_25___PolyTech_iqqsao
{
	meta:
		description = "VMProtect v1_25 ___ PolyTech"
	strings:
		$a = {68????????E8????????555052}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
