rule __VMProtect_v1_25___PolyTech_kagsfd
{
	meta:
		description = "_ VMProtect v1_25 ___ PolyTech"
	strings:
		$a = {68????????E8????????53559C56575150525568000000008B74242C89E581ECC000000089E70375008A06460FB6C0FF2485????????8B450083C502668B0066894500E9}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
