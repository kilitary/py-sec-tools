rule _Borland_Delphi_Setup_Module_uebhdd
{
	meta:
		description = "Borland Delphi Setup Module"
	strings:
		$a = {5589E5E8????????C9C3????455845}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
