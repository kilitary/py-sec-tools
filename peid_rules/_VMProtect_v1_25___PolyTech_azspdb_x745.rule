rule __VMProtect_v1_25___PolyTech_azspdb
{
	meta:
		description = "_ VMProtect v1_25 ___ PolyTech"
	strings:
		$a = {68????????E8????????56505550525157539C68000000008B74242C89E581ECC000000089E70375008A060FB6C083EEFFFF3485????????C3}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
