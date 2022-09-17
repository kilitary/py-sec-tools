rule __VMProtect_v1_25___PolyTech_eckted
{
	meta:
		description = "_ VMProtect v1_25 ___ PolyTech"
	strings:
		$a = {68????????E8????????5156565355579C525068000000008B74242C89E581ECC000000089E70375008A068D76010FB6C0FF2485????????8B45008A550483C5068810E9}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
