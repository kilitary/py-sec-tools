rule __VMProtect_v1_25___PolyTech_jlvcih
{
	meta:
		description = "_ VMProtect v1_25 ___ PolyTech"
	strings:
		$a = {68????????E8????????515756529C5053555768000000008B74242C89E581ECC000000089E70375008A060FB6C083C6018D0C85????????FF2189EC595F5D5B589D5A5E5959C3}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
