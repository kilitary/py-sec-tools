rule __VMProtect_v1_25___PolyTech_ttohug
{
	meta:
		description = "_ VMProtect v1_25 ___ PolyTech"
	strings:
		$a = {68????????E8????????55505752519C53565468000000008B74242C89E581ECC000000089E70375008A060FB6C08D7601FF2485????????8B0683ED0489450083C604E9}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
