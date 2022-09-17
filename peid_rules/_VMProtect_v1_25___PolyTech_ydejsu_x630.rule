rule __VMProtect_v1_25___PolyTech_ydejsu
{
	meta:
		description = "_ VMProtect v1_25 ___ PolyTech"
	strings:
		$a = {68????????E8????????5352559C575651505468000000008B74242C89E581ECC000000089E70375008A068D76010FB6C0FF2485????????89EC5A5E58595E5F9D5D5A5BC3}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
