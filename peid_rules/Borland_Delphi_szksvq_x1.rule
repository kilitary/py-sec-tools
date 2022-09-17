rule _Borland_Delphi_szksvq
{
	meta:
		description = "Borland Delphi"
	strings:
		$a = {558BEC83C4F0B8????4500E8??????FFA1????45008B00E8????FFFF8B0D}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
