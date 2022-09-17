rule __VMProtect_v1_25___PolyTech_bezbxg
{
	meta:
		description = "_ VMProtect v1_25 ___ PolyTech"
	strings:
		$a = {68????????E8????????8A0683ED026689450083EEFFE9}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
