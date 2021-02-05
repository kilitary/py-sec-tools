rule _Borland_Delphi_Setup_Module_vpkpcb
{
	meta:
		description = "Borland Delphi Setup Module"
	strings:
		$a = {558BEC83C4??53565733C08945F08945D48945D0E8}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
