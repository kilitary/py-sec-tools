rule _Borland_Delphi_v6_0_ykpqkx
{
	meta:
		description = "Borland Delphi v6_0"
	strings:
		$a = {68001040006804010000E83903000005001040C6005C68????????68????????6A00E8}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
