rule __VMProtect_v1_25___PolyTech_ihrwxu
{
	meta:
		description = "_ VMProtect v1_25 ___ PolyTech"
	strings:
		$a = {68????????E8????????8B450083C50266368B0066894500E9}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
