rule __VMProtect_v1_25___PolyTech_skgzrg
{
	meta:
		description = "_ VMProtect v1_25 ___ PolyTech"
	strings:
		$a = {68????????E8????????525750535156559C5068000000008B74242C89E581ECC000000089E70375008A060FB6C08D7601FF3485????????C3}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
