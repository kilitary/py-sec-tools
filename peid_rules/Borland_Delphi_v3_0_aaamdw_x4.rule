rule _Borland_Delphi_v3_0_aaamdw
{
	meta:
		description = "Borland Delphi v3_0"
	strings:
		$a = {83????6A00FF15F8100BB08D??????516A086A006A0068}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
