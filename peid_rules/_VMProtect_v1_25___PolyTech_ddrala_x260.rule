rule __VMProtect_v1_25___PolyTech_ddrala
{
	meta:
		description = "_ VMProtect v1_25 ___ PolyTech"
	strings:
		$a = {68????????E8????????8B0683ED0489450083EEFCE9}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
