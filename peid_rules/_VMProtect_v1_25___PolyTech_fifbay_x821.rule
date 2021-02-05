rule __VMProtect_v1_25___PolyTech_fifbay
{
	meta:
		description = "_ VMProtect v1_25 ___ PolyTech"
	strings:
		$a = {8B450083C502668B0066894500E9A50600008B4500668B550483C506668910E9}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
