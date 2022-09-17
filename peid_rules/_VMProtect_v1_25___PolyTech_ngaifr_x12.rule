rule __VMProtect_v1_25___PolyTech_ngaifr
{
	meta:
		description = "_ VMProtect v1_25 ___ PolyTech"
	strings:
		$a = {68????????E8????????F75500668B450083ED02662145049C8F4500E9}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
