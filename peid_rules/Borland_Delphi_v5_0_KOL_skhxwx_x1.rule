rule _Borland_Delphi_v5_0_KOL_skhxwx
{
	meta:
		description = "Borland Delphi v5_0 KOL"
	strings:
		$a = {558BEC83C4F0B8????4000E8????FFFFE8????FFFFE8????FFFF8BC00000000000000000000000}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
